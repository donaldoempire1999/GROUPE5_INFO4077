# Generated by Django 3.1.1 on 2020-12-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_api_rest', '0003_auto_20201205_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hasscreened',
            name='region',
            field=models.CharField(choices=[('North_West', 'North_West'), ('South', 'South'), ('South_West', 'South_West'), ('Centre', 'Centre'), ('North', 'North'), ('West', 'West'), ('Extreme_North', 'Extreme_North'), ('Littoral', 'Littoral'), ('East', 'East'), ('Adamaoua', 'Adamaoua')], max_length=13),
        ),
    ]
