# Generated by Django 3.2.6 on 2021-09-13 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20210910_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Image',
            field=models.ImageField(default='', upload_to='job/'),
            preserve_default=False,
        ),
    ]