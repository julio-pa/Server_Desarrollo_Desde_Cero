from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 7


class MediumSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class LargeSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 18
    page_size_query_param = 'page_size'
    max_page_size = 18
