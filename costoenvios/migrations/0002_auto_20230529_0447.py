# Generated by Django 3.2.5 on 2023-05-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costoenvios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costosenvios',
            name='precio_rapido',
            field=models.IntegerField(verbose_name='Precio Rapido AR$'),
        ),
        migrations.AlterField(
            model_name='costosenvios',
            name='precio_std',
            field=models.IntegerField(verbose_name='Precio Standard AR$'),
        ),
    ]
