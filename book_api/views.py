from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializer import BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)



@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})



 # books_pyhton=list(books.values())
    # return JsonResponse ({
    #     'books':books_pyhton
    # })

