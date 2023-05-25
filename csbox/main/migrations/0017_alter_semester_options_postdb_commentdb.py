# Generated by Django 4.1.7 on 2023-05-24 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0016_alter_semester_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['-year']},
        ),
        migrations.CreateModel(
            name='PostDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_announcement', models.BooleanField(default=False)),
                ('uploadFile', models.FileField(blank=True, null=True, upload_to='uploaded_files')),
                ('postBody', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sessiondata')),
            ],
            options={
                'verbose_name': 'Post DB',
                'verbose_name_plural': 'Post DB',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='CommentDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentBody', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postdb')),
            ],
            options={
                'verbose_name': 'Comment DB',
                'verbose_name_plural': 'Comment DB',
            },
        ),
    ]
