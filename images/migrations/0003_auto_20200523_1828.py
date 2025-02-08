# Generated by Django 3.0.6 on 2020-05-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_update_field_names'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='geoimage',
            name='images_geoi_mission_520eee_idx',
        ),
        migrations.AddIndex(
            model_name='geoimage',
            index=models.Index(fields=['mission', 'deleted_at', 'replaced_at', 'created_at'], name='images_geoi_mission_79768c_idx'),
        ),
    ]
