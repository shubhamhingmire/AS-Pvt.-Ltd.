# Generated by Django 3.2.23 on 2024-02-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mnumber',
            field=models.CharField(max_length=10),
        ),
    ]
