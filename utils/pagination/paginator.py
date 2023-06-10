from rest_framework.pagination import PageNumberPagination


class FeaturePagination(PageNumberPagination):
    page_size = 100
