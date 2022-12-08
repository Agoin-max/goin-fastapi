from fastapi import Request, APIRouter, Query
from aioredis import Redis

from core.Utils import code_number
from models.base import SystemParams, User
from core.Response import fail, success

router = APIRouter()


@router.get('/send', summary="发送验证码", description='注册、登陆')
async def send_msg(req: Request, phone_number: str = Query(..., regex="^1[34567890]\\d{9}$")):
    """
    验证码发送
    :param req:
    :param phone_number:
    :return:
    """
    session_code = req.session.get("session")
    # redis 连接
    redis: Redis = await req.app.state.cache
    # 查询当前手机号是否绑定用户
    user = await User.get_or_none(user_phone=phone_number)
    if not user:
        return fail(msg=f"手机号 {phone_number} 未绑定用户!")
    # 获取云短信配置
    # params = {
    #     "secret_id": "",
    #     "secret_key": "",
    #     "region": "ap-guangzhou",
    #     "app_id": "",
    #     "sign": "",
    #     "template_id": "",
    #     "expire": 10
    # }
    # result = await SystemParams.get_or_none(params_name="tencent_sms")
    # if not result:
    #     return fail(msg="请配置腾讯云短信参数")

    # 验证码过期时间
    # expire = result.params.get("expire")
    expire = 1
    # 查询是否发送过验证码
    is_send = await redis.get(name=f"code_{phone_number}")
    if is_send:
        return fail(msg=f"手机号 {phone_number} 已发送过验证码，若未收到短信，请{expire}分钟后重试!")

    # 生成验证码
    code = code_number(6)
    # 发送验证码
    # result.params.pop('expire')

    # 存入redis
    await redis.set(name=f"code_{phone_number}", value=code, ex=expire * 60)
    return success(msg=f"短信已经发送，{expire} 分钟内有效。", data=expire * 60)
    # try:
    #     res = send(phone_number, session_code, code, **result.params)
    #     if not res:
    #         return fail(msg='短信接口错误')
    #     res = res.SendStatusSet
    #     if res[0].Code != 'Ok':
    #         print("短信发送失败！", res[0].Message)
    #         return fail(msg="短信发送失败，请稍后再试或者更换手机号！")
    #     print(res)
    #     await redis.set(name=f"code_{phone_number}", value=code, ex=expire * 60)
    #     return success(msg=f"短信已经发送，{expire} 分钟内有效。", data=expire * 60)
    # except TencentCloudSDKException as err:
    #     return fail(msg="短信接发生错误!", data=err.message)


async def check_code(req: Request, verify_code: str, phone: str):
    """
    短信验证码校验
    :param req:
    :param verify_code:
    :param phone:
    :return:
    """
    # 获取redis中的验证码
    redis: Redis = await req.app.state.cache
    code = await redis.get(f"code_{phone}")
    # 比对验证码
    if code and verify_code == code:
        await redis.delete(f"code_{phone}")
        return True
    # 获取缓存中验证码
    return False
