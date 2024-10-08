# Generated by Django 5.0.6 on 2024-08-28 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsingle',
            name='comment',
            field=models.PositiveIntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.blog')),
            ],
        ),
    ]
