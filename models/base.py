from tortoise import Model, fields


class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")


class Role(TimestampMixin):
    role_name = fields.CharField(max_length=15, description="角色名称")
    user: fields.ManyToManyRelation["User"] = fields.ManyToManyField("default.User", related_name="role",
                                                                     on_delete=fields.CASCADE)
    access: fields.ManyToManyRelation["Access"] = fields.ManyToManyField("default.Access", related_name="role",
                                                                         on_delete=fields.CASCADE)
    role_status = fields.BooleanField(default=False, description="True:启用 False:禁用")
    role_desc = fields.CharField(null=True, max_length=255, description="角色描述")

    class Meta:
        table_description = "角色表"
        table = "role"


class User(TimestampMixin):
    role: fields.ManyToManyRelation[Role]
    username = fields.CharField(null=True, max_length=20, description="用户名")
    type = fields.BooleanField(default=False, description="用户类型 True:超级管理员 False:普通管理员")
    password = fields.CharField(null=True, max_length=255, description="密码")
    nickname = fields.CharField(default="Goin", max_length=60, description="昵称")
    u_phone = fields.CharField(null=True, max_length=11, description="手机号")
    u_email = fields.CharField(null=True, max_length=100, description="邮箱")
    full_name = fields.CharField(null=True, max_length=60, description="姓名")
    u_status = fields.SmallIntField(default=0, description="0未激活 1正常 2禁用")
    head_img = fields.CharField(null=True, max_length=255, description="头像")
    sex = fields.SmallIntField(default=0, null=True, description="0未知 1男 2女")
    remarks = fields.CharField(null=True, max_length=60, description="备注")
    client_host = fields.CharField(null=True, max_length=20, description="访问IP")

    class Meta:
        table_description = "用户"
        table = "user"


class Access(TimestampMixin):
    role: fields.ManyToManyRelation[Role]
    rule_name = fields.CharField(max_length=15, description="权限名称")
    parent_id = fields.IntField(default=0, description="父id")
    scopes = fields.CharField(unique=True, max_length=255, description="权限范围标识")
    rule_desc = fields.CharField(null=True, max_length=255, description="权限描述")
    menu_icon = fields.CharField(null=True, max_length=255, description="菜单图标")
    is_check = fields.BooleanField(default=False, description="是否验证权限 True为验证 False不验证")
    is_menu = fields.BooleanField(default=False, description="是否为菜单 True为菜单 False不是菜单")

    class Meta:
        table_description = "权限表"
        table = "access"


class AccessLog(TimestampMixin):
    user_id = fields.IntField(description="用户ID")
    target_url = fields.CharField(null=True, description="访问的url", max_length=255)
    user_agent = fields.CharField(null=True, description="访问的user_agent", max_length=255)
    request_params = fields.JSONField(null=True, description="请求参数get|post")
    ip = fields.CharField(null=True, max_length=32, description="访问IP")
    note = fields.CharField(null=True, max_length=255, description="备注")

    class Meta:
        table_description = "用户操作记录表"
        table = "access_log"


class Token(Model):
    uid = fields.IntField(null=False, description="用户id")
    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_at = fields.DatetimeField(auto_now=True, description="更新时间")
    token = fields.CharField(max_length=60, description="token值", null=False)
    ip = fields.CharField(max_length=30, null=False, description="用户ip")
    client_md5 = fields.CharField(max_length=32, null=False, description="客户端信息md5")

    class Meta:
        table = "tbl_token"

# CREATE TABLE `tbl_token` (
#   `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `uid` int(10) unsigned NOT NULL COMMENT '用户id',
#   `created_at` datetime NOT NULL COMMENT '创建时间',
#   `updated_at` datetime NOT NULL,
#   `token` char(60) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'token值',
#   `ip` char(30) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '用户ip',
#   `client_md5` char(32) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '客户端信息md5',
#   PRIMARY KEY (`id`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=1582 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
