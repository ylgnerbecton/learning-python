# Generated by Django 2.2.4 on 2020-11-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('razão', models.CharField(blank=True, max_length=100, null=True, verbose_name='razão social')),
                ('dono', models.CharField(blank=True, max_length=100, null=True, verbose_name='nome dono')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
                ('CNPJ', models.CharField(blank=True, max_length=14, null=True, verbose_name='CNPJ')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('telefone_para_contato', models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone')),
                ('negocios', models.CharField(blank=True, max_length=200, null=True, verbose_name='tipo de negocio')),
                ('pais', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pais')),
                ('estado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('Bairro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('rua', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua')),
                ('numero', models.CharField(blank=True, max_length=100, null=True, verbose_name='Numero')),
                ('complemento', models.CharField(blank=True, max_length=300, null=True, verbose_name='Complemento')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
