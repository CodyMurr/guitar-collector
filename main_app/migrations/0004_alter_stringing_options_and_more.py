# Generated by Django 4.1.dev20211213175307 on 2022-02-09 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_stringing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stringing',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='stringing',
            old_name='date_changed',
            new_name='date',
        ),
    ]
