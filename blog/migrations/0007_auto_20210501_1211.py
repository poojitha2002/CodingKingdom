# Generated by Django 3.1.5 on 2021-05-01 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210501_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(default='as', max_length=200)),
                ('file', models.FileField(default='d.pdf', upload_to='')),
                ('type', models.CharField(default='asdf', max_length=300)),
                ('content', models.TextField(default='Content to be displayed')),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),

        migrations.AddField(
            model_name='courses',
            name='id',
            field=models.AutoField(auto_created=True, default=datetime.date, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]