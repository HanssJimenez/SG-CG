# Generated by Django 3.2.16 on 2022-10-17 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0020_alter_inventario_medida'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobanteCompra',
            fields=[
                ('nocomp', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=12, unique=True)),
                ('dirreccion', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('gestion', models.CharField(max_length=15, unique=True)),
                ('borrado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('preciouni', models.IntegerField(default=1)),
                ('totalprecio', models.IntegerField(default=1)),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidadcompra', to='principal.inventario')),
                ('nocomp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comprobantecomprano', to='principal.comprobantecompra')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleComprobanteCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(blank=True, max_length=50, null=True)),
                ('nocomp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detallecomprobantecompra', to='principal.comprobantecompra')),
            ],
        ),
        migrations.AddField(
            model_name='comprobantecompra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proveedorcompra', to='principal.proveedor'),
        ),
    ]