# Generated by Django 4.1.7 on 2023-06-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_sessionmember_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedatabase',
            name='uploadFile',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]