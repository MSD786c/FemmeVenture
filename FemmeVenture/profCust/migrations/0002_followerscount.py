# Generated by Django 4.1.12 on 2024-03-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profCust', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
