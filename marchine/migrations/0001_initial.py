# Generated by Django 4.1 on 2022-12-12 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marchine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(default=0)),
                ('acao', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
