# Generated by Django 4.1.12 on 2024-04-01 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profCust', '0003_alter_userprofile_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
    ]
