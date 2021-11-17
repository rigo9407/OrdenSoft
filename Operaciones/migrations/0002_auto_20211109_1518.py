# Generated by Django 3.2.9 on 2021-11-09 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.TextField(max_length=10)),
                ('dimenciones', models.TextField(choices=[('20 pies', '20 pies'), ('40 pies', '40 pies')])),
                ('cantidad', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=9)),
                ('embalaje', models.TextField(max_length=50)),
                ('marca', models.TextField(max_length=15)),
                ('mercancia', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=10)),
                ('apellidos', models.TextField(max_length=20)),
                ('cargo', models.TextField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='Contrato',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='Crea_Solicitud',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='Fecha_Inspeccion',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='Fecha_Solicitud',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='Mercancia',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='contrato',
            field=models.TextField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='fecha_Inspeccion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='fecha_Solicitud',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.cliente'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='mercancia',
            field=models.TextField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_firma',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero_contrato',
            field=models.TextField(max_length=6),
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Operaciones.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Receptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Operaciones.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Operaciones.empresa')),
            ],
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_comprador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.comprador'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_contendor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.contenedor'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_ervicios',
            field=models.ManyToManyField(blank=True, null=True, to='Operaciones.Servicios'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_receptor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.receptor'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.trabajador'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Operaciones.vendedor'),
        ),
    ]