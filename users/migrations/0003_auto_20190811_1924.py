# Generated by Django 2.2.3 on 2019-08-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190811_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile/default/default_img.png', upload_to='profile/%Y/%m/%d/'),
        ),
    ]
