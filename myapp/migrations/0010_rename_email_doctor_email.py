# Generated by Django 3.2.2 on 2021-05-23 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_email_doctor_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='email',
            new_name='Email',
        ),
    ]