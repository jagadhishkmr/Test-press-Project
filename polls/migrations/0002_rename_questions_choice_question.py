# Generated by Django 3.2.5 on 2021-07-08 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='questions',
            new_name='question',
        ),
    ]
