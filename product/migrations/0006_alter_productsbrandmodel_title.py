# Generated by Django 4.0.6 on 2022-08-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productscartmodel_total_productsordermodel_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsbrandmodel',
            name='title',
            field=models.CharField(max_length=55, unique=True),
        ),
    ]
