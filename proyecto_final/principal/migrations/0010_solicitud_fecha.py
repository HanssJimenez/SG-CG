# Generated by Django 3.2.16 on 2022-10-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_rename_fnaci_colaborador_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
