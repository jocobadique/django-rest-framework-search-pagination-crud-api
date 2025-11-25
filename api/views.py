from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Drink
from .serializers import DrinkSerializer
from .pagination import StandardPagination
from .utils.response import api_response
from .permissions import IsAdminOrReadOnly


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    pagination_class = StandardPagination

    # 🔎 Enable Search + Filtering
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name", "category__name"]  # ?search=cola
    filterset_fields = ["category", "id"]  # ?category=2
    ordering_fields = ["name", "id"]  # ?ordering=name

    # list
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.paginator.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            api_response(data=serializer.data, message="Fetched drinks successfully")
        )

    # create
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                api_response(
                    data=serializer.data, message="Drink created successfully"
                ),
                status=status.HTTP_201_CREATED,
            )

        return Response(
            api_response(
                data=None, message="See error on fields", error=serializer.errors
            ),
            status=status.HTTP_400_BAD_REQUEST,
        )

    # retrieve
    def retrieve(self, request, *args, **kwargs):
        drink = self.get_object()
        serializer = self.get_serializer(drink)
        return Response(api_response(data=serializer.data, message="Drink retrieved"))

    # update
    def update(self, request, *args, **kwargs):
        drink = self.get_object()
        serializer = self.get_serializer(drink, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                api_response(data=serializer.data, message="Drink updated successfully")
            )

        return Response(
            api_response(error=serializer.errors, message="See error on fields"),
            status=status.HTTP_400_BAD_REQUEST,
        )

    # delete
    def destroy(self, request, *args, **kwargs):
        drink = self.get_object()
        drink.delete()

        return Response(
            api_response(
                data=None,
                message="Drink deleted successfully",
                status=status.HTTP_204_NO_CONTENT,
            ),
            status=status.HTTP_204_NO_CONTENT,
        )
