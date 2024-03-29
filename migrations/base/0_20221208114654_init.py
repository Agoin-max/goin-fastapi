from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `access` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `access_name` VARCHAR(15) NOT NULL  COMMENT '权限名称',
    `parent_id` INT NOT NULL  COMMENT '父id' DEFAULT 0,
    `scopes` VARCHAR(255) NOT NULL UNIQUE COMMENT '权限范围标识',
    `access_desc` VARCHAR(255)   COMMENT '权限描述',
    `menu_icon` VARCHAR(255)   COMMENT '菜单图标',
    `is_check` BOOL NOT NULL  COMMENT '是否验证权限 True为验证 False不验证' DEFAULT 0,
    `is_menu` BOOL NOT NULL  COMMENT '是否为菜单 True菜单 False不是菜单' DEFAULT 0
) CHARACTER SET utf8mb4 COMMENT='权限表';
CREATE TABLE IF NOT EXISTS `access_log` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` INT NOT NULL  COMMENT '用户ID',
    `target_url` VARCHAR(255)   COMMENT '访问的url',
    `user_agent` VARCHAR(255)   COMMENT '访问UA',
    `request_params` JSON   COMMENT '请求参数get|post',
    `ip` VARCHAR(32)   COMMENT '访问IP',
    `note` VARCHAR(255)   COMMENT '备注'
) CHARACTER SET utf8mb4 COMMENT='用户操作记录表';
CREATE TABLE IF NOT EXISTS `author` (
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(62) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='作家';
CREATE TABLE IF NOT EXISTS `book` (
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `book_name` VARCHAR(62) NOT NULL,
    `author_id` INT NOT NULL,
    CONSTRAINT `fk_book_author_ed0cb68f` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='图书';
CREATE TABLE IF NOT EXISTS `role` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `role_name` VARCHAR(15) NOT NULL  COMMENT '角色名称',
    `role_status` BOOL NOT NULL  COMMENT 'True:启用 False:禁用' DEFAULT 0,
    `role_desc` VARCHAR(255)   COMMENT '角色描述'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `system_params` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `params_name` VARCHAR(255) NOT NULL UNIQUE COMMENT '参数名',
    `params` JSON NOT NULL  COMMENT '参数'
) CHARACTER SET utf8mb4 COMMENT='系统参数表';
CREATE TABLE IF NOT EXISTS `user` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `username` VARCHAR(20)   COMMENT '用户名',
    `user_type` BOOL NOT NULL  COMMENT '用户类型 True:超级管理员 False:普通管理员' DEFAULT 0,
    `password` VARCHAR(255),
    `nickname` VARCHAR(255) NOT NULL  COMMENT '昵称' DEFAULT 'binkuolo',
    `user_phone` VARCHAR(11)   COMMENT '手机号',
    `user_email` VARCHAR(255)   COMMENT '邮箱',
    `full_name` VARCHAR(255)   COMMENT '姓名',
    `user_status` INT NOT NULL  COMMENT '0未激活 1正常 2禁用' DEFAULT 0,
    `header_img` VARCHAR(255)   COMMENT '头像',
    `sex` INT   COMMENT '0未知 1男 2女' DEFAULT 0,
    `remarks` VARCHAR(30)   COMMENT '备注',
    `client_host` VARCHAR(19)   COMMENT '访问IP'
) CHARACTER SET utf8mb4 COMMENT='用户表';
CREATE TABLE IF NOT EXISTS `user_wechat` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `city` VARCHAR(255)   COMMENT '城市',
    `country` VARCHAR(255)   COMMENT '国家',
    `headimgurl` VARCHAR(255)   COMMENT '微信头像',
    `nickname` VARCHAR(255)   COMMENT '微信昵称',
    `openid` VARCHAR(255) NOT NULL UNIQUE COMMENT 'openid',
    `unionid` VARCHAR(255)  UNIQUE COMMENT 'unionid',
    `province` VARCHAR(255)   COMMENT '省份',
    `sex` INT   COMMENT '性别',
    `user_id` INT NOT NULL UNIQUE,
    CONSTRAINT `fk_user_wec_user_a1775abb` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='用户微信';
CREATE TABLE IF NOT EXISTS `role_access` (
    `role_id` INT NOT NULL,
    `access_id` INT NOT NULL,
    FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`access_id`) REFERENCES `access` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `user_role` (
    `user_id` INT NOT NULL,
    `role_id` INT NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
