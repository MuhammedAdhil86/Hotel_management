# Generated by Django 5.0.1 on 2024-02-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0003_rename_usert_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]