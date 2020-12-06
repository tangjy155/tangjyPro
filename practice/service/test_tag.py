# -*- coding: utf-8 -*-
# @Author   : tangjy
# @File     : test_tag.py
import json

import allure
from jsonpath import jsonpath
import pytest
from hamcrest import *

# todo: 代码冗余
# todo: 与底层框架耦合太多
# todo: 封装层次不足，不利于管理
# 课后作业：丰富标签管理的测试用例，主要是list add delete接口，拔高点完善下数据清理的过程
from practice.service.tag import Tag


class TestTag:
    def setup_class(self):
        print("\n============= setup_class ============= ")
        self.tag = Tag()
        self.tag.get_token()
        # todo：数据清理的过程，把测试数据清空或者还原
        # 获取所有 list 中 group_id
        r = self.tag.list()
        for group in r.json()['tag_group']:
            # 依据 group_id 清空
            self.tag.delete(group_ids=group['group_id'])
        self.tag.list()
        # 数据准备
        # 用于测试add
        self.tag.add('group_addFail_1205', [{'name': 'tag_addFail_1205'}])
        # 用于测试delete
        self.tag.add('group_delete_1205',
                     [{'name': 'tag_delete_1205_1'}, {'name': 'tag_delete_1205_2'}, {'name': 'tag_delete_1205_3'}])
        self.tag.add('group_delete_1205_1',
                     [{'name': 'tag_delete_1205_4'}, {'name': 'tag_delete_1205_5'}, {'name': 'tag_delete_1205_6'}])
        self.tag.add('group_delete_1205_2',
                     [{'name': 'tag_delete_1205_7'}, {'name': 'tag_delete_1205_8'}, {'name': 'tag_delete_1205_9'}])
        self.tag.add('group_delete_1205_3',
                     [{'name': 'tag_delete_1205_10'}, {'name': 'tag_delete_1205_11'}, {'name': 'tag_delete_1205_12'}])

    @allure.feature('测试获取所有的tag list')
    def test_tag_list_all(self):
        print("\n============= test_tag_list_all ============= ")
        # 获取全部 list
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @allure.feature('测试通过tag id获取 tag list')
    @pytest.mark.parametrize('tag_names', [
        ['tag_delete_1205_1'],      # 测试单个tag_id获取list
        ['tag_delete_1205_4', 'tag_delete_1205_7', 'tag_delete_1205_10']    # 测试多个tag id 获取list
    ])
    def test_tag_list(self, tag_names):
        print("\n============= test_tag_list ============= ")
        r = self.tag.list()
        # 通过tag name 找 tag id
        tag_ids = [jsonpath(r.json(), f'$..[?(@.name=="{name}")].id')[0] for name in tag_names]

        # 通过tag_id 获取tag list
        r = self.tag.list(tag_ids)

        assert r.json()['errcode'] == 0
        # 验证通过tag_id 获取的列表与查询的一致
        assert sorted(jsonpath(r.json(), '$..id')) == sorted(tag_ids)

    @allure.feature('测试获取tag id不存在的 tag list')
    @pytest.mark.parametrize('tag_ids', [
        ['tag_notExist_1205'],
        ['tag_notExist_1205_1', 'tag_notExist_1205_2']
    ])
    def test_tag_list_fail(self, tag_ids):
        print("\n============= test_tag_list_fail ============= ")
        r = self.tag.list(tag_ids)
        assert r.status_code == 200
        assert r.json()['errcode'] == 40068

        r = self.tag.list()
        for id in tag_ids:
            assert id not in jsonpath(r.json(), '$..id')

    @allure.feature('测试添加tag group')
    @pytest.mark.parametrize('group_name, tag_names', [
        ['group_demo_1201', [{'name': 'tag_demo_1201'}]],
        ['group_demo_1202', [{'name': 'tag_demo_1202'}, {'name': 'tag_demo_1203'}]],
        ['group_demo_1205_12345678901234', [{'name': 'tag_demo_1205_1234567890123456'}]],  # group name, tag name 均30字符
        ['~`!@#$%^&*()-_=+[]{}', [{'name': '~`!@#$%^&*()-_=+[]{}'}, {'name': '\\|;:\'",.<>/?'}]],   # 特殊字符
        ['\\|;:\'",.<>/?', [{'name': '~`!@#$%^&*()-_=+[]{}'}, {'name': '\\|;:\'",.<>/?'}]]
    ])
    def test_tag_add(self, group_name, tag_names):
        print("\n============= test_tag_add ============= ")
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        r = self.tag.list()
        assert r.json()['errcode'] == 0

        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [tag['name'] for tag in group['tag']]
        names = [tag['name'] for tag in tag_names]
        assert group['group_name'] == group_name
        assert sorted(tags) == sorted(names)

    @allure.feature('测试添加tag group 失败')
    @pytest.mark.parametrize('group_name, tag_names', [
        ['group_addFail_1205', [{'name': 'tag_addFail_1205'}]],  # 存在 group name 同名
        ['group_addFail_1205_12345678901_', [{'name': 'tag_addFail_1205_1234567890123'}]],  # group name 超过30字符
        ['group_addFail_1205_12345678901_1234567890', [{'name': 'tag_addFail_1205_1234567890124'}]],
        ['group_addFail_1205_12345678901', [{'name': 'tag_addFail_1205_1234567890123_'}]],  # tag name 超过30字符
        ['group_addFail_1205_12345678901', [{'name': 'tag_addFail_1205_1234567890123_1234567890'}]],
        ['', [{'name': 'tag_addFail_1205'}]],      # group name 为空
        ['group_addFail_1205', []],                # tag name 为空
    ])
    def test_tag_add_fail(self, group_name, tag_names):
        print("\n============= test_tag_add_fail ============= ")
        r = self.tag.list()
        names_before = jsonpath(r.json(), '$..name')

        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] >= 40058

        r = self.tag.list()
        names_after = jsonpath(r.json(), '$..name')
        # 验证添加失败前后，获取到的tag name list一致
        assert sorted(names_after) == sorted(names_before)

    @allure.feature('测试通过group id删除')
    @pytest.mark.parametrize('group_names', [
        ['group_delete_1205'],
        ['group_delete_1205_1'],
        ['group_delete_1205_2', 'group_delete_1205_3']
    ])
    def test_tag_del_group(self, group_names):
        print("\n============= test_tag_del_group ============= ")
        # 通过group id 删除
        r = self.tag.list()
        # 通过group name 找 group id
        group_ids = [jsonpath(r.json(), f'$..[?(@.group_name =="{name}")].group_id') for name in group_names]

        self.tag.delete(group_ids=group_ids)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # 验证被删除的group 不存在
        r = self.tag.list()
        assert {jsonpath(r.json(), f'$..[?(@.group_id=="{id}")') for id in group_ids} == {False}

    @allure.feature('测试通过tag id删除')
    @pytest.mark.parametrize('group_names', [
        ['group_delete_1205'],
        ['group_delete_1205_1'],
        ['group_delete_1205_2', 'group_delete_1205_3']
    ])
    def test_tag_del_tag(self, group_names):
        print("\n============= test_tag_del_tag ============= ")
        # 通过tag id 删除
        r = self.tag.list()
        # 通过group name 找 tag id第一个
        tag_ids = [jsonpath(r.json(), f'$..[?(@.group_name=="{name}")].tag[0].id') for name in group_names]

        r = self.tag.delete(tag_ids=tag_ids)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # 验证被删除的tag id不存在
        r = self.tag.list()
        assert {jsonpath(r.json(), f'$..[?(@.id=="{id}")') for id in tag_ids} == {False}

    @pytest.mark.parametrize('group_ids, tag_ids', [
        [None, None],
        [['group_deleteFail_1205'], None],
        [['group_deleteFail_1205_1', 'group_deleteFail_1205_2'], None],
        [None, ['tag_deleteFail_1205']],
        [None, ['tag_deleteFail_1205_1', 'tag_deleteFail_1205_2']],
    ])
    def test_tag_del_fail(self, group_ids, tag_ids):
        print("\n============= test_tag_del_fail ============= ")
        r = self.tag.list()
        list_before = r.json()

        r = self.tag.delete(group_ids, tag_ids)
        assert r.status_code == 200
        # assert r.json()['errcode'] >= 40068
        assert_that(r.json()['errcode'], any_of(equal_to(40068), equal_to(41017)))
        # 验证删除失败前后的 list 一致
        r = self.tag.list()
        assert r.json() == list_before


