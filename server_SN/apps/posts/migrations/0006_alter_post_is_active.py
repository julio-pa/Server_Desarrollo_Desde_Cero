# Generated by Django 4.2.6 on 2023-11-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
