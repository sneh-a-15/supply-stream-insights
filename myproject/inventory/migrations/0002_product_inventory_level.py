# Generated by Django 5.0.4 on 2024-08-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory_level',
            field=models.IntegerField(default=0),
        ),
    ]
