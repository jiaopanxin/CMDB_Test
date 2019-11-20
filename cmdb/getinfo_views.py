from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, HttpResponse,redirect
from cmdb.models import Memory,Server, Disk
@method_decorator(csrf_exempt, name='dispatch')
class AssetInfoView(View):
    def get(self, request):
        return HttpResponse("get方法")
    
    def post(self, request):
        # print("body数据", request.body)
        # # 将请求发送的数据信息转为字符串形式
        assert_s = str(request.body, encoding='utf-8')
       
        ## 将字符串型的数据反序列化
        assert_data = json.loads(assert_s)           
        base_info =  assert_data['base']
        cpu_info = assert_data['cpu']
        mem_info = assert_data['memory']
        disk_info = assert_data['disk']
            
            # 将两个字典合并到一个字典中
        server_info = {**base_info,**cpu_info}
        try:
            server_obj = Server.objects.create(**server_info)
            for k,v in mem_info.items():                         
                #  将值插入到表中, host_name是外键,间接指定, 它必须是要关联的表的对象
                Memory.objects.create(**v, server=server_obj)
            for keys,values in disk_info.items():              
                #  将值插入到表中, host_name是外键,间接指定, 它必须是要关联的表的对象
                Disk.objects.create(**values, server=server_obj)
        except Exception as e:
            print(e)
            return HttpResponse("存库失败")