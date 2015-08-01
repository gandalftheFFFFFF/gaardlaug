from django.shortcuts import render
from .models import Post, Image
from file_uploader.models import Document

# Create your views here.
def news(request):
    template = 'news.html'

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

    context = {
        'post':post,
        'docs': docs,
        'images': images,
    }

    return render(request, template, context)


def specific_post(request, post_slug):
    template = 'specific_post.html'

    try:
        post = Post.objects.filter(slug=post_slug)
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
        posts = Post.objects.filter(published=True)
    except Post.DoesNotExist:
        posts = None

    if posts:
        archive = {}
        for post in posts:
            year = post.date.year
            if year in archive:
                archive[year].append(post)
            else:
                archive[year] = [post, ]

    context = {
        'archive':archive,
    }

    return render(request, template, context)


def latest(request):
    template = 'latest.html'
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


    context = {
        'post':post,
        'docs': docs,
        'images': images,
    }

    return render(request, template, context)
