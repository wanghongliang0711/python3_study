"""
@author: wanghongliang
@file: dept.py
@time: 2020/7/16 14:11 
"""
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')
data = [
    {
        "id": 1,
        "name": 'MIK',
        "parentId": 0
    }, {
        "id": 2,
        "name": 'wang',
        "parentId": 1
    }, {
        "id": 432774533251235840,
        "name": 'ht',
        "parentId": 1
    }, {
        "id": 432775163952922624,
        "name": 'admin1',
        "parentId": 432774533251235840
    }, {
        "id": 432775489057718272,
        "name": 'admin2',
        "parentId": 432774533251235840
    }, {
        "id": 432776913422385152,
        "name": 'wang22',
        "parentId": 2
    }, {
        "id": 432777032800665600,
        "name": 'admin3',
        "parentId": 2
    }, {
        "id": 432802145368014848,
        "name": 'wanghongli',
        "parentId": 432777032800665600
    }, {
        "id": 432813072719347712,
        "name": 'wanghong',
        "parentId": 432777032800665600
    }
]

@app.route('/')
def hello():
    return "test flask"


@app.route('/dev-api/vue-element-admin/user/info', methods=['GET'])
def hello1():
    data = [
        {
              "deptId": 1,
              "date": '2016-05-02',
              "name": '王小虎',
              "address": '上海市普陀区金沙江路 1518 弄'
            }, {
              "deptId": 2,
              "date": '2016-05-04',
              "name": '王小虎',
              "address": '上海市普陀区金沙江路 1517 弄'
            }, {
              "deptId": 3,
              "date": '2016-05-01',
              "name": '王小虎',
              "address": '上海市普陀区金沙江路 1519 弄',
              "children": [{
                "deptId": 31,
                "date": '2016-05-01',
                "name": '王小虎',
                "address": '上海市普陀区金沙江路 1519 弄'
              }, {
                "deptId": 32,
                "date": '2016-05-01',
                "name": '王小虎',
                "address": '上海市普陀区金沙江路 1519 弄'
              }]
            }, {
              "deptId": 4,
              "date": '2016-05-03',
              "name": '王小虎',
              "address": '上海市普陀区金沙江路 1516 弄'
            }]
    res = {"data" : data}
    return res

@app.route('/dev-api/dept/list', methods=['GET'])
def hello2():
    print("deptName ", request.args.get('deptName'))
    global data
    res = {"data" : data, "code": 20000}
    return res


if __name__ == '__main__':
    app.run('127.0.0.1', '7890')
