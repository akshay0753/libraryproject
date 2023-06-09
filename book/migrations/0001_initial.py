# Generated by Django 4.0.5 on 2022-11-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('is_published', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
