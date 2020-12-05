# Generated by Django 3.1.1 on 2020-12-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_api_rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CitizenScreened',
            new_name='Citizen',
        ),
        migrations.AlterField(
            model_name='hasscreened',
            name='region',
            field=models.CharField(choices=[('Adamaoua', 'Adamaoua'), ('West', 'West'), ('Extreme_North', 'Extreme_North'), ('Centre', 'Centre'), ('South_West', 'South_West'), ('East', 'East'), ('South', 'South'), ('North', 'North'), ('Littoral', 'Littoral'), ('North_West', 'North_West')], max_length=13),
        ),
        migrations.AlterModelTable(
            name='citizen',
            table='citizens',
        ),
    ]
