# Generated by Django 4.0.2 on 2022-04-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0006_quizcodefb_quizdatafb'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBAttemptStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('rollno', models.CharField(max_length=200, null=True)),
                ('quizcode', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]