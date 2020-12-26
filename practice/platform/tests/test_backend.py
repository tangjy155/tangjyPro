from datetime import datetime

import requests


def test_testcase():
    testcase_url = 'http://127.0.0.1:5000/testcase'
    r = requests.post(
        testcase_url,
        json={
            'name': f'case1 {datetime.now().isoformat()}',
            'description': 'description 1',
            'steps': ['1', '2', '3']
        }
    )

    assert r.status_code == 200

    r = requests.get(testcase_url)
    print(r.json())
    assert r.json()['body']


def test_testcase_relate_task():
    testcase_url = 'http://127.0.0.1:5000/testcase'
    r = requests.post(
        testcase_url,
        json={
            'name': f'case2 {datetime.now().isoformat()}',
            'description': 'description 2',
            'steps': ['1', '2', '3'],
            'task_id': 1
        }
    )

    assert r.status_code == 200

    r = requests.get(testcase_url)
    print(r.json())
    assert r.json()['body']


def test_task():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.post(
        task_url,
        json={
            'name': f'task {datetime.now().isoformat()}',
            'description': 'task description'
        }
    )

    assert r.status_code == 200

    r = requests.get(task_url)
    print(r.json())
    assert r.json()['body']


def test_task_update():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.post(
        task_url,
        json={
            'id': 1,
            'name': f'task {datetime.now().isoformat()}',
            'description': 'task description update 111'
        }
    )

    assert r.status_code == 200

    r = requests.get(task_url)
    print(r.json())
    assert r.json()['body']


def test_task_del():
    task_url = 'http://127.0.0.1:5000/task?id=1'
    r = requests.delete(task_url)
    print(r.json())
    assert r.status_code == 200


def test_task_relate_cases():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.post(
        task_url,
        json={
            'name': f'task2 {datetime.now().isoformat()}',
            'description': 'task description 2',
            'cases':[1,2,3]
        }
    )

    assert r.status_code == 200

    r = requests.get(task_url)
    print(r.json())
    assert r.json()['body']
