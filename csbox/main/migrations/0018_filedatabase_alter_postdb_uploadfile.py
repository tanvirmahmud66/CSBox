# Generated by Django 4.1.7 on 2023-05-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_semester_options_postdb_commentdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadFile', models.FileField(blank=True, null=True, upload_to='uploaded_files/')),
                ('sessionId', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Files Database',
                'verbose_name_plural': 'Files Database',
            },
        ),
        migrations.AlterField(
            model_name='postdb',
            name='uploadFile',
            field=models.FileField(blank=True, null=True, upload_to='uploaded_files/'),
        ),
    ]
