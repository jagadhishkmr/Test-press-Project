# Generated by Django 3.2.5 on 2021-07-08 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_questions_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choices_text',
            new_name='choice_text',
        ),
    ]
