# Generated by Django 5.1 on 2024-09-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_userproduct_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='category',
            field=models.CharField(choices=[('Clothing & Apparel', 'Clothing & Apparel'), ('Electronics & Gadgets', 'Electronics & Gadgets'), ('Food Items', 'Food Items'), ('Home & Kitchen', 'Home & Kitchen'), ('Books & Media', 'Books & Media'), ('Sports & Outdoor', 'Sports & Outdoor')], max_length=50),
        ),
    ]
