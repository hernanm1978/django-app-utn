# Generated by Django 3.2.5 on 2022-12-28 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_store_cantidad_disponible'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='stock_valor',
            field=models.IntegerField(null=True, verbose_name='Valor Stock AR$'),
        ),
    ]