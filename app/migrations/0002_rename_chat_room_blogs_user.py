# Generated by Django 4.2.1 on 2023-12-28 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='chat_room',
            new_name='user',
        ),
    ]
