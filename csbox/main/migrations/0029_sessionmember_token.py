# Generated by Django 4.1.7 on 2023-06-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_sessionmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionmember',
            name='token',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
