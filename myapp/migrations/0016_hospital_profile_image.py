# Generated by Django 3.2.2 on 2021-06-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20210607_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
