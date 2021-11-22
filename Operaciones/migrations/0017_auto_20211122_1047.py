# Generated by Django 3.2.9 on 2021-11-22 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operaciones', '0016_alter_orden_fotos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='representante',
        ),
        migrations.AddField(
            model_name='persona',
            name='empresa',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicios',
            name='tipo_servicio',
            field=models.TextField(choices=[('buque', 'Buques'), ('contenedor', 'Contenedores')]),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='medio',
            field=models.TextField(choices=[('buque', 'Buques'), ('contenedor', 'Contenedores')], default='Buques'),
        ),
    ]
