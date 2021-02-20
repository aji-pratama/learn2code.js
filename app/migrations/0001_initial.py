# Generated by Django 3.1.1 on 2021-02-20 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('instruction', models.TextField()),
                ('initial_code', models.TextField(blank=True)),
                ('display_order', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='ExpectedAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('expected_code', models.TextField(blank=True)),
                ('expected_result', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
