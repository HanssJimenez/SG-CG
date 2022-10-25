# Generated by Django 3.2.16 on 2022-10-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0024_auto_20221021_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='colaborador',
            options={'verbose_name': 'Colaborador', 'verbose_name_plural': 'Colaboradores'},
        ),
        migrations.AlterModelOptions(
            name='comprobantecompra',
            options={'verbose_name': 'Comprobante de compra', 'verbose_name_plural': 'Comprobantes de compras'},
        ),
        migrations.AlterModelOptions(
            name='comprobanteservicio',
            options={'verbose_name': 'Comprobante de servicio', 'verbose_name_plural': 'Comprobantes de servicios'},
        ),
        migrations.AlterModelOptions(
            name='detallecomprobantecompra',
            options={'verbose_name': 'Detalle de compra', 'verbose_name_plural': 'Detalles de compras'},
        ),
        migrations.AlterModelOptions(
            name='detallecomprobanteservicio',
            options={'verbose_name': 'Detalle de servicio', 'verbose_name_plural': 'Detalle de servicios'},
        ),
        migrations.AlterModelOptions(
            name='inventario',
            options={'verbose_name': 'Inventario', 'verbose_name_plural': 'Inventario'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='unidadcompra',
            options={'verbose_name': 'Unidad compra', 'verbose_name_plural': 'Unidades compradas'},
        ),
        migrations.AlterModelOptions(
            name='unidadvendida',
            options={'verbose_name': 'Unidad Vendida', 'verbose_name_plural': 'Unidades Vendidas'},
        ),
    ]
