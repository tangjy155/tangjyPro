# -*-coding:utf-8-*-

# ===============================================================================
# 目录对比工具(包含子目录 )，并列出
# 1、A比B多了哪些文件
# 2、B比A多了哪些文件
# 3、二者相同的文件: md5比较
# ===============================================================================

import os
import time


def get_file_mtime(filename):
    if not os.path.isfile(filename):
        print('file not exist: ' + filename)
        return

    return time.ctime(os.stat(filename).st_mtime)


def get_all_files(path):
    flist = []
    for root, dirs, fs in os.walk(path):
        for f in fs:
            f_fullpath = os.path.join(root, f)
            f_relativepath = f_fullpath[len(path):]

            f.lower()
            is_file = lambda x: any(x.endswith(extension)
                                    for extension in ['dll', 'ini', 'crt','config','xml','dat','lib','exe','ico','sys'])
            if is_file(f):
                flist.append(f_relativepath)

    return flist


def update_compare(new_path, old_path):
    new_files = get_all_files(new_path)
    old_files = get_all_files(old_path)
    diff_files = []  # {'FileName': None, 'Path': None, 'NewTime': None, 'OldTime': None}

    set_new = set(new_files)
    set_old = set(old_files)

    # 处理共有文件
    common_files = set_new & set_old

    for f in sorted(common_files):
        new_time = get_file_mtime(new_path + '\\' + f)
        old_time = get_file_mtime(old_path + '\\' + f)
        if new_time != old_time:
            # print("dif file: %s" % (f))
            file_info = {'FileName': f, 'Path': None, 'NewTime': new_time, 'OldTime': old_time}

            diff_files.append(file_info)
            print(file_info)

    # 处理仅出现在一个目录中的文件
    only_files = set_new ^ set_old
    only_in_new = []
    only_in_old = []
    for of in only_files:
        if of in new_files:
            only_in_new.append(of)
        elif of in old_files:
            only_in_old.append(of)

        file_info = {'FileName': of, 'Path': None, 'NewTime': new_time, 'OldTime': old_time}

        diff_files.append(file_info)
        print(file_info)

    # sorted(diff_files, key=lambda i: (i['Path'], i['FileName']))
    # print(diff_files)


    # if len(only_in_new) > 0:
    #     print('-' * 20, "only in ", new_path, '-' * 20)
    #     for of in sorted(only_in_new):
    #         print(of)
    #
    # if len(only_in_old) > 0:
    #     print('-' * 20, "only in ", old_path, '-' * 20)
    #     for of in sorted(only_in_old):
    #         print(of)


if __name__ == '__main__':
    new_path = "F:\\tmp\\网云集中管控系统_new"
    old_path = "F:\\tmp\\网云集中管控系统_old"
    update_compare(new_path, old_path)
    print("\ndone!")

