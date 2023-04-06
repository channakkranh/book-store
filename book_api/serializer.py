from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=100)
    num_of_pages=serializers.IntegerField()
    public_date=serializers.DateField()
    quatity=serializers.IntegerField()