# Generated by Django 3.2.7 on 2021-10-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
