# Generated by Django 5.0.4 on 2024-04-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety_resources', '0003_safetyresource_card_img_safetyresource_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safetyresource',
            name='card_img',
            field=models.ImageField(blank=True, default='static/images/SR3.png', null=True, upload_to='static/images/'),
        ),
    ]
