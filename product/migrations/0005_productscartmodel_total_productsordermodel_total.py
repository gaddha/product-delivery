# Generated by Django 4.0.6 on 2022-08-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_produtscategorymodel_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productscartmodel',
            name='total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productsordermodel',
            name='total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
