# Generated by Django 4.1.7 on 2023-03-14 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_adminhod_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminhod',
            name='email',
        ),
    ]