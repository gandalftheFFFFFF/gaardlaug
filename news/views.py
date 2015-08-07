from django.shortcuts import render
from .models import Post, Image
from file_uploader.models import Document

# Create your views here.
def get_latest_post():
    try:
        post = Post.objects.latest('date')
    except Post.DoesNotExist:
        post = None

    try:
        docs = Document.objects.filter(post=post)
    except Document.DoesNotExist:
        docs = None

    try:
        images = Image.objects.filter(post=post)
    except Document.DoesNotExist:
        images = None

    return post, docs, images


def news(request):
    template = 'news.html'

    post, docs, images = get_latest_post()

    context = {
        'post':post,
        'docs': docs,
        'images': images,
    }

    return render(request, template, context)


def specific_post(request, post_slug):
    template = 'specific_post.html'

    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        post = None

    try:
        docs = Document.objects.filter(post=post)
    except Document.DoesNotExist:
        docs = None

    try:
        images = Image.objects.filter(post=post)
    except Document.DoesNotExist:
        images = None

    context = {
        'post':post,
        'docs': docs,
        'images': images,
    }

    return render(request, template, context)


def archive(request):
    template = 'news_archive.html'

    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None

    # List to store all dicts in
    arcs = []

    if posts:
        for post in posts:
            arcs.append({'post': post, 'year': post.date.year, 'date': post.date})

    context = {
        'arcs': arcs,
    }

    return render(request, template, context)


def latest(request):
    template = 'latest.html'

    post, docs, images = get_latest_post()

    context = {
        'post':post,
        'docs': docs,
        'images': images,
    }

    return render(request, template, context)
