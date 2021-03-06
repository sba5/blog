# Generated by Django 3.1.5 on 2021-01-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=16, verbose_name='user_id')),
                ('userpassword', models.CharField(default='', max_length=16, null=True, verbose_name='user_password')),
                ('username', models.CharField(max_length=16, null=True, verbose_name='user_name')),
                ('usergender', models.CharField(default='', max_length=2, null=True, verbose_name='user_gender')),
                ('useremail', models.EmailField(max_length=128, verbose_name='user_email')),
                ('userphone', models.CharField(max_length=16, verbose_name='user_phone')),
                ('useraddress', models.CharField(default='', max_length=128, null=True, verbose_name='user_address')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='register_time')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='modify_time')),
            ],
            options={
                'verbose_name': 'World_Users',
                'verbose_name_plural': 'World Users',
                'db_table': 'world_users',
            },
        ),
    ]
