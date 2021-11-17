# Generated by Django 3.2.9 on 2021-11-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operaciones', '0007_auto_20211111_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=15)),
                ('catidad', models.DecimalField(decimal_places=2, max_digits=11)),
                ('producto', models.TextField(max_length=15)),
                ('bl', models.TextField(max_length=20)),
                ('manifiesto', models.TextField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='contenedor',
            name='estiba',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipo_solicitud',
            field=models.TextField(choices=[('Origen', 'Origen'), ('Destino', 'Destino')], null=True),
        ),
    ]