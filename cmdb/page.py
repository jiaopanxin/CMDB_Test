#  自定义的分页的方法
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
class StandardResultsSetPagination(PageNumberPagination):
    # 每页 2 条数据
    page_size = 5  
    
    page_size_query_param = 'page_size'
    
    # 请求页码的参数名   
    page_query_param = 'p'  
    
    # 最大的页面数
    max_page_size = 10
    def get_paginated_response(self, data):
        return Response({
            'links':self.get_html_context(),
            'count': self.page.paginator.count,
            'results': data
        })


from django.views.generic import ListView

from pure_pagination.mixins import PaginationMixin

class MyModelListView(PaginationMixin, ListView):
    paginate_by= 10   #每页显示的数据


