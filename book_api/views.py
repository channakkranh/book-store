from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from book_api.models import Book

# Create your views here.
def test(request):
    return HttpResponse('Hello')

def book_list(request):
    books=Book.objects.all()
    books_pyhton=list(books.values())
    return JsonResponse ({
        'books':books_pyhton
    })


