# Generated by Django 4.0.6 on 2022-08-05 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_productscartmodel_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsattributemodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productsAttributeModel_category', to='product.produtscategorymodel'),
        ),
        migrations.AlterField(
            model_name='productsattributemodel',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productsattributemodel',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productsproductmodel',
            name='title',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='produtscategorymodel',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produtsCategoryModel_product', to='product.productsproductmodel'),
        ),
    ]
