from rest_framework import serializers

from .models import Book, Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'author', 'slug', 'title', 'genre', 'rating']
        read_only_fields = ['slug']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['url', 'id', 'user', 'book', 'review_text', 'rating']
