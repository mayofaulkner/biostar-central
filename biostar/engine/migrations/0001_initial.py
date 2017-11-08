# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 15:57
from __future__ import unicode_literals

import biostar.engine.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=32, unique=True)),
                ('sticky', models.BooleanField(default=True)),
                ('name', models.CharField(default='No name', max_length=256)),
                ('summary', models.TextField(default='No summary.')),
                ('text', models.TextField(default='No description.', max_length=10000)),
                ('html', models.TextField(default='html')),
                ('auth', models.IntegerField(choices=[(1, 'Authorized'), (2, 'Under Review')], default=2)),
                ('state', models.IntegerField(choices=[(1, 'Active'), (2, 'Deleted')], default=1)),
                ('json_text', models.TextField(default='{}', max_length=10000)),
                ('template', models.TextField(default='makefile')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default=None, max_length=1024, upload_to=biostar.engine.models.image_path)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name', max_length=256)),
                ('summary', models.TextField(default='no summary')),
                ('image', models.ImageField(blank=True, default=None, max_length=1024, upload_to=biostar.engine.models.image_path)),
                ('sticky', models.BooleanField(default=True)),
                ('text', models.TextField(default='no description', max_length=10000)),
                ('html', models.TextField(default='html')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file_type', models.IntegerField(choices=[(1, 'File'), (2, 'Collection')], default=1)),
                ('data_type', models.IntegerField(default=0)),
                ('size', models.IntegerField(default=0)),
                ('state', models.IntegerField(choices=[(1, 'Pending'), (2, 'Ready'), (3, 'Error'), (4, 'Deleted')], default=1)),
                ('file', models.FileField(max_length=1024, null=True, upload_to=biostar.engine.models.data_upload_path)),
                ('link', models.FilePathField(max_length=1024, null=True)),
                ('uid', models.CharField(max_length=32)),
                ('valid', models.BooleanField(default=True)),
                ('data_dir', models.FilePathField(default='', max_length=1024)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name', max_length=256)),
                ('summary', models.TextField(default='no summary')),
                ('image', models.ImageField(blank=True, default=None, max_length=1024, upload_to=biostar.engine.models.image_path)),
                ('text', models.TextField(default='no description', max_length=10000)),
                ('html', models.TextField(default='html')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('json_text', models.TextField(default='commands')),
                ('uid', models.CharField(max_length=32)),
                ('template', models.TextField(default='makefile')),
                ('security', models.IntegerField(choices=[(1, 'Authorized'), (2, 'Under Review')], default=2)),
                ('script', models.TextField(default='')),
                ('stdout_log', models.TextField(default='', max_length=200000)),
                ('stderr_log', models.TextField(default='', max_length=200000)),
                ('valid', models.BooleanField(default=True)),
                ('state', models.IntegerField(choices=[(1, 'Queued'), (2, 'Running'), (3, 'Completed'), (4, 'Error'), (5, 'Deleted')], default=1)),
                ('path', models.FilePathField(default='')),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Analysis')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sticky', models.BooleanField(default=True)),
                ('privacy', models.IntegerField(choices=[(3, 'Private'), (2, 'Shareable Link'), (1, 'Public')], default=2)),
                ('state', models.IntegerField(choices=[(1, 'Active'), (2, 'Deleted')], default=1)),
                ('image', models.ImageField(blank=True, default=None, max_length=1024, upload_to=biostar.engine.models.image_path)),
                ('name', models.CharField(default='no name', max_length=256)),
                ('summary', models.TextField(default='no summary', max_length=10000)),
                ('text', models.TextField(default='no description', max_length=10000)),
                ('html', models.TextField(default='html', max_length=200000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('uid', models.CharField(max_length=32, unique=True)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Project'),
        ),
        migrations.AddField(
            model_name='data',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Project'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Project'),
        ),
    ]
