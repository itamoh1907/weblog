# Generated by Django 4.2.17 on 2024-12-29 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_category_alter_article_pub_date_alter_article_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 29, 12, 59, 28, 49453, tzinfo=datetime.timezone.utc)),
        ),
    ]
