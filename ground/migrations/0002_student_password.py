# Generated by Django 5.1.2 on 2024-11-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ground', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
