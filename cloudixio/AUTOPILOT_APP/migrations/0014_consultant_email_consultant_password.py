# Generated by Django 4.0.4 on 2022-05-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOPILOT_APP', '0013_alter_timesheet_annee'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='consultant',
            name='password',
            field=models.CharField(default=1234, max_length=100),
            preserve_default=False,
        ),
    ]
