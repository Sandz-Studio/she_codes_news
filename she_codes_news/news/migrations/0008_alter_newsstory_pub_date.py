# Generated by Django 4.2.2 on 2023-12-09 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_newsstory_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
