from django.contrib import admin
from cmdb.models import Asset,Memory,Server,Tag,Cabinet,IDC,TreeNode
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass

class IDCAdmin(admin.ModelAdmin):
    pass

class CabinetAdmin(admin.ModelAdmin):
    pass

class AssetAdmin(admin.ModelAdmin):
    pass

class MemoryAdmin(admin.ModelAdmin):
    pass


class TreeNodeAdmin(admin.ModelAdmin):
    pass

class ServerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Asset,AssetAdmin)
admin.site.register(Memory,MemoryAdmin)
admin.site.register(TreeNode,TreeNodeAdmin)
admin.site.register(Server,ServerAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Cabinet,CabinetAdmin)
admin.site.register(IDC,IDCAdmin)




