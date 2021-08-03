from django.db import models

# Create your models here.

class user_register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    facebook_name = models.CharField(max_length=100)
    facebook_email = models.CharField(max_length=100)
    facebook_password = models.CharField(max_length=50)
    facebook_link = models.CharField(max_length=200)

class user_post(models.Model):
    fb_username = models.CharField(max_length=100)
    post = models.JSONField(null=True)
    comment = models.JSONField(null=True)
    user_score = models.IntegerField(null=True)
    friend_score = models.JSONField(null=True)
