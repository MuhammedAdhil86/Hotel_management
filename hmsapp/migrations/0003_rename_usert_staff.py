# Generated by Django 5.0.1 on 2024-02-07 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0002_usert_delete_usertable'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usert',
            new_name='staff',
        ),
    ]
