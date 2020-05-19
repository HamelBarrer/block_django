# Generated by Django 3.0.6 on 2020-05-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
