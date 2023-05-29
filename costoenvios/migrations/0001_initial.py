# Generated by Django 3.2.5 on 2023-05-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostosEnvios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=60)),
                ('precio_std', models.IntegerField(verbose_name='Precio AR$')),
                ('precio_rapido', models.IntegerField(verbose_name='Precio AR$')),
                ('fecha_actualizacion_valor', models.DateField(verbose_name='Fecha de actualizacion valor')),
                ('estado_actual', models.CharField(choices=[('Destino No Activo', 'Destino No Activo'), ('Destino Activo', 'Destino Activo'), ('Actualizar!', 'Actualizar!')], default='Destino Activo', max_length=30)),
            ],
        ),
    ]
