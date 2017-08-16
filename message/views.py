from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import Pform
# Create your views here.
#function to submit posts to template in order
def posts(request):
    plist = Post.objects.filter(post_date__lte=timezone.now()).order_by('-post_date')
    return render(request, 'message/post.html', {'posts': plist})
#puts only one post on a page dedicated to that post
def post_detail(request, pk):
    selectedPost = Post.objects.get(pk=pk)
    return render(request, 'message/post_detail.html', {'post': selectedPost})
#bring up a page to sbmit new post
def post_new(request):
    if request.method == "POST":
        form = Pform(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.post_date = timezone.now()
            post.save()
            return redirect('posts')
    else:
        form = Pform()
    return render(request, 'message/post_add.html', {'form': form})
