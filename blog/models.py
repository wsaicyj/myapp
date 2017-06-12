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




admin.site.register(BlogPost, BlogPostAdmin)   #对BlogPost在管理员界面进行注册以便显示