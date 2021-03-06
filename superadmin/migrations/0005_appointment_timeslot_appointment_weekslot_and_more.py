# Generated by Django 4.0.4 on 2022-05-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0004_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='timeslot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='appointment',
            name='weekslot',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Completed'), (2, 'Absent'), (3, 'Cancel')], default=0),
        ),
    ]
