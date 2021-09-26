# Generated by Django 3.2.7 on 2021-09-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_finder', '0004_alter_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='current_proj',
            field=models.ManyToManyField(to='team_finder.Project'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills',
            field=models.ManyToManyField(to='team_finder.Skill'),
        ),
    ]