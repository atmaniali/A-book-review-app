from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Book, Review
from .serializer import BookSerializer, ReviewSerializer
from .peremission import IsUserOwnerOrGetOrPostOnly


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['rating', 'genre']
    search_fields = ['author', 'title']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsUserOwnerOrGetOrPostOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['rating']
    search_fields = ['user', 'book']
