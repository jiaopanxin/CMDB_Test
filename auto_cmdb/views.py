from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from cmdb.models import Asset
from django.db.models import Count


class DashView(View):
    def get(self, request):
        type_qs1 = list(Asset.objects.filter(device_type_id=1).values_list('device_status_id').annotate(value=Count('device_status_id')))   
        type_qs2 = list(Asset.objects.filter(device_type_id=2).values_list('device_status_id').annotate(value=Count('device_status_id')))   
        type_qs3 = list(Asset.objects.filter(device_type_id=3).values_list('device_status_id').annotate(value=Count('device_status_id')))   
        type_qs4 = list(Asset.objects.filter(device_type_id=4).values_list('device_status_id').annotate(value=Count('device_status_id')))           
        # li.insert(type_qs[0][0],type_qs[0][1])
        dic1 = {}
        dic2 = {}
        dic3 = {}
        dic4 = {}
        for tup1 in type_qs1:
               dic1[tup1[0]] = tup1[1]
        for tup2 in type_qs2:
               dic2[tup2[0]] = tup2[1]
        for tup3 in type_qs3:
               dic3[tup3[0]] = tup3[1]
        for tup4 in type_qs4:
               dic4[tup4[0]] = tup4[1]
        li = [
            ['设备状态',"上架" ,"在线", "离线","下架"],
            ["服务器", dic1.get('1'), dic1.get('2'),dic1.get('3'),dic1.get('4')],
            ["路由器", dic2.get('1'), dic2.get('2'),dic2.get('3'),dic2.get('4')],
            ["交换机", dic3.get('1'), dic3.get('2'),dic3.get('3'),dic3.get('4')],
            ["防火墙", dic4.get('1'), dic4.get('2'),dic4.get('3'),dic4.get('4')],
        ]
        return JsonResponse(li,safe=False)
