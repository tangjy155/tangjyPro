# -*- coding: utf-8 -*-
# @Author   : tangjy
# @File     : tag.py

import json

import requests

corpid = 'ww65dc6d7815f33b43'
corpsecret = '1FGElXsNlKx7rN4oKLUKcS962j6g09c9xlUb6gWc-wQ'

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888',
}

class Tag:

    def __init__(self):
        self.token = ""

    def get_token(self):
        r = requests.get(
            ' https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        print(json.dumps(r.json(), indent=2))
        self.token = r.json()['access_token']

    def list(self, tag_ids=[]):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={
                'tag_id': tag_ids
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def add(self, group_name, tags):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                'group_name': group_name,
                'tag': tags
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete(self, group_ids=None, tag_ids=None):
        if tag_ids is None:
            json_data = {
                'group_id': group_ids
            }
        elif group_ids is None:
            json_data = {
                'tag_id': tag_ids
            }

        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json=json_data
            # proxies=proxies,
            # verify=False
        )
        print(json.dumps(r.json(), indent=2))
        return r