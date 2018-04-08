# -*- coding: utf-8 -*-
import xdrlib, sys
import xlrd


def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)

        # 根据索引获取Excel表格中的数据


# 参数：file: Excel文件路径
#      colnameindex: 表头列名所在行的索引
#      by_index: 表的索引

def excel_table_byindex(file='file.xls', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)  # 以列表格式输出
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)  # 向列表中插入字典类型的数据
    return list


def main():
    tables = excel_table_byindex(file='test.xls')
    for row in tables:
        print row


if __name__ == "__main__":
    main()