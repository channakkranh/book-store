# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from book_api.models import Book
# from book_api.serializer import BookSerializer

# # Create your views here.
# @api_view(['GET'])
# def book_list(request):
#     books=Book.objects.all()
#     serializer=BookSerializer(books,many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create_book(request):
#     serializer=BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data),
#     else:
#         return Response(serializer.errors),
    
   
# @api_view(['GET','PUT','DELETE'])
# def book(request,pk):
#     if request.method=='GET':
#         book=Book.objects.get(pk=pk)
#         serializer=BookSerializer(book)
#         return Response (serializer.data)
    


# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})



 # books_pyhton=list(books.values())
    # return JsonResponse ({
    #     'books':books_pyhton
    # })

# we use class view 

from rest_framework.views import APIView
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self, request):
         books=Book.objects.all()
         serializer=BookSerializer(books,many=True)
         return Response(serializer.data)
    
# class CreatBook(APIView):
#      def post(self,requst):
    
#          serializer=BookSerializer(data=request.data)
#          if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data),
#          else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST),
class CreateBook(APIView):
     def post(self, request):
    
         serializer = BookSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
# class Book(APIView):
#     def get(self,request,pk):
#          try:
#              book=Book.objects.get(pk=pk)
#         except:
    
#          serializer=BookSerializer(book)
#          return Response(serializer.data)