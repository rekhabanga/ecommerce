# Generated by Django 2.2.4 on 2019-10-21 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='pu',
        ),
    ]
