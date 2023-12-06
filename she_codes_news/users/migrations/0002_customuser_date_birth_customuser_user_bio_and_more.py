# Generated by Django 4.2.2 on 2023-12-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_birth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_bio',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
