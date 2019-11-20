from celery.result import AsyncResult
from .utils.handlecommand import handlecommand
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, ListView, DetailView


from cmdb.models import Server, Invertory_group, Invertory_group
import pexpect
import subprocess
import json
import os


class ConnectionView(View):
    def get(self, request):
        conninfo = Server.objects.all()

        return render(request, "octoups/connection.html", {"connection": conninfo})

    def post(self, request):
        id = request.POST.get("server_id")
        server = Server.objects.filter(id=id)[0]
        auth = server.connection.auth
        if auth:
            # 还需要判断推送的公钥和现有的公钥是否一致
            return JsonResponse({"status": "公钥不需要再次推送"})

        user = server.connection.user
        port = server.connection.port
        ip = server.manager_ip

        shell_command = "ssh-copy-id -p {} {}@{} ".format(port, user, ip)
        print(shell_command)

        child = pexpect.spawn(shell_command)

        index = child.expect(["yes/no", "password", "exist",
                              pexpect.exceptions.EOF, pexpect.TIMEOUT], timeout=5)
        try:
            print("开始向%s上传公钥" % (ip))
            child.sendline("yes")
            child.expect("password")
            child.sendline("qwe123qwe")
            child.expect("added")
            print("已向%s上传公钥" % (ip))
            server.connection.auth = True
            server.connection.save()
            return JsonResponse({"status": True})
        except Exception as e:
            return JsonResponse({"status": False})


class ExecCommandView(View):
    def get(self, request):
        
        invertory = Invertory_group.objects.all()
        return render(request, "octoups/run.html", {"data": invertory})

    def post(self, request):
        command = request.POST.get("data")

        from .tasks import exec_command

        task_id = exec_command.delay(command)
        return JsonResponse({"task_id": task_id.id})


class CommandResultView(View):
    def get(self, request):
        task_id = request.GET.get("task_id")
        task_obj = AsyncResult(id=task_id)
        task_json = {
            "id": task_obj.id,
            "status": task_obj.status,
            "success": task_obj.successful(),
            "result": task_obj.result
        }
        
        return JsonResponse(task_json)


class AsyncDemoView(View):
    def get(self, request):
        return render(request, "octoups/async-demo.html")

    def post(self, request):
        num = request.POST.get("num")
        from .tasks import add
        result = add.delay(int(num))
        print("命令已送达")
        return JsonResponse({"task_id": result.task_id})


class AnsibleAdhocView(View):
    def get(self, request):
        inventory = Invertory_group.objects.all()

        return render(request, "octoups/ansible-adhoc.html", {"info": inventory})

    def post(self, request):

        inv_path = request.POST.get("inv_path")
        remote_user = request.POST.get("remote_user")
        connection = request.POST.get("connection")
        model = request.POST.get("model")
        group = request.POST.get("group")
        args = request.POST.get("args")

        from octoups.tasks import ansible_ad_hoc

        result = ansible_ad_hoc.delay(connection, remote_user, inv_path, group, model, args)


        return JsonResponse({"task_id": result.task_id})
