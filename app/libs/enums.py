from enum import Enum


class ClientTypeEnum(Enum):     # 创建枚举类型, 访问方式ClientTypeEnum.USER_MOBILE
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
