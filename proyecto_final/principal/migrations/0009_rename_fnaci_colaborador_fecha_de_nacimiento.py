# Generated by Django 3.2.16 on 2022-10-08 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_solicitud_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colaborador',
            old_name='fnaci',
            new_name='fecha_de_nacimiento',
        ),
    ]