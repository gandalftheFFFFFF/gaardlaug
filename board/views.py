from django.shortcuts import render
from .models import BoardMember, Matrikel

# Create your views here.
def index(request):
    template = 'board.html'
    try:
        members = BoardMember.objects.all()
    except BoardMember.DoesNotExist:
        members = None

    try:
        mats = Matrikel.objects.all()
    except Matrikel.DoesNotExist:
        mats = None

    context = {
        'members': members,
        'mats': mats,
    }

    return render(request, template, context)
