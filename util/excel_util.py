# -*- coding: utf-8 -*-
import os

import time
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import Workbook


def _setWidth(book, count):
    """
    设置单元格宽度
    :param book:
    :param count:
    :return:
    """
    for i in range(count):
        sheet = book.get_sheet(i)
        first_col = sheet.col(0)
        first_col.width = 256 * 20
        second_col = sheet.col(1)
        second_col.width = 256 * 20


class ExcelUtil(object):
    def __init__(self, name="test"):
        self.name = name + ".xls"
        # 防止文件被覆盖，每次新建相同名字文件，需要加时间戳
        if os.path.exists(self.name):
            self.name = name + str(time.time()) + ".xls"
        self._create_excel()

    def _create_excel(self):
        """
        新建excel

        :param name: 文件名字
        :return:excel文件
        """
        wb = Workbook()
        # 默认创建一个sheet
        wb.add_sheet('sheet1')
        wb.save(self.name)

    def create_sheet(self, sheet_name, data=None):
        """
        新建sheet页并插入数据

        :param book: excel
        :param sheet_name: sheet名字
        :param data: 数据
        :return:
        """
        rexcel = open_workbook(self.name)  # 用wlrd提供的方法读取一个excel文件
        count = len(rexcel.sheets())
        book = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
        sheet = book.add_sheet(sheet_name)
        # 设置所有sheet单元格宽度
        _setWidth(book, count + 1)
        if data is None:
            book.save(self.name)
            return
        # 创建title xlwt对象的写方法，参数分别是行、列、值
        sheet.write(0, 0, 'date')
        sheet.write(0, 1, 'price')
        row = 1
        # 填充内容
        for stock in data:
            sheet.write(row, 0, stock[0])
            sheet.write(row, 1, float(stock[1]))
            row += 1
        book.save(self.name)
