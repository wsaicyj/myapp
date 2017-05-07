from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from .models import BlogPost
# Create your views here.
def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')   #查出全部数据
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))     #进行模板渲染