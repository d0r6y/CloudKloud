# Generated by Django 3.1.3 on 2020-11-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baguni', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='tag',
            field=models.TextField(blank=True),
        ),
    ]
