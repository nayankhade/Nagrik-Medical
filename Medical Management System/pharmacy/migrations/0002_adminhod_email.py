# Generated by Django 4.1.7 on 2023-03-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminhod',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
