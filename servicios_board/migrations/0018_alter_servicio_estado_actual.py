# Generated by Django 3.2.5 on 2022-11-25 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios_board', '0017_alter_servicio_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='estado_actual',
            field=models.CharField(choices=[('En Espera Diagnostico', 'En Espera Diagnostico'), ('En Diagnostico', 'En Diagnostico'), ('Esperando Aprobacion Cliente', 'Esperando Aprobacion Cliente'), ('Servicio Iniciado', 'Servicio Iniciado'), ('Servicio Finalizado', 'Servicio Finalizado'), ('Pago Pendiente', 'Pago Pendiente'), ('Esperando Retiro', 'Esperando Retiro'), ('Entregado', 'Entregado'), ('No Aprobado Esperando Retiro', 'No Aprobado Esperando Retiro')], default='En Espera Diagnostico', max_length=30),
        ),
    ]
