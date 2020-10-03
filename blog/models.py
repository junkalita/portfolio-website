from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify


# Create your models here.


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    category = models.ForeignKey('BlogCategory', on_delete=models.SET_NULL, null=True)
    blog_published = models.DateTimeField('date published', default=datetime.now)
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.blog_title:
            self.slug = slugify(self.blog_title)
        super(Blog,self).save(*args, **kwargs)


    def __str__(self):
        return self.blog_title


class BlogCategory(models.Model):
    blog_category = models.CharField(max_length=200)
    blog_summary = models.CharField(max_length=200)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.blog_category


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name='replies')
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}.{}'.format(self.blog.blog_title, str(self.user.username))
