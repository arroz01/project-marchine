# Generated by Django 4.1 on 2022-12-12 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marchine', '0002_alter_marchine_acao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marchine',
            options={'ordering': ['-data_criacao'], 'verbose_name': 'Marchine', 'verbose_name_plural': 'Marchines'},
        ),
    ]
