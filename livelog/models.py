from django.db import models
from django.contrib import admin

# Create your models here.
'''
应用程序只含有一个网页。不需要其他花哨的东西-我们只是要建立一个一次更新一个事件的liveblog
它只跟踪一条连续的信息流。尽量保持简单
这个流由带时间戳的文本段落组成。所以我们的模型只需要两个变量
这条流按时间逆序显示，即最新的放在最前面。所以最新的信息总是显示在页面顶端
初始页面载入显示的是流的当前状态。访问一个不断变化的liveblog的用户无需Ajax就可以看到那一刻为止的所有事件
页面每隔一分钟就会向服务器提出新的请求。
事件是通过Django admin添加的。不过若是有老板娘，为他创建一个自定义的表彰也不难-为了得到更出色 的响应，你甚至可以在后台也使用Ajax提交
'''

class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return "(%s) %s" % (self.timestamp.strftime("%Y-%m-%d %H:%M:%S"), self.text)


class UpdateAdmin(admin.ModelAdmin):
    list_display = ('text', 'timestamp')

admin.site.register(Update, UpdateAdmin)