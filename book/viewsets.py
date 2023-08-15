from rest_framework import viewsets

from models import Book, Review
from .serializer import BookSerializer, ReviewSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objets.all()
    serializer_class = BookSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer