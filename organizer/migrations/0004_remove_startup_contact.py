# Generated by Django 4.1 on 2022-09-05 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0003_alter_newslink_slug_alter_startup_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='contact',
        ),
    ]
