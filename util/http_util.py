# -*- coding: utf-8 -*-

"http工具"
import logging

import requests
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def get_history_list(stock_code):
    """

    :param stock_code: 股票代码
    :return: 股票历史数据
    """

    url = 'https://www.asx.com.au/asx/1/chart/highcharts?asx_code=' + stock_code
    logging.info("获取历史数据开始，股票代码：%s", stock_code)
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        result = resp.text
        logging.info("%s 股票历史结果：%s", stock_code, result)
        return resp.text
    except Exception as e:
        # 将异常打印，返回None
        logging.exception(e)
        return None

