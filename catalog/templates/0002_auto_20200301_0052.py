# Generated by Django 2.2.4 on 2020-03-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Tags',
        ),
        migrations.AlterField(
            model_name='games',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
