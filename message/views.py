from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def posts(request):
    plist = Post.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'message/index.html', {'posts': plist})
