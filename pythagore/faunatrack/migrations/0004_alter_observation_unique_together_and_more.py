# Generated by Django 5.2.4 on 2025-07-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faunatrack', '0003_rename_projet_observation_project_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='observation',
            unique_together={('date_observation', 'species', 'location')},
        ),
        migrations.AddIndex(
            model_name='observation',
            index=models.Index(fields=['species'], name='observation_index'),
        ),
    ]
