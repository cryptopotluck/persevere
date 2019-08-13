# Generated by Django 2.2.3 on 2019-08-12 08:59

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190811_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=stdimage.models.StdImageField(blank=True, default='profile/default/default_img.png', upload_to='profile/%Y/%m/%d/'),
        ),
    ]