# Generated by Django 4.1.1 on 2022-09-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_ready_api', '0009_merge_0005_stage_nameofstage_0008_matches_matchname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='durabilityP1',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='durabilityP2',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='imageP1',
            field=models.TextField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='intelligenceP1',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='intelligenceP2',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='powerP1',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='powerP2',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='speedP1',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='speedP2',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='strengthP1',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='matches',
            name='strengthP2',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='stage',
            name='nameOfStage',
            field=models.CharField(default='0000000', max_length=100),
        ),
    ]