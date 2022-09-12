# Generated by Django 4.0.4 on 2022-09-11 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_newregister'),
        ('foodservice', '0014_alter_product_brand_alter_product_measure_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='default.company')),
                ('company_worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='default.companyworker')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foodservice.product')),
            ],
            options={
                'verbose_name': 'Venda Items',
                'verbose_name_plural': 'Vendas Items',
                'ordering': ('company', 'product'),
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='default.company')),
                ('company_worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='default.companyworker')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
                'ordering': ('company', 'id'),
            },
        ),
    ]