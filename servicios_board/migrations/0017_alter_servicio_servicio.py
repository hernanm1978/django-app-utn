# Generated by Django 3.2.5 on 2022-11-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios_board', '0016_alter_servicio_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='servicio',
            field=models.CharField(choices=[('Recupero De Datos', 'Recupero De Datos'), ('Borrado Seguro De Datos', 'Borrado Seguro De Datos'), ('Reparacion Pedal Guitarra/Bajo', 'Reparacion Pedal Guitarra/Bajo'), ('Reparacion Parlante', 'Reparacion Parlante'), ('Reparacion Joystick PS-4', 'Reparacion Joystick PS-4'), ('Reparacion Joystick PS-5', 'Reparacion Joystick PS-5'), ('Reparacion Joystick XBOX-ONE', 'Reparacion Joystick XBOX-ONE'), ('Reparacion Joystick XBOX-360', 'Reparacion Joystick XBOX-360'), ('Reparacion PC/Notebook', 'Reparacion PC/Notebook'), ('Reparaciones Varias', 'Reparaciones Varias')], max_length=30),
        ),
    ]
