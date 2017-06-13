from django.test import TestCase

# Create your tests here.
from blog.models import BlogPost


posts = BlogPost.objects.all().order_by('-timestamp')
print(posts)