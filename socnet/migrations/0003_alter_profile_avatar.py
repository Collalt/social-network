# Generated by Django 4.0.5 on 2022-06-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socnet', '0002_profile_avatar_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static/images/default.jpg', upload_to='static/images'),
        ),
    ]
