from django.urls import path

from . import views

app_name = 'marchine'
urlpatterns = [
    path('', views.home, name='home'),
    path('createmachine/', views.createmarchine, name='createmarchine'),
    path('editmachine/', views.editmarchine, name='editmarchine'),
    path('deletemarchine/', views.deletemarchine, name='deletemarchine'),
]
