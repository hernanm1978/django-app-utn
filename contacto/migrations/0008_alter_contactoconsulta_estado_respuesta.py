# Generated by Django 3.2.5 on 2023-01-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0007_alter_contactorespuesta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactoconsulta',
            name='estado_respuesta',
            field=models.CharField(choices=[('Contestada', 'Contestada'), ('No Contestada', 'No Contestada'), ('En Proceso', 'En Proceso')], default='No Contestada', max_length=50),
        ),
    ]