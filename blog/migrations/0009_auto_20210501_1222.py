# Generated by Django 3.1.5 on 2021-05-01 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_courses_coursecode'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Materials',
            new_name='Files',
        ),
    ]
