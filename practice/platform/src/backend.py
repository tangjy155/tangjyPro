import json
from typing import List

from flask import app, Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou4:lagou4password@stuq.ceshiren.com:23306/lagou4'

db = SQLAlchemy(app)

# fake db
app.config['db'] = []


@app.route('/')
def hello():
    return 'hello from ceshiren.com'

# 表
class TestCase(db.Model):
    '''
    case(id, name, description, steps, task_id)
    '''
    __tablename__ = 'case_tjy2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    steps = db.Column(db.String(1024), nullable=True)

    task_id = db.Column(db.Integer, db.ForeignKey('task_tjy2.id'), nullable=True)
    task = db.relationship('Task', backref=db.backref('cases', lazy=True))

    def __repr__(self):
        return '<TestCase %r>' % self.name


class Task(db.Model):
    '''
    task(id, name, description)
    '''
    __tablename__ = 'task_tjy2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.name


# 服务
class TestCaseService(Resource):
    def get(self):
        """
        测试用例的浏览获取 /testcase.json /testcase.json?id=1
        """
        testcases:List = []
        print(request.args.get('id'))
        if request.args.get('id') is not None:
            # 指定id 获取 testcase
            testcases.append(TestCase.query.get(request.args.get('id')))
        else:
            # 获取所有testcase
            testcases: List[TestCase] = TestCase.query.all()

        res = [{
            'id': testcase.id,
            'name': testcase.name,
            'description': testcase.description,
            'steps': json.loads(testcase.steps),
            'task_id': testcase.task_id,
            # 'task':json.loads(testcase.task)
        } for testcase in testcases]
        return {
            'body': res
        }

    def post(self):
        """
        上传用例， 更新用例
        /testcase.json  {'name': 'xx', 'description': 'xxx', 'steps': []}
        """
        testcase = TestCase(
            name=request.json.get('name'),
            description=request.json.get('description'),
            steps=json.dumps(request.json.get('steps')),
        )

        if request.json.get('task_id') is not None:
            task = Task.query.get(request.json.get('task_id'))
            if task is None:
                return 'error: task id is not exist'

            testcase.task = task

        db.session.add(testcase)
        db.session.commit()
        return 'ok'


# done: 作业1
# 完成TaskService的功能，基本的增删改查
# 拔高：增加的时候关联TestCase
class TaskService(Resource):
    def get(self):
        '''
        测试任务的获取 /task
        :return: {'taskname' : 'XXX', 'description': 'xxx', 'case_id' : 'xx', 'case' : 'xx'}
        '''
        tasks:List = []
        if request.args.get('id') is not None:
            # 有id，按id查询 task
            task = Task.query.get(request.args.get('id'))
            if task is not None:
                # 查询结果存在
                tasks.append(task)
        else:
            # 无id，则查询所有结果
            tasks = Task.query.all()

        print(tasks)
        if tasks == []:
            return {'body':[]}
        else:
            res = [{
                'id': task.id,
                'name': task.name,
                'description': task.description
            } for task in tasks]
            return {
                'body': res
            }

    def post(self):
        '''
        上传任务，更新任务 /task {'id': 'xxx', taskname' : 'XXX', 'description': 'xxx'}
        :return: status
        '''
        task = None
        if request.json.get('id') is not None and Task.query.get(request.json.get('id')) is not None:
            # task id存在则修改数据库中数据
            task = Task.query.get(request.json.get('id'))
            task.name = request.json.get('name')
            task.description = request.json.get('description')
        else:
            # task id 不存在则新实例化task，添加数据库
            task = Task(
                name=request.json.get('name'),
                description=request.json.get('description')
            )
            db.session.add(task)

        # task 关联 case，可关联多个
        if request.json.get('cases') is not None:
            for id in request.json.get('cases'):
                case = TestCase.query.get(id)
                task.cases.append(case)

        db.session.commit()
        return 'ok'

    def delete(self):
        '''
        删除任务，/task?id=1
        :return: msg
        '''
        if request.args.get('id') is not None and Task.query.get(request.args.get('id')) is not None:
            task = Task.query.get(request.args.get('id'))
            db.session.delete(task)
            db.session.commit()
            return 'ok'
        else:
            return 'error, illegal parameter or record not exist'


class ReportService(Resource):
    def get(self):
        pass


api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskService, '/task')
api.add_resource(ReportService, '/report')

if __name__ == '__main__':
    app.run(debug=True)
