# Generated by Django 3.1 on 2021-06-06 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
        ('rebase_app', '0002_texto_text_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Texto',
            new_name='Text',
        ),
    ]
