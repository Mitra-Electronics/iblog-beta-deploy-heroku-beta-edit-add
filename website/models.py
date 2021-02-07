from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import uuid


# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    blog_title = models.CharField(max_length=255, verbose_name='Put a title')
    slug = models.SlugField(max_length=255, unique=True)
    blog_content = RichTextField(max_length=10000, verbose_name='Put the description', blank=False, null=False)
    #blog_content = models.CharField()
    thumbnail = models.URLField(blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title

    def save(self):
        self.slug = slugify(self.blog_title + '-' + str(uuid.uuid4()))
        super(Blog, self).save()


class Comment(models.Model):
    video = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date', ]

    def __str__(self):
        return self.comment
