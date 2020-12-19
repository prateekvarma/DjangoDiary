from django.shortcuts import render
from . models import Entry


# Create your views here.
def index(request):
    # entries = Entry.objects.all()
    # to get the latest DB entries
    entries = Entry.objects.order_by('-date_posted')
    return render(request, 'entries/index.html', {'entries': entries})


def add(request):
    return render(request, 'entries/add.html')