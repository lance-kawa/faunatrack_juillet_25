# Generated by Django 5.0.3 on 2025-07-08 07:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lattitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('at_risk', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Species',
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.CreateModel(
            name='FaunatrackUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='faunatrack_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'FaunatrackUser',
                'verbose_name_plural': 'FaunatrackUsers',
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_observation', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=1)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='observations', to='faunatrack.location')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='observations', to='faunatrack.project')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='observations', to='faunatrack.species')),
            ],
            options={
                'verbose_name': 'Observation',
                'verbose_name_plural': 'Observations',
            },
        ),
        migrations.CreateModel(
            name='ObservationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('observation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='faunatrack.observation')),
            ],
            options={
                'verbose_name': 'ObservationImage',
                'verbose_name_plural': 'ObservationImages',
            },
        ),
        migrations.CreateModel(
            name='ProjectUserAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('roles', models.CharField(choices=[('admin', 'Admin'), ('spectator', 'Spectator'), ('contributor', 'Contributor')], default='contributor', max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='faunatrack.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_access', to='faunatrack.faunatrackuser')),
            ],
            options={
                'verbose_name': 'ProjectUserAccess',
                'verbose_name_plural': 'ProjectUserAccesses',
            },
        ),
    ]
