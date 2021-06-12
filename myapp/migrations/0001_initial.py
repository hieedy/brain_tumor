# Generated by Django 3.2.2 on 2021-05-15 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clinics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('full_address', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('no_of_beds', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='labs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('full_address', models.CharField(max_length=100)),
                ('start_time', models.IntegerField()),
                ('closing_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Message', models.CharField(max_length=100)),
                ('Attachement', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('bloodgroup', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('contactno', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('experience_yrs', models.FloatField(max_length=10)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('specialization', models.CharField(max_length=30)),
                ('clinic_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.clinics')),
                ('hospital_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('status', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.diseases')),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.doctor')),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
    ]
