from django.urls import path
from.import views

urlpatterns = [
    # path('test/',views.hello_world),
    path ('book/list/',views.BookList.as_view()),
    path('book/post/',views.CreateBook.as_view()),
    # path('book/', views.Book.as_view())
]