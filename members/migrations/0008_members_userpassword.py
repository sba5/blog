# Generated by Django 3.1.5 on 2021-01-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20210126_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='userpassword',
            field=models.CharField(default='', max_length=16, null=True, verbose_name='user_password'),
        ),
    ]
