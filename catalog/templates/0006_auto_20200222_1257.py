# Generated by Django 2.2.4 on 2020-02-22 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200217_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='last_name',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='Tags',
        ),
    ]