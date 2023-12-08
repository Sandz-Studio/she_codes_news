# Generated by Django 4.2.2 on 2023-12-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsstory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='category',
            field=models.CharField(choices=[('Animals', 'Animals'), ('Travel', 'Travel'), ('Food', 'Food'), ('World', 'World'), ('Sport', 'Sport'), ('Lifestyle', 'Lifestyle'), ('Entertainment', 'Entertainment'), ('Technology', 'Technology')], default='', max_length=15),
        ),
    ]
