# Generated by Django 2.0.12 on 2020-01-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200103_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='isbn',
            field=models.CharField(default=0, max_length=500),
        ),
    ]
