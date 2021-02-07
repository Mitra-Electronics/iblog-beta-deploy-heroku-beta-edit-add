# framwork imports
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# project imports
from .forms import UploadForm, CommentForm
import uuid
from .models import Blog, Comment


# Create your views here.

def home(request):
    videos = Blog.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Blog.objects.filter(blog_title__icontains=search)
    return render(request, 'blog/home.html', {'videos': videos, 'search': search, 'result': result})


@login_required
def upload_blog(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            title = video.blog_title
            video.user = request.user
            video.slug = str(uuid.uuid4())
            video.save()
            messages.success(request, f'Blog upload sucessful')
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'blog/upload_blog.html', {'form': form})


def details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog_details', kwargs={'slug': slug}))
    return render(request, 'blog/blog_details.html', {'blog': blog, 'form': comment_form})


@login_required
def edit_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = UploadForm(instance=Blog)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            #form = UploadForm(instance=Blog)
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'blog/edit_blog.html', {'form': form, 'edit': True})


def services(request):
    return render(request, 'services/services.html', {})
