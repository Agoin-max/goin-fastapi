from tortoise import Model, fields


class TokenLog(Model):
    uid = fields.IntField(null=False, description="用户uid")
    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    token = fields.CharField(max_length=60, description="token值", null=False)
    ip = fields.CharField(max_length=30, null=False, description="用户ip")
    client = fields.CharField(max_length=600, null=False, description="客户端信息")

    class Meta:
        table = "tbl_token_log"

# CREATE TABLE `tbl_token_log` (
#   `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `uid` int(10) unsigned NOT NULL COMMENT '用户uid',
#   `created_at` datetime NOT NULL COMMENT '创建时间',
#   `ip` char(60) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'ip地址',
#   `client` varchar(600) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '客户端信息',
#   `token` char(60) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'token值',
#   PRIMARY KEY (`id`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=1582 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci