# Generated by Django 2.2.4 on 2019-10-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191021_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=500),
        ),
    ]
