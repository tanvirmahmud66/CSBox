# Generated by Django 4.1.7 on 2023-05-18 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_semestername_alter_teacherid_options_studentid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section',
            field=models.CharField(max_length=1),
        ),
    ]
