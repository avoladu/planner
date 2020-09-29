from django.shortcuts import render

from .models import *
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

class BoardList(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filters_fields = ["title"]
    search_fields = ["title", "id"]
    ordering_fields = ["id", "title"]

class BoardCreate(generics.CreateAPIView):
    serializer_class = BoardSerializer

class BoardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

class BoardFilter(generics.ListAPIView):
    serializer_class = BoardListSerializer
    def get_queryset(self):
        return Board.objects.filter(title=self.kwargs['title'])