# Generated by Django 4.2.2 on 2023-12-05 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_bio_customuser_bio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_photo',
            new_name='profile_photo',
        ),
    ]
