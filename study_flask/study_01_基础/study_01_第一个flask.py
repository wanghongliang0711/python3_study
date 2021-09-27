"""
@author: wanghongliang
@file: study_01_第一个flask.py
@time: 2021/7/16 13:51 
"""
from flask import Flask, render_template, request

# 创建Flask应用程序实例
# 需要出入__name__， 作用是为了确定资源所在的路径
app = Flask(__name__)


# 路由默认只支持GET，如果需要增加，需要自行指定 methods
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'hello world, my dream'


# 使用同一个视图函数，来显示不同用户的订单信息
# <>定义路由的参数， <>内需要起个名字
# @app.route('/orders/<order_id>')
@app.route('/orders/<float:order_id>')  # 对参数类型进行限定，默认是字符串。此时输入字符串，提示 Not Found
# @app.route('/orders/<int:order_id>')  # 对参数类型进行限定，默认是字符串。此时输入字符串，提示 Not Found
def get_order_id(order_id):
    # 需要在视图函数的() 内填入参数名，那么后面的代码才能使用
    return 'order_id %s' % order_id

@app.route('/jinji2', methods=['GET', 'POST'])
def hello_jinji2():
    url_str = 'https://www.baidu.com/'
    url_str1 = 'https://www.csdn.net/'
    return render_template('index.html', url_str=url_str, url_str1=url_str1)


@app.route('/get_args')
def args_get():
    arg = request.args.get("test")
    print(arg)
    print(request.args)
    disable = request.args.get("disable", "morenzhi ", type = str)
    '''
    获取get请求中的disable参数
    指定disable的默认值
    指定disable的类型
    '''
    print(disable)
    return arg



@app.route('/post_args', methods=['POST'])
def args_post():
    if request.method == 'POST':
        print(request)
        print(request.form)
        print('test' in request.form)
        print(request.form['test'])
        print(request.form['name'])
        return request.form['name']


@app.route('/post_args_json', methods=['POST'])
def args_post_json():
    if request.method == 'POST':
        print(request)
        print("request.data", request.data)
        print("request.json", request.json)
        print("request.args", request.args)
        print("request.form", request.form)
        print("request.headers", request.headers)
        # print(request.get_json())
        print(type(request.get_json()))

        return "request.get_json()"


if __name__ == '__main__':
    app.run()
