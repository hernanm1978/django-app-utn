# Generated by Django 3.2.5 on 2023-01-31 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0008_alter_contactoconsulta_estado_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactorespuesta',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]