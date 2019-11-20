from django.shortcuts import render
from django.views import View
from cmdb.models import Asset
from django.http import JsonResponse
# Create your views here.
class ApiView(View):
    def get(self, request):
        users = Asset.objects.values()        
        return JsonResponse(list(users), safe=False)
