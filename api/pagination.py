from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.utils.http import urlencode
from .utils.response import api_response
from api.models import Drink


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 200

    # Next URL
    def get_next_page_url(self):
        if not self.page.has_next():
            return None

        query_params = self.request.query_params.copy()
        query_params["page"] = self.page.next_page_number()

        return f"{self.request.path}?{urlencode(query_params)}"

    # Previous URL
    def get_prev_page_url(self):
        if not self.page.has_previous():
            return None

        query_params = self.request.query_params.copy()
        query_params["page"] = self.page.previous_page_number()

        return f"{self.request.path}?{urlencode(query_params)}"

    def get_paginated_response(self, data):
        pagination_data = {
            "filtered_count": self.page.paginator.count,
            "total_count": Drink.objects.count(),
            "page": self.page.number,
            "page_size": self.get_page_size(self.request),
            "total_pages": self.page.paginator.num_pages,
            "next_page_url": self.get_next_page_url(),
            "prev_page_url": self.get_prev_page_url(),
        }

        return Response(
            api_response(
                data={
                    "results": data,
                    "pagination": pagination_data,
                },
                message="Paginated results",
            )
        )
