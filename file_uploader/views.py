from django.shortcuts import render
from .models import Document

# Create your views here.
def documents(request, category=None):
    template = 'documents.html'
    error = None
    if category:
        try:
            docs = Document.objects.filter(category=category)
        except Document.DoesNotExist:
            docs = None  # Do I need this?
        if not docs:
            error = 'Der er ingen dokumenter i denne kategori.'
    else:
        try:
            docs = Document.objects.all()[0:3]
        except Document.DoesNotExist:
            docs = None

    context = {
        'docs': docs,
        'error': error,
        'category': category,
    }

    return render(request, template, context)