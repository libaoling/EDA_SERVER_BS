from django.db import models

# Create your models here.


class User(models.Model):
    """用户信息"""
    user_id = models.AutoField('用户id', primary_key=True)
    user_name = models.CharField('用户名称', max_length=32, unique=True)
    user_pwd = models.CharField('用户密码', max_length=32)
    create_time = models.DateTimeField(null=True, blank=True)    # 创建时间
    login_time = models.DateTimeField(null=True, blank=True)     # 登录时间
    logout_time = models.DateTimeField(null=True, blank=True)    # 退出时间
    permission = models.IntegerField(blank=True, default=0)      # 用户权限: 管理员权限(1)  普通权限(0)--默认为0
    login_state = models.IntegerField(blank=True, default=0)     # 登录状态: 登陆(1) 未登录(0)
    is_delete = models.BooleanField('是否删除', default=False)


# Create your models here.
# 创建审讯室类表-Interrogation_room_table
# 属性如下:
# 1.id :审讯室id(int)
# 2.connection_number:连接的个数(int)
# 3.url_type:rstp类型(int)
#   0 为原始流：original_url(varchar)
#   1 为智能流:smart_url(varchar)
# 4.add_person:添加人(varchar)
# 5.create_time:创建时间时间(datetime)
# 6.is_del:是否删除(tinyint)
# 7.审讯状态interrogate_status()


class InterrogationRoomTable(models.Model):
    room_id = models.AutoField('审讯室id', primary_key=True)     # 审讯室id
    connection_number = models.IntegerField()    # 连接个数
    url_type = models.IntegerField()    # 0:原始流  1:智能流
    original_url = models.URLField()    # 原始流url
    smart_url = models.URLField()       # 智能流url
    add_person = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)    # 关联用户
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    is_del = models.BooleanField('是否删除', default=False)     # 用于假删除
    interrogate_status = models.BooleanField('状态', default=False)
