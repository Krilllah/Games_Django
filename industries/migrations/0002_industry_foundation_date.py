# Generated by Django 4.0.2 on 2022-05-25 10:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('industries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='foundation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
