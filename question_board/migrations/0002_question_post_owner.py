# Generated by Django 2.2.3 on 2019-08-03 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('question_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='post_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile'),
        ),
    ]
