# Generated by Django 2.2.4 on 2020-02-29 05:58

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20200229_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True, null=True),
        ),
    ]