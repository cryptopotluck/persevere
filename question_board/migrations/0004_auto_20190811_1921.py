# Generated by Django 2.2.3 on 2019-08-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_board', '0003_auto_20190803_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.CharField(choices=[('HTML', 'HTML'), ('Javascript', 'Javascript'), ('Node.js', 'Node.js'), ('React', 'React'), ('Python', 'Python'), ('Data Science', 'Data Science'), ('SQL', 'SQL'), ('Java', 'Java'), ('JQuery', 'JQuery'), ('css', 'css'), ('Sass', 'Sass')], default='HTML', max_length=50),
        ),
    ]
