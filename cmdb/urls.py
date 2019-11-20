from django.urls import path, include

from django.views.generic import TemplateView

from . import views, getinfo_views

from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'assets', views.AssetViewSet)
router.register(r'memory', views.MemoryViewSet)
router.register(r'server', views.ServerViewSet)
router.register(r'disk', views.DiskViewSet)
router.register(r'idc', views.IDCViewSet)
router.register(r'cabinet', views.CabinetViewSet)
router.register(r'server-tree', views.ServerTreeViewSet)
router.register(r'assets', views.AssetsViewSet)



app_name = "cmdb"

urlpatterns = [
    path('', include(router.urls)),
    # 获取服务器信息, 并将服务器信息储存至数据库的路由
    path('asset/', getinfo_views.AssetInfoView.as_view(), name="asset-list"),
    path('assets-list/', views.AssetViewSet.as_view(), name="assets"),
    # path('delete/<slug:id>/', views.assets_delete,name="delete"),
    # 直接显示视图的模块   TemplateView   (CBV)
#     path('assets-list/',TemplateView.as_view(template_name="cmdb/assets-list.html"),name="assets-list"),
    # path('memory-list/',TemplateView.as_view(template_name="cmdb/memory-list.html"),name="memory-list"),
    path('assets-list/asset-detail/',TemplateView.as_view(template_name="cmdb/server-list.html"),name="asset-detail"), 
    path('server-list/',TemplateView.as_view(template_name="cmdb/server-list.html"),name="server-list"),
    path('idc-list/',TemplateView.as_view(template_name="cmdb/idc-list.html"),name="idc-list"),
    path('cabinet-list/',TemplateView.as_view(template_name="cmdb/cabinet-list.html"),name="cabinet-list"),
    path('assets-list/', TemplateView.as_view(template_name="cmdb/assets-list.html"),
         name="assets-list"),

    path('server-list/', TemplateView.as_view(template_name="cmdb/server-list.html"),
         name="server-list"),
    path('memory-list/', TemplateView.as_view(template_name="cmdb/memory-list.html"),
         name="memory-list"),
    path('disk-list/', TemplateView.as_view(template_name="cmdb/disk-list.html"),
         name="disk-list"),

    #  详情页
    path("detail_server/", TemplateView.as_view(template_name="cmdb/detail_server.html"),
         name="detail_server"),
    path('assets-list/asset-detail/',
         TemplateView.as_view(template_name="cmdb/server-list.html"), name="asset-detail"),
    path('asset-detail/<slug:pk>',views.asset_detail.as_view(),name="asset-detail"),


    # 删除数据
    path("del_server/", views.del_server.as_view(), name="del_server"),

]
