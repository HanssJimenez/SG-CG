# Generated by Django 3.2.16 on 2022-10-14 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0012_auto_20221013_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='principal.cliente', verbose_name='Clientes existentes'),
        ),
    ]
