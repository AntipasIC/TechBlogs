# Generated by Django 3.0.2 on 2021-10-01 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210928_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='Category',
        ),
    ]
