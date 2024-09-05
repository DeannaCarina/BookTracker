from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Book
from django.http import HttpResponseRedirect
from .forms import BookForm


# Create your views here.

def all_books(request):
    """ A view to show all excursions, including sorting and searching """

    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/all_books.html', context)

def unread_books(request):
    """ A view to show all excursions, including sorting and searching """

    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/unread_books.html', context)

def completed_books(request):
    """ A view to show all excursions, including sorting and searching """

    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/completed_books.html', context)


def view_book(request, pk):
    """ A view to show individual book information """
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'books/view_book.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect(reverse('view_book', args=[book.pk]))
    else:
        form = BookForm()

    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_book', args=[book.pk]))
    else:
        form = BookForm(instance=book)

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)

def delete_book(request, pk):
    """ Delete a product from the store """
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect(reverse('books'))
