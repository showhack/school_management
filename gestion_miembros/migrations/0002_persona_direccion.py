# Generated by Django 4.2.6 on 2023-11-07 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_miembros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='direccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='gestion_miembros.direccion'),
            preserve_default=False,
        ),
    ]
