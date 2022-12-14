# Generated by Django 3.2.16 on 2022-10-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0014_alter_inventario_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='monto',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numtel',
            field=models.CharField(max_length=9, verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='numero_de_telefono',
            field=models.CharField(max_length=100, verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='pago',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
