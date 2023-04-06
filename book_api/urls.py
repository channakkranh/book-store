from django.urls import path
from.import views


urlpatterns = [
    path('test/',views.hello_world),
    path ('book/list/',views.book_list)
]