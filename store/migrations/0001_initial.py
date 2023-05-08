# Generated by Django 3.2.5 on 2022-12-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(choices=[('Filtro 80x80mm', 'Filtro 80x80mm'), ('Filtro 120x120mm', 'Filtro 120x120mm'), ('Filtro 140x140mm', 'Filtro 140x140mm'), ('Disco Rigido', 'Disco Rigido')], max_length=60)),
                ('descripcion', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('dispositivo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de Publicacion')),
                ('estado_actual', models.CharField(choices=[('No Publicado', 'No Publicado'), ('Publicado', 'Publicado'), ('Borrador', 'Borrador')], default='No Publicado', max_length=30)),
                ('precio', models.IntegerField(verbose_name='Precio AR$')),
                ('cantidad_disponible', models.DateField(verbose_name='Unidades Disponibles')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='producto/%Y/%m/%d')),
            ],
        ),
    ]
