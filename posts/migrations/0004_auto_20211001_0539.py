# Generated by Django 3.0.2 on 2021-10-01 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211001_0534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Category',
            new_name='category',
        ),
    ]