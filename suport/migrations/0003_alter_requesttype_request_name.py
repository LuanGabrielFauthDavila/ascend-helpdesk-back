# Generated by Django 4.0.4 on 2022-09-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suport', '0002_alter_requesttype_request_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttype',
            name='request_name',
            field=models.CharField(max_length=25),
        ),
    ]
