# Generated by Django 3.1.5 on 2021-01-26 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20210126_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='useraddress',
            new_name='user_address',
        ),
    ]