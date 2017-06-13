from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from .models import BlogPost
# Create your views here.
def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')  # 查出全部数据
    return render(request, 'archive.html', {'posts': posts})
    # posts = BlogPost.objects.all()  # 查出全部数据
    # posts = get_object_or_404(BlogPost, pk=id)
    # t = loader.get_template("archive.html")
    # c = Context({'posts': posts})
    # return HttpResponse(t.render(c))     #进行模板渲染