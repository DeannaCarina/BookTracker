from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

from django.contrib.auth.decorators import login_required
from django.db.models import Q

from books.models import Book
from django.http import HttpResponseRedirect



# Create your views here.

def index(request):
    """ A view to render the home page """

    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'home/index.html', context)
