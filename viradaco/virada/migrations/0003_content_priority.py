# Generated by Django 3.2.7 on 2021-10-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virada', '0002_rename_name_content_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='priority',
            field=models.IntegerField(null=True),
        ),
    ]
