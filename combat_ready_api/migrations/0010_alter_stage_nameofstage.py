# Generated by Django 4.1.1 on 2022-09-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_ready_api', '0009_merge_0005_stage_nameofstage_0008_matches_matchname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='nameOfStage',
            field=models.CharField(default='0000000', max_length=100),
        ),
    ]
