# Generated by Django 5.1.6 on 2025-03-05 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
