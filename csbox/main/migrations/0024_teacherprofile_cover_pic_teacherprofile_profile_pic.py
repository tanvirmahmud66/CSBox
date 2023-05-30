# Generated by Django 4.1.7 on 2023-05-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_teacherprofile_address_teacherprofile_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_coverPic/'),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_profilePic/'),
        ),
    ]
