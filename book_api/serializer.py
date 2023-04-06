from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=100)
    num_of_pages=serializers.IntegerField()
    public_date=serializers.DateField()
    quatity=serializers.IntegerField()

    def create(self,data):
        return Book.objects.create(**data)


