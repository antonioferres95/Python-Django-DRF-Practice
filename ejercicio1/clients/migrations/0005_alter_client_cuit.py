# Generated by Django 4.0 on 2022-01-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_client_cuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cuit',
            field=models.PositiveBigIntegerField(),
        ),
    ]