# Generated by Django 4.1.7 on 2023-05-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_postdb_uploadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdb',
            name='is_announcement',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
