import subprocess
from auto_cmdb.settings import INVENT_PATH as invent_path


class handlecommand:
    ret_msg = {
        "status": "False",
        "result": "命令格式错误"
    }

    def __init__(self, command, inventory):
        self.command = command
        self.invent_path = invent_path
        self.inventory = inventory
        self.command_tpl = "{} -i "+self.invent_path+" -{}"
        self.rewrite()

    def rewrite(self):
        li = []
        for group in self.inventory:
            li.append("["+group.group_name+"]"+"\n")
            for host in group.server.all():
                li.append(host.manager_ip+"\n")
        with open(self.invent_path, "w", encoding="utf-8") as wf:
            wf.writelines(li)

    def checked(self):
        ansib, arg = self.command.split("-", 1)
        self.command = self.command_tpl.format(ansib, arg)

        print(self.command)
        return self.command

    def exec_command(self):
        conn = self.checked()
        if conn:
            status, result = subprocess.getstatusoutput(conn)
            if not status:
                self.ret_msg["status"] = "True"
            self.ret_msg["result"] = result
        return self.ret_msg
