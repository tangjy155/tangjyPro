# -*- coding: utf-8 -*-
# @time     : 2020/10/27 09:51
# @Author   : tangjy
# @File     : files_info.py

import os
import win32api
import xlsxwriter


# 获取文件详细信息
def get_file_properties(file_name):
    prop_names = ('Comments', 'InternalName', 'ProductName',
                  'CompanyName', 'LegalCopyright', 'ProductVersion',
                  'FileDescription', 'LegalTrademarks', 'PrivateBuild',
                  'FileVersion', 'OriginalFilename', 'SpecialBuild')

    props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

    try:
        fixed_info = win32api.GetFileVersionInfo(file_name, '\\')
        props['FixedFileInfo'] = fixed_info
        props['FileVersion'] = "%d.%d.%d.%d" % (fixed_info['FileVersionMS'] / 65536,
                                                fixed_info['FileVersionMS'] % 65536,
                                                fixed_info['FileVersionLS'] / 65536,
                                                fixed_info['FileVersionLS'] % 65536)

        # \VarFileInfo\Translation returns list of available (language, codepage)
        # pairs that can be used to retreive string info. We are using only the first pair.
        lang, codepage = win32api.GetFileVersionInfo(file_name, '\\VarFileInfo\\Translation')[0]

        # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
        # two are language/codepage pair returned from above

        str_info = {}
        for propName in prop_names:
            str_info_path = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
            # print str_info
            str_info[propName] = win32api.GetFileVersionInfo(file_name, str_info_path)

        props['StringFileInfo'] = str_info

    except:
        pass

    return props


# 获取文件夹下所有文件的版本信息
def get_files_version(file_dir):
    files_version = []

    # 递归获取路径下文件、文件夹
    for root, dirs, files in os.walk(file_dir):
        # print(root)   # 当前路径
        # print(dirs)   # 所有子目录
        # print(files)  # 所有文件
        print()

        for file in files:
            # stat_info = os.stat(root + "\\" + file)
            # print (stat_info)

            file_string_info = get_file_properties(root + "\\" + file)["StringFileInfo"]
            # print(file_string_info)
            file_version = []
            file_version.append(file)

            if file_string_info:
                print(file + "--- : " + file_string_info["ProductVersion"])
                file_version.append(file_string_info["ProductVersion"])

            files_version.append(file_version)

    return files_version

# 写入excel文件
def write_into_excel(title, files_version, excel_file):
    workbook = xlsxwriter.Workbook(excel_file)        # 创建一个excel文件
    worksheet = workbook.add_worksheet()      # 创建一个sheet

    row = 0    # 定义要插入的列
    for i in title:
        worksheet.write(0, row, i)
        row += 1

    line = 1    # 定义要插入的行，1 是第二行
    for info in files_version:
        row = 0
        for unit in info:
            # 写入数据：行、列、数据
            worksheet.write(line, row, unit)
            row += 1
        line += 1

    # 保存
    workbook.close()


if __name__ == "__main__":
    # get_files_version("F:\\03windows集控测试\\云桌面优化升级文件")

    title = {'文件名', '版本号'}
    write_into_excel(title,
                     get_files_version("F:\\03windows集控测试\\云桌面优化升级文件"),
                     "update_20201030.xlsx")