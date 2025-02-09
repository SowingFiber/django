from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#Post class Start
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

#Post Class End

#Basic Tweet Class Start
class Tweet(models.Model):
    tweet = models.TextField(max_length=150)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tweets')
    publish = models.DateTimeField(default = timezone.now)
    retweets = models.IntegerField(name='retweet')
    likes = models.IntegerField(name='likes')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.tweet
#Basic Tweet Class End

