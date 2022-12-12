from datetime import timedelta

from django.contrib import messages
from django.db.models import Sum
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from parse import parse

from .models import Marchine


# Create your views here.
def home(request):
    template = 'marchine/pages/home.html'
    dadosmarchines = Marchine.objects.all().order_by('-data_criacao')
    search = request.GET.get('search')
    if search:
        dadosmarchines = dadosmarchines.filter(
            data_criacao__icontains=search
        )

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        end_date = parse(end_date) + timedelta(days=1)
        dadosmarchines = dadosmarchines.filter(
            data_criacao__range=[start_date, end_date]
        )

    # calcula o total diario
    ValordiarioEntrada = Marchine.objects.all().filter(
        acao=True, data_criacao__day=timezone.now().day).aggregate(Sum('valor'))  # noqa
    if ValordiarioEntrada['valor__sum'] is None:
        ValordiarioEntrada['valor__sum'] = 0

    ValordiarioSaida = Marchine.objects.all().filter(
        acao=False, data_criacao__day=timezone.now().day).aggregate(Sum('valor'))  # noqa
    if ValordiarioSaida['valor__sum'] is None:
        ValordiarioSaida['valor__sum'] = 0

    TotalDiario = ValordiarioEntrada['valor__sum'] -\
        ValordiarioSaida['valor__sum']

    # calcula o total mensal
    ValorMensalEntrada = Marchine.objects.all().filter(
        acao=True, data_criacao__month=timezone.now().month).aggregate(Sum('valor'))  # noqa
    if ValorMensalEntrada['valor__sum'] is None:
        ValorMensalEntrada['valor__sum'] = 0
    ValorMensalSaida = Marchine.objects.all().filter(
        acao=False, data_criacao__month=timezone.now().month).aggregate(Sum('valor'))  # noqa
    if ValorMensalSaida['valor__sum'] is None:
        ValorMensalSaida['valor__sum'] = 0

    TotalMensal = ValorMensalEntrada['valor__sum'] - \
        ValorMensalSaida['valor__sum']

    # calcula o total anual
    ValorAnualEntrada = Marchine.objects.all().filter(
        acao=True, data_criacao__year=timezone.now().year).aggregate(Sum('valor'))  # noqa
    if ValorAnualEntrada['valor__sum'] is None:
        ValorAnualEntrada['valor__sum'] = 0

    ValorAnualSaida = Marchine.objects.all().filter(
        acao=False, data_criacao__year=timezone.now().year).aggregate(Sum('valor'))  # noqa
    if ValorAnualSaida['valor__sum'] is None:
        ValorAnualSaida['valor__sum'] = 0

    TotalAnual = ValorAnualEntrada['valor__sum'] - \
        ValorAnualSaida['valor__sum']

    contexto = {
        'dadosmarchines': dadosmarchines,
        'TotalDiario': TotalDiario,
        'TotalMensal': TotalMensal,
        'TotalAnual': TotalAnual,

    }

    return render(request, template, contexto)


def createmarchine(request):
    if not request.POST:
        raise Http404()
    if request.method == 'POST':
        valor = request.POST.get('valor')
        if 'acao' in request.POST:
            acao = request.POST.get('acao')
            acao = True
        else:
            acao = False
        Marchine.objects.create(valor=valor, acao=acao)
        messages.success(request, 'Data saved successfully!')
        return redirect('marchine:home')
    else:
        messages.error(request, 'Data not saved!')
        return redirect(reverse('marchine:home'))


def editmarchine(request):
    if not request.POST:
        raise Http404()
    id = request.POST.get('marchine_id')
    marchineedit = get_object_or_404(Marchine, id=id)
    if request.method == 'POST':
        marchineedit.valor = request.POST.get('valor')
        if 'acao' in request.POST:
            marchineedit.acao = request.POST.get('acao')
            marchineedit.acao = True
        else:
            marchineedit.acao = False
        marchineedit.save()
        messages.success(request, 'Data saved successfully!')
        return redirect('marchine:home')
    else:
        messages.error(request, 'Data not saved!')
        return redirect(reverse('marchine:home'))


def deletemarchine(request):
    if not request.POST:
        raise Http404()

    id = request.POST.get('marchine_id')

    marchinedelete = get_object_or_404(Marchine, id=id)

    marchinedelete.delete()
    messages.success(request, 'Data successfully deleted!')
    return redirect(reverse('marchine:home'))
