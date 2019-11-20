from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.views import View
# 
from rest_framework import viewsets


from cmdb.models import Asset,Server,Memory,IDC,Cabinet
from .serialazer import AssetSerializer,MemorySerializer,ServerSerializer,IDCSerializer,CabinetSerializer,TreeNodeSerializer

from cmdb.models import Asset,Server,Memory,IDC,Cabinet,Disk,TreeNode
from .serialazer import AssetSerializer,MemorySerializer,ServerSerializer,IDCSerializer,CabinetSerializer,DiskSerializer

from .page import StandardResultsSetPagination

#分页
from pure_pagination.mixins import PaginationMixin


class AssetViewSet(View):
    def get(self, request):
        asset = Asset.objects.all()
        return render(request, 'cmdb/assets-list.html', {"assetList":asset})


class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    pagination_class = StandardResultsSetPagination


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    pagination_class = StandardResultsSetPagination


class IDCViewSet(viewsets.ModelViewSet):
    queryset=IDC.objects.all()
    serializer_class=IDCSerializer
    pagination_class=StandardResultsSetPagination


class CabinetViewSet(viewsets.ModelViewSet):
    queryset=Cabinet.objects.all()
    serializer_class=CabinetSerializer
    pagination_class=StandardResultsSetPagination


class DiskViewSet(viewsets.ModelViewSet):
    queryset=Disk.objects.all()
    serializer_class=DiskSerializer
    pagination_class=StandardResultsSetPagination

class TreeViewSet(viewsets.ModelViewSet):
    queryset=TreeNode.objects.filter(node_upstream=None)
    serializer_class=TreeNodeSerializer

class AssetsViewSet(viewsets.ModelViewSet):
    queryset=Asset.objects.all()
    serializer_class=AssetSerializer



#删除数据
class del_server(View):
    def get(self,request):
        id=request.GET.get("id")
        Server.objects.filter(id=id).delete()
        return render(request,"cmdb/server-list.html")

###服务树
class ServerTreeViewSet(viewsets.ModelViewSet):
    queryset = TreeNode.objects.filter(node_upstream=None)
    serializer_class = TreeNodeSerializer


#服务器跳转详情
class asset_detail(DetailView):
    model=Server

    context_object_name="info"

    template_name="cmdb/assetserver_detail.html"






