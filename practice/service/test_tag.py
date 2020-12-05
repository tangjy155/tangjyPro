# -*- coding: utf-8 -*-
# @Author   : tangjy
# @File     : test_tag.py
import json

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
            self.tag.delete(group['group_id'])
        self.tag.list()
        # 数据准备
        # 用于测试add
        self.tag.add('group_addFail_1205', [{'name': 'tag_addFail_1205'}])
        # 用于测试delete
        self.tag.add('group_delete_1205',
                     [{'name': 'tag_delete_1205_1'}, {'name': 'tag_delete_1205_2'}, {'name': 'tag_delete_1205_3'}])
        self.tag.add('group_delete_1205_1',
                     [{'name': 'tag_delete_1205_1'}, {'name': 'tag_delete_1205_2'}, {'name': 'tag_delete_1205_3'}])
        self.tag.add('group_delete_1205_2',
                     [{'name': 'tag_delete_1205_1'}, {'name': 'tag_delete_1205_2'}, {'name': 'tag_delete_1205_3'}])
        self.tag.add('group_delete_1205_3',
                     [{'name': 'tag_delete_1205_1'}, {'name': 'tag_delete_1205_2'}, {'name': 'tag_delete_1205_3'}])

    def test_tag_list(self):
        print("\n============= test_tag_list ============= ")
        # todo: 完善功能测试
        # 获取全部list
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        # 通过tag_id 获取tag list
        tag_ids:list =[]
        for group in r.json()['tag_group']:
            for tag in group['tag']:
                tag_ids.append(tag['id'])

        r = self.tag.list(tag_ids)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        #
        tag_ids_actual: list = []
        for group in r.json()['tag_group']:
            for tag in group['tag']:
                tag_ids_actual.append(tag['id'])
        assert sorted(tag_ids_actual) == sorted(tag_ids)

    @pytest.mark.parametrize('tag_ids', [
        ['tag_notExist_1205'],
        ['tag_notExist_1205_1', 'tag_notExist_1205_2']
    ])
    def test_tag_list_fail(self, tag_ids):
        print("\n============= test_tag_list_fail ============= ")
        r = self.tag.list(tag_ids)
        assert r.status_code == 200
        assert r.json()['errcode'] == 40068

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
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [tag['name'] for tag in group['tag']]
        names = [tag['name'] for tag in tag_names]
        print(group)
        print(tags)
        print(tag_names)
        print(names)
        assert group['group_name'] == group_name
        assert sorted(tags) == sorted(names)

    @pytest.mark.parametrize('group_name, tag_names', [
        ['group_addFail_1205', [{'name': 'tag_addFail_1205'}]],  # 存在 group name 同名
        ['group_addFail_1205_12345678901_', [{'name': 'tag_addFail_1205_1234567890123'}]],  # group name 超过30字符
        ['group_addFail_1205_12345678901_1234567890', [{'name': 'tag_addFail_1205_1234567890123'}]],
        ['group_addFail_1205_12345678901', [{'name': 'tag_addFail_1205_1234567890123_'}]],  # tag name 超过30字符
        ['group_addFail_1205_12345678901', [{'name': 'tag_addFail_1205_1234567890123_1234567890'}]],
        ['', [{'name': 'tag_addFail_1205'}]],      # group name 为空
        ['group_addFail_1205', []],                # tag name 为空
    ])
    def test_tag_add_fail(self, group_name, tag_names):
        print("\n============= test_tag_add_fail ============= ")
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()['errcode'] >= 40058

    @pytest.mark.parametrize('group_names', [
        ['group_delete_1205'],
        ['group_delete_1205_1'],
        ['group_delete_1205_2', 'group_delete_1205_3']
    ])
    def test_tag_del(self, group_names):
        print("\n============= test_tag_del_group ============= ")
        # 通过tag id 删除
        r = self.tag.list()
        tag_ids:list = []
        for group_name in group_names:
            for group in r.json()['tag_group']:
                if group['group_name'] == group_name:
                    tag_ids.append(group['tag'][0]['id'])

        print(f"tag_ids {tag_ids}")
        r = self.tag.delete(tag_ids=tag_ids)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # 验证被删除的tag id不存在
        r = self.tag.list()
        tag_ids_actual:list =[]  # 删除后剩下的tag id
        for group_name in group_names:
            for group in r.json()['tag_group']:
                if group['group_name'] == group_name:
                    for tag in group['tag']:
                        tag_ids_actual.append(tag['id'])
        print(f"tag_ids_actual {tag_ids_actual}")
        for id in tag_ids:
            for id_actual in tag_ids_actual:
                assert id_actual != id

        # 通过group id 删除
        r = self.tag.list()
        group_ids:list = []
        for group_name in group_names:
            for group in r.json()['tag_group']:
                if group['group_name'] == group_name:
                    group_ids.append(group['group_id'])
        print(f"tag_ids_actual {tag_ids_actual}")
        self.tag.delete(group_ids=group_ids)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # 验证被删除的group 不存在
        r = self.tag.list()
        for id in group_ids:
            for group in r.json()['tag_group']:
                assert group['group_id'] != id

    @pytest.mark.parametrize('group_ids, tag_ids', [
        [[], []],
        [['group_deleteFail_1205'], []],
        [['group_deleteFail_1205_1', 'group_deleteFail_1205_2'], []],
        [[], ['tag_deleteFail_1205']],
        [[], ['tag_deleteFail_1205_1', 'tag_deleteFail_1205_2']],
    ])
    def test_tag_del_fail(self, group_ids, tag_ids):
        print("\n============= test_tag_del_fail ============= ")
        # 验证group id不存在
        r = self.tag.list()
        for id in group_ids:
            for group in r.json()['tag_group']:
                assert group['group_id'] != id
        # 验证 tag id 不存在
        for id in tag_ids:
            for group in r.json()['tag_group']:
                for tag in group['tag']:
                    assert tag['id'] != id

        r = self.tag.delete(group_ids, tag_ids)
        assert r.status_code == 200
        # assert r.json()['errcode'] >= 40068
        assert_that(r.json()['errcode'], any_of(equal_to(40068), equal_to(41017)))


