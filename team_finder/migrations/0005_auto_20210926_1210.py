# Generated by Django 3.2.7 on 2021-09-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_finder', '0004_alter_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(to='team_finder.Team'),
        ),
    ]