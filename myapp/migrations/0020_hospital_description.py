# Generated by Django 3.2.2 on 2021-06-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_hospital_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
