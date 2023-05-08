# Generated by Django 3.2.5 on 2022-11-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios_board', '0002_servicios_valor_presupuestado1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=200)),
                ('cliente', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('dispositivo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_ingreso', models.DateTimeField(verbose_name='Fecha de Ingreso')),
                ('estado_actual', models.CharField(max_length=200)),
                ('entrega_estimada', models.DateField(verbose_name='Fecha Estimada de Entrega')),
                ('valor_presupuestado1', models.IntegerField(verbose_name='Valor Presupuestado')),
                ('fecha_presupuesto', models.DateField(verbose_name='Fecha Presupuesto')),
            ],
        ),
        migrations.DeleteModel(
            name='Servicios',
        ),
    ]