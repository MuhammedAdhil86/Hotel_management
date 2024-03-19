# Generated by Django 5.0.1 on 2024-02-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0005_remove_staff_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, null=True)),
                ('lastname', models.CharField(max_length=30, null=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('password', models.CharField(max_length=100, null=True)),
                ('confirm_password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
