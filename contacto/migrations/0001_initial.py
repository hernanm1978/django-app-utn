# Generated by Django 4.1 on 2023-01-29 05:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoConsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('email', models.EmailField(max_length=50)),
                ('estado_respuesta', models.CharField(choices=[('Contastada', 'Contastada'), ('No Contestada', 'No Contestada'), ('En Proceso', 'En Proceso')], default='No Contestada', max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_consulta', models.DateTimeField(blank=True, verbose_name=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='ContactoRespuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField()),
                ('fecha_consulta', models.DateTimeField(blank=True, verbose_name=datetime.datetime.now)),
                ('consulta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contacto.contactoconsulta')),
            ],
        ),
    ]