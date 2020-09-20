# Generated by Django 3.1 on 2020-09-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before_ranking', models.IntegerField(default=10000)),
                ('after_ranking', models.IntegerField(default=10000)),
            ],
        ),
        migrations.CreateModel(
            name='fantasy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before_ranking', models.IntegerField(default=10000)),
                ('after_ranking', models.IntegerField(default=10000)),
            ],
        ),
        migrations.CreateModel(
            name='romance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before_ranking', models.IntegerField(default=10000)),
                ('after_ranking', models.IntegerField(default=10000)),
            ],
        ),
    ]