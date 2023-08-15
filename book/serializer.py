from rest_framework import serializers

from models import Book, Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ['url', 'id', 'author', 'slug', 'title', 'genre', 'rating']
        read_only_fields = ['slug']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        field = Review
        field = ['url', 'id', 'user', 'book', 'content', 'rating']
