# Generated by Django 3.1.5 on 2021-05-01 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210501_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='courseCode',
        ),
    ]
