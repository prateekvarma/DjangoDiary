from django.shortcuts import render, redirect
from . models import Entry
from .forms import EntryForm


# Create your views here.
def index(request):
    # entries = Entry.objects.all()
    # to get the latest DB entries
    entries = Entry.objects.order_by('-date_posted')
    return render(request, 'entries/index.html', {'entries': entries})


def add(request):
    if request.method == 'POST':
        # instantiate EntryForm with request data
        form = EntryForm(request.POST)
        # check if form data is valid
        if form.is_valid():
            form.save()  # simple & easy as we're using ModelForm
            return redirect('home')
    else:
        # it's a GET request, so initialize the form and send to template
        form = EntryForm()
        return render(request, 'entries/add.html', {'form': form})