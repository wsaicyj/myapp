from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Update


# Create your views here.
# class UpdateListView(TemplateView):
#     template_name = "update_list.html"
#     object_list = Update.objects.all()
def update_list(request):
    object_list = Update.objects.all()
    return render(request, 'update_list.html', {'object_list': object_list})
