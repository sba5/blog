# Generated by Django 3.1.5 on 2021-01-26 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20210126_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='user_address',
            new_name='useraddress',
        ),
    ]