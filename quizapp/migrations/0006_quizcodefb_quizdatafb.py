# Generated by Django 4.0.2 on 2022-04-06 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_studentmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCodeFB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200, null=True)),
                ('quizcode', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizDataFB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('correctans', models.CharField(max_length=200, null=True)),
                ('qquizcode', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
