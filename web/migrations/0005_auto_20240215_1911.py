# Generated by Django 3.2.23 on 2024-02-15 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_founder_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='founder',
            old_name='description',
            new_name='fdescription',
        ),
        migrations.RenameField(
            model_name='founder',
            old_name='image',
            new_name='fimage',
        ),
        migrations.RenameField(
            model_name='founder',
            old_name='name',
            new_name='fname',
        ),
    ]
