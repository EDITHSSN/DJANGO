# Generated by Django 4.0.8 on 2022-12-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_comments_date_comments_title_alter_comments_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='threads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_id', models.IntegerField(default=0)),
                ('thread', models.CharField(default='', max_length=10000)),
                ('date', models.DateField(default='2019-01-01')),
            ],
        ),
    ]
