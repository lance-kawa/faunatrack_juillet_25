# Generated by Django 5.2.4 on 2025-07-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faunatrack', '0005_remove_observation_observation_index_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
    ]
