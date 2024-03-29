# Generated by Django 3.2.9 on 2021-11-11 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operaciones', '0008_auto_20211111_1330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buque',
            options={'verbose_name': 'Buque', 'verbose_name_plural': 'Buques'},
        ),
        migrations.AddField(
            model_name='servicios',
            name='tipo_servicio',
            field=models.TextField(choices=[('Buques', 'Buques'), ('Contenedores', 'Contenedores')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='aprobada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_buque',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.buque', verbose_name='Buque'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='id_contendor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.contenedor', verbose_name='Contenedor'),
        ),
    ]
