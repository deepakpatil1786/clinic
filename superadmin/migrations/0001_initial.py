# Generated by Django 4.0.1 on 2022-04-28 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('patient', 'Patient')], max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('clinic', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], default=None, null=True)),
                ('speciality', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('Address', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('profile', models.FileField(default='profile.html', upload_to='profile')),
            ],
        ),
    ]
