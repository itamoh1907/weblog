# Generated by Django 4.2.17 on 2025-01-23 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_message_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 23, 6, 41, 12, 681115, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 23, 6, 41, 12, 679136, tzinfo=datetime.timezone.utc)),
        ),
    ]
