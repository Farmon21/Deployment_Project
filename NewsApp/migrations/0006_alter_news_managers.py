# Generated by Django 4.1.7 on 2023-03-31 12:05

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0005_alter_comment_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='news',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
