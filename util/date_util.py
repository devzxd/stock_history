# -*- coding: utf-8 -*-
import time


def get_date_str(timestamp, fmt="%Y-%m-%d"):
    """
    时间戳转字符串
    :param timestamp: 时间戳（毫秒）
    :param fmt: 需要转换的时间类型
    :return:
    """
    timeStamp = timestamp / 1000
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime(fmt, timeArray)
    return otherStyleTime


def is_after(now, flag='2016-01-01 00:00:00'):
    """
    判断输入的时间戳是否在规定时间之后
    :param now: 时间戳
    :param flag: 规定的时间
    :return:
    """
    # 将其转换为时间数组
    timeArray = time.strptime(flag, "%Y-%m-%d %H:%M:%S")

    # 转换为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp <= int(now) / 1000
