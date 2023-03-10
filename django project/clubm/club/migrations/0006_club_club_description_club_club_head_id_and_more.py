# Generated by Django 4.0.8 on 2022-12-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_description',
            field=models.CharField(default=None, max_length=4000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='club_head_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='club_img',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='club_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
