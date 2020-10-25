# -*- coding: utf-8 -*-
# @Time     : 2020/10/25 19:10
# @Author   : tangjy
# @File     : student_oop.py


class Student:
    def __init__(self, name, age, grade, stu_no):
        self._name = name        # 名字
        self._age = age          # 年龄
        self._grade = grade      # 年级
        self._stu_no = stu_no    # 学号

    # 获取学生信息
    def show_info(self):
        print(f"我的名字是{self._name}，{self._age}岁，大学{self._grade}年级")

    # 修改学生信息
    def change_info(self, grade, stu_no):
        self._grade = grade
        self._stu_no = stu_no

    # 获取学生分数
    def get_score(self, filename):
        try:
            # 读取文件数据
            with open(filename) as f:
                # 一次读一行数据
                data = f.readline()
                while data:
                    temp_score = data.strip().split(",")

                    score = []
                    # 如果当前行学生姓名是自己的名字，则获取到分数，并直接返回结果
                    if temp_score.pop(0) == self._name:
                        while temp_score:
                            score.append(temp_score.pop(0))
                        return score

                    # 继续读取下一行数据
                    data = f.readline()
        except IOError as io_error:
            print(f"file error: {str(io_error)}")
            return None


if __name__ == "__main__":
    zs = Student("zs", 18, 1, "12345678")
    zs.show_info()

    zs.change_info(2,"87654321")
    zs.show_info()
    print(f"张三的成绩为：{zs.get_score('students_score.dat')}")

    ls = Student("ls", 18, 2, "12345677")
    ls.show_info()
    print(f"李四的成绩为：{ls.get_score('students_score.dat')}")
