# Generated by Django 3.2.2 on 2021-06-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_chat_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='specialization',
            field=models.CharField(max_length=30),
        ),
    ]
