# Generated by Django 4.0.5 on 2022-06-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socnet', '0007_alter_profile_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='static/images'),
        ),
    ]
