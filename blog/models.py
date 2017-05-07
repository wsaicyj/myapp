from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    # class Meta:   #根据时间倒序排列
    #     ordering = ('-timestamp',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


# class Person(models.Model):
#     first = models.CharField(max_length=100)
#     last = models.CharField(max_length=100)
#     middle = models.CharField(max_length=100, blank=True)
#
#     class Meta:
#         ordering = ['first', 'last', 'middle']
#         unique_together = ['first', 'last', 'middle']
#         verbose_name_plural = 'people'

admin.site.register(BlogPost, BlogPostAdmin)   #对BlogPost在管理员界面进行注册以便显示