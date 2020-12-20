from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']

    #  __init__.py from the app is called, which can help modify beahvior of the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add attributes to the field called text
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'What\'s on your mind'})