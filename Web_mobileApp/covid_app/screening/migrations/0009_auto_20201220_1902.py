# Generated by Django 3.1.4 on 2020-12-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screening', '0008_auto_20201218_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinetest',
            name='state',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='onlinetest',
            name='voice',
            field=models.FileField(null=True, upload_to='media/voices'),
        ),
        migrations.AlterField(
            model_name='hasscreened',
            name='region',
            field=models.CharField(choices=[('North_West', 'North_West'), ('North', 'North'), ('West', 'West'), ('Centre', 'Centre'), ('Extreme_North', 'Extreme_North'), ('Adamaoua', 'Adamaoua'), ('Littoral', 'Littoral'), ('East', 'East'), ('South_West', 'South_West'), ('South', 'South')], max_length=13),
        ),
    ]
