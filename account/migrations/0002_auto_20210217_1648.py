# Generated by Django 3.1.2 on 2021-02-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/images/unisex_avatar.jpg', upload_to='display_pictures'),
        ),
    ]
