# Generated by Django 4.1.dev20211213175307 on 2022-02-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('accessory_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='guitar',
            name='year',
        ),
        migrations.AddField(
            model_name='guitar',
            name='accessories',
            field=models.ManyToManyField(to='main_app.Accessory'),
        ),
    ]
