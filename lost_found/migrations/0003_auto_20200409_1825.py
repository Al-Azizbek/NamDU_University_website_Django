# Generated by Django 2.2.7 on 2020-04-09 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lost_found', '0002_auto_20200409_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lost_found',
            old_name='slug1',
            new_name='slug_path',
        ),
    ]