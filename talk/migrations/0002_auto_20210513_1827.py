# Generated by Django 2.1.5 on 2021-05-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
