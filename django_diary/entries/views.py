from django.shortcuts import render
from . models import Entry
from .forms import EntryForm


# Create your views here.
def index(request):
    # entries = Entry.objects.all()
    # to get the latest DB entries
    entries = Entry.objects.order_by('-date_posted')
    return render(request, 'entries/index.html', {'entries': entries})


def add(request):
    form = EntryForm()
    return render(request, 'entries/add.html', {'form': form})