# Generated by Django 3.0.2 on 2021-09-28 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Category',
            new_name='category',
        ),
    ]
