# Generated by Django 4.0.6 on 2022-08-05 14:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0007_paymentsmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='paymentsModel',
            new_name='productpaymentsModel',
        ),
    ]