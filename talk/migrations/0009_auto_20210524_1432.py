# Generated by Django 2.1.5 on 2021-05-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0008_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='conatct_us',
            new_name='conatct_no',
        ),
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('unlike', 'unlike'), ('like', 'like')], default='like', max_length=10),
        ),
    ]