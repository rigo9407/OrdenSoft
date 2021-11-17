# Generated by Django 3.2.9 on 2021-11-15 20:33

from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('Operaciones', '0009_auto_20211111_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='telefono',
        ),
        migrations.AddField(
            model_name='persona',
            name='ci',
            field=models.IntegerField(default=94071731305, verbose_name=django.db.models.fields.related.ForeignKey),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_orden', models.TextField(verbose_name=django.db.models.fields.related.ForeignKey)),
                ('fotos', models.ImageField(upload_to='')),
                ('solicitud', models.ManyToManyField(to='Operaciones.Solicitud')),
            ],
        ),
    ]