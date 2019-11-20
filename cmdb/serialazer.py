from rest_framework import serializers

from cmdb.models import Asset,Memory,Server,IDC,Cabinet,Disk,TreeNode


# # serializers 格式类
class AssetSerializer(serializers.ModelSerializer):
    device_type = serializers.SerializerMethodField()
    device_status = serializers.SerializerMethodField()
    server = serializers.SlugRelatedField(
        read_only=True,
        slug_field='host_name'
    )
    cabinet = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Asset
        fields = "__all__"

    def get_device_type(self, obj):
        return obj.get_device_type_id_display()

    def get_device_status(self, obj):
        return obj.get_device_status_id_display()


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = "__all__"


class IDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDC
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = "__all__"


class DiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disk
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    memory = MemorySerializer(many=True)
    disk = DiskSerializer(many=True)

    class Meta:
        model = Server
        fields = ["id", "memory", "os_name", "host_name", "disk", "asset", "machine",
                  "os_version", "host_name", "kernel", "cpu_model", "cpu_type", "cpu_num", "cpu_cores", "latest_date", "create_at"]



class subsubTreeNodeSerializer(serializers.ModelSerializer):
    sub_node = serializers.SerializerMethodField()

    class Meta:
        model = TreeNode
        fields = "__all__"

    def get_sub_node(self, obj):
        return []


class subTreeNodeSerializer(serializers.ModelSerializer):
    sub_node = subsubTreeNodeSerializer(many=True)

    class Meta:
        model = TreeNode
        fields = "__all__"


class TreeNodeSerializer(serializers.ModelSerializer):
    sub_node = subTreeNodeSerializer(many=True)

    class Meta:
        model = TreeNode
        fields = "__all__"


#####服务树

class subsubTreeNodeSerializer(serializers.ModelSerializer):
    sub_node = serializers.SerializerMethodField()
    class Meta:
        model = TreeNode
        fields = "__all__"
    def get_sub_node(self, obj):
        return []
class subTreeNodeSerializer(serializers.ModelSerializer):
    sub_node = subsubTreeNodeSerializer(many=True)
    class Meta:
        model = TreeNode
        fields = "__all__"

class TreeNodeSerializer(serializers.ModelSerializer):
    sub_node = subTreeNodeSerializer(many=True)
    class Meta:
        model = TreeNode
        fields = "__all__"
