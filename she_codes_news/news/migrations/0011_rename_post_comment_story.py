# Generated by Django 4.2.2 on 2023-12-13 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_comment_modified_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='story',
        ),
    ]