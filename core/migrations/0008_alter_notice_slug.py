# Generated by Django 5.2 on 2025-04-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_faculty_options_notice_image_alter_event_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
