# Generated by Django 2.2.7 on 2020-04-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost_found', '0003_auto_20200409_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost_found',
            name='slug_path',
            field=models.SlugField(unique='True'),
        ),
    ]
