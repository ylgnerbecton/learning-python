# Generated by Django 2.2.4 on 2020-11-26 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Cidade')),
                ('latitude', models.DecimalField(blank=True, decimal_places=12, max_digits=14, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=12, max_digits=14, null=True)),
                ('cod_ibge', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cidade',
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.City')),
            ],
            options={
                'verbose_name_plural': 'Bairro',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uf', models.CharField(max_length=2, verbose_name='Estado')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_ibge', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('zip_code', models.CharField(max_length=10, verbose_name='CEP')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('place_type', models.CharField(blank=True, max_length=80, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=12, max_digits=14, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=12, max_digits=14, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.City')),
                ('neighborhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Neighborhood')),
            ],
            options={
                'verbose_name_plural': 'Localidade',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, max_length=2, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.State'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('street', models.CharField(blank=True, max_length=300, null=True, verbose_name='Rua')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('reference_point', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ponto de referência')),
                ('latitude', models.DecimalField(blank=True, decimal_places=12, max_digits=14, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=12, max_digits=14, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.City')),
                ('neighborhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Neighborhood')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Place')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.State')),
            ],
            options={
                'verbose_name_plural': 'Endereço',
            },
        ),
    ]
