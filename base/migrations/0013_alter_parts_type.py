# Generated by Django 3.2.21 on 2023-10-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_parts_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='type',
            field=models.CharField(choices=[('CPU', 'CPU'), ('GPU', 'GPU')], max_length=10),
        ),
    ]