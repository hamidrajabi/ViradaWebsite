# Generated by Django 3.2.7 on 2021-10-01 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virada', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='name',
            new_name='title',
        ),
    ]