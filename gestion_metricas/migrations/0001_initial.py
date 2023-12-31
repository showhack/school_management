# Generated by Django 4.2.6 on 2023-11-01 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistribucionAcentosCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DistribucionAcentosPrioridades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DistribucionVolSemNXContenidoCualidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DistribucionVolSemNXContenidoDistribucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DistribucionVolSemNXRelacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esta_marcado', models.BooleanField(default=False)),
                ('porciento', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cualidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_metricas.distribucionvolsemnxcontenidocualidad')),
                ('distribucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_metricas.distribucionvolsemnxcontenidodistribucion')),
            ],
        ),
        migrations.CreateModel(
            name='DistribucionAcentosSubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_metricas.distribucionacentoscategoria')),
            ],
        ),
        migrations.CreateModel(
            name='DistribucionAcentosRelacionPrioridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=50)),
                ('prioridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_metricas.distribucionacentosprioridades')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_metricas.distribucionacentossubcategoria')),
            ],
        ),
        migrations.AddField(
            model_name='distribucionacentosprioridades',
            name='subcategorias',
            field=models.ManyToManyField(related_name='prioridades', through='gestion_metricas.DistribucionAcentosRelacionPrioridad', to='gestion_metricas.distribucionacentossubcategoria'),
        ),
    ]
