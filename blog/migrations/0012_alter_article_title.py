# Generated by Django 4.2.17 on 2024-12-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(choices=[('A', 'پایتون'), ('B', 'جنگو'), ('C', 'جاوا')], max_length=200),
        ),
    ]
