# Generated by Django 4.0.4 on 2022-05-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOPILOT_APP', '0017_alter_mission_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionsType',
            fields=[
                ('idMissionSheet', models.BigAutoField(primary_key=True, serialize=False)),
                ('titre', models.TextField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'missionsType',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='mission',
            table='missions',
        ),
    ]
