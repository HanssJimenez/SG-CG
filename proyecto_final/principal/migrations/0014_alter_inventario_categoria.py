# Generated by Django 3.2.16 on 2022-10-15 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_alter_solicitud_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='principal.categorias'),
        ),
    ]
