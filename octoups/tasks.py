# Create your tasks here
from __future__ import absolute_import, unicode_literals
from cmdb.models import Invertory_group
from .utils.handlecommand import handlecommand
from celery import shared_task


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def exec_command(command):
    invertory = Invertory_group.objects.all()
    hand = handlecommand(command, invertory)

    res = hand.exec_command()
    return res


@shared_task
def add(num):
    import time
    time.sleep(10)
    return num+10


@shared_task
def ansible_ad_hoc(connection="local", remote_user=None, inv_path=None, group="all", model="shell", args=""):

    from testansiblei import ResultCallback, MyAnsiable2

    myansible = MyAnsiable2(
        connection=connection, remote_user=remote_user, inventory=inv_path)

    myansible.run(hosts=group, module=model, args=args)

    result = myansible.get_result()


    return result
