# -*- coding: utf-8 -*-

"主程序，获取股票代码，抓取股票历史数据，将数据处理之后放入excel中"
import logging
import os

from util.date_util import is_after, get_date_str
from util.excel_util import ExcelUtil
from util.http_util import get_history_list

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def get_code_list():
    """

    :return: 股票代码列表
    """
    with open(os.path.join(os.path.abspath('../'), 'util/stock_code'), 'r') as f:
        # 读取文件内容去除换行符，按','分割
        result = f.read().replace('\n', '').split(',')
        logging.info("股票代码列表：%s", result)
        return result


def get_data(history):
    """
    获取有效数据
    :param history: 历史数据列表
    :return:
    """

    result = []
    for stock in list(eval(history)):
        info = []
        if not is_after(stock[0]):
            # 时间不符合要求，判断下一个
            continue
        # 将时间戳传转为时间字符串
        info.append(get_date_str(stock[0]))
        # 价格
        info.append(stock[1])
        result.append(info)
    return result


if __name__ == '__main__':
    # 新建excel文件
    book = ExcelUtil('stock_history_data')
    # 获取股票代码
    stock_code_list = get_code_list()
    # 循环处理股票数据
    for code in stock_code_list:
        try:
            # 获取股票历史数据
            history = get_history_list(code)
            if history is None:
                # 股票历史数据为空，直接获取下一只股票信息
                logging.info("股票历史信息为空！股票代码：%s", code)
                # 创建一个空的sheet
                book.create_sheet(code)
                continue

            # 获取有效数据
            data = get_data(history)
            # 存入excel
            book.create_sheet(code, data)
            logging.info("%s 数据处理完成！", code)
        except Exception as e:
            logging.exception(e)

    logging.info("======================任务完成==================================")
