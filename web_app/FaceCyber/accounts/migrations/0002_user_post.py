# Generated by Django 3.1.7 on 2021-03-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_username', models.CharField(max_length=100)),
                ('post', models.JSONField(null=True)),
                ('comment', models.JSONField(null=True)),
                ('user_score', models.IntegerField(null=True)),
                ('friend_score', models.JSONField(null=True)),
            ],
        ),
    ]
