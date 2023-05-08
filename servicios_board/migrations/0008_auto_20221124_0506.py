# Generated by Django 3.2.5 on 2022-11-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios_board', '0007_alter_servicio_descripcion_servicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='categoria',
        ),
        migrations.AddField(
            model_name='servicio',
            name='estado_actual',
            field=models.CharField(choices=[('En Espera Diagnostico', 'En Espera Diagnostico'), ('En Diagnostico', 'En Diagnostico'), ('Esperando Aprobacion Cliente', 'Esperando Aprobacion Cliente'), ('Servicio Iniciado', 'Servicio Iniciado'), ('Servicio Finalizado', 'Servicio Finalizado'), ('Pago Pendiente', 'Pago Pendiente'), ('Esperando Retiro', 'Esperando Retiro'), ('Entregado', 'Entregado')], default='En Espera Diagnostico', max_length=30),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
