# Generated by Django 3.2.23 on 2024-03-02 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20240302_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='resume',
        ),
    ]
