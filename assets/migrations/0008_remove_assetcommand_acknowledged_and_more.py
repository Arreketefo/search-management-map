# Generated by Django 5.0.6 on 2024-06-12 09:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assets", "0007_asset_icon_assettype_icon"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="assetcommand",
            name="acknowledged",
        ),
        migrations.AddField(
            model_name="assetcommand",
            name="responded_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assetcommand",
            name="responded_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="responder%(app_label)s_%(class)s_related",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="assetcommand",
            name="response_message",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assetcommand",
            name="response_type",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="assetcommand",
            name="issued_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_by%(app_label)s_%(class)s_related",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
