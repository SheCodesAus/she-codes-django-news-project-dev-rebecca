# Generated by Django 4.0.1 on 2022-06-03 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsstory',
            name='image',
        ),
    ]
