# Generated by Django 3.2.25 on 2024-03-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
            ],
        ),
    ]
