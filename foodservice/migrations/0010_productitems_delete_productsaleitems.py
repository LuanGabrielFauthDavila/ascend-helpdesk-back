# Generated by Django 4.0.4 on 2022-09-10 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_newregister'),
        ('foodservice', '0009_delete_productitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='default.company')),
                ('company_worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='default.companyworker')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foodservice.product')),
            ],
            options={
                'verbose_name': 'Produto Item',
                'verbose_name_plural': 'Produto Items',
                'ordering': ('product',),
            },
        ),
        migrations.DeleteModel(
            name='ProductSaleItems',
        ),
    ]