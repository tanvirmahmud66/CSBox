# Generated by Django 4.1.7 on 2023-06-20 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_commentdb_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile_pic.webp', null=True, upload_to='teacher_profilePic/'),
        ),
    ]
