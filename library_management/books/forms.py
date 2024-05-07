from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'category', 'publication_date', 'availability_status']

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'category', 'publication_date', 'availability_status', 'borrower']

def clean_isbn(self):
    isbn = self.cleaned_data.get('isbn')
    if len(isbn) != 13:
        raise forms.ValidationError('ISBN must be 13 characters long.')
    return isbn        