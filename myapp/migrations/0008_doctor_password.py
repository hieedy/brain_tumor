# Generated by Django 3.2.2 on 2021-05-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_helpandsupport_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
