# Generated by Django 3.2.23 on 2024-03-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_apply_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experiance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(max_length=50),
        ),
    ]