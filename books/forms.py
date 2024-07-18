
from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs['placeholder'] = 'Book title'
        self.fields['author'].widget.attrs['placeholder'] = 'Book author'
        self.fields['published'].widget.attrs['placeholder'] = 'Year published'
        self.fields['pages'].widget.attrs['placeholder'] = 'Total pages'
        self.fields['progress'].widget.attrs['placeholder'] = 'Current page'
        self.fields['frontcover'].widget.attrs['placeholder'] = 'Front cover:'
        self.fields['genre'].widget.attrs['placeholder'] = 'Genre'
        self.fields['keypoints'].widget.attrs['placeholder'] = 'Keypoints'
        

