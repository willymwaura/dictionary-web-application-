# Generated by Django 3.2.6 on 2021-10-04 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_search_feature_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
