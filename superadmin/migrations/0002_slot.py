# Generated by Django 4.0.4 on 2022-05-04 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SLOT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.IntegerField(choices=[(1, '10:00 -11:00'), (2, '11:00 - 12:00'), (3, '12:00 - 1:00'), (4, '1:00 - 2:00'), (5, '2:00 - 3:00'), (6, '3:00 - 4:00'), (7, '4:00 - 5:00')])),
                ('weekslot', models.IntegerField(choices=[(1, 'mon'), (2, 'tue'), (3, 'wed'), (4, 'thu'), (5, 'fri'), (6, 'sat'), (7, 'sun')])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.user')),
            ],
        ),
    ]
