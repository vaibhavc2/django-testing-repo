from django.shortcuts import redirect, render

from .forms import BookForm, BookUpdateForm
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookUpdateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookUpdateForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form})