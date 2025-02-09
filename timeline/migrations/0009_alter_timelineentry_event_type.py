# Generated by Django 5.1.2 on 2024-11-03 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timeline", "0008_alter_timelineentry_event_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timelineentry",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("add", "Added/Created an Object"),
                    ("del", "Removed an Object"),
                    ("upd", "Updated/Edited an Object"),
                    ("sbg", "Asset Started Search"),
                    ("snd", "Asset Finished Search"),
                    ("usr", "User defined Event"),
                    ("oad", "Organization added to mission"),
                    ("oup", "Organization updated"),
                    ("orm", "Organization removed from mission"),
                    ("uad", "User added to mission"),
                    ("uup", "User updated"),
                    ("aad", "Asset added to mission"),
                    ("arm", "Asset removed from mission"),
                    ("ipc", "Image priority changed"),
                    ("que", "Search was Queued or Dequeued"),
                    ("mas", "Mission Asset Status"),
                    ("acs", "Asset Command Sent"),
                    ("acr", "Asset Command Response"),
                ],
                max_length=3,
            ),
        ),
    ]
