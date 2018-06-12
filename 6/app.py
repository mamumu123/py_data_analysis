from flask import Flask, render_template, request, url_for, jsonify, json, redirect, session
from flask_bootstrap import Bootstrap
import db
import cal

app = Flask(__name__)
app.secret_key = '\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'
Bootstrap(app)


# 主页
@app.route('/', methods=['POST', 'GET'])
def index():
    username = session.get('username')
    # 如果还没有登录，就返回登录页面
    if username == None:
        return redirect(url_for('login'))
    # 从数据库中获取展示数据
    data = db.show()
    return render_template('index.html', all_message=data)


# 登陆
@app.route("/login", methods=["POST", "GET"])
def login():
    # 如果提交，开始处理
    if request.method == 'POST':
        # 提交，即开始验证
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        username = session['username']
        password = session['password']
        result = db.check_user(username, password)
        if result is None:
            return render_template('login.html', errorMessage='此用户名不存在')
        if result[3] != password:
            return render_template('login.html', errorMessage='密码错误')
        # 如果类型为1，即为管理员，重定向到管理员界面
        if result[2] == 1:
            return redirect('admin')
        # 如果类型为0，即为普通用户，重定向到主页
        if result[2] == 0:
            return redirect(url_for('index'))
    # 如果不是提交表单，即打开登录页面
    return render_template('login.html')


# 登出
@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))


# 注册
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        print('正在注册')
        # 提交，即开始验证
        username = request.form['username']
        password = request.form['password']
        result = db.insert_user(username, password)
        return redirect(url_for('login'))
    return render_template('register.html')


# 管理页面
@app.route('/admin', methods=['POST', 'GET'])
def admin():
    username = session.get('username')
    if username == None:
        return redirect(url_for('login'))
    message = db.show()
    print('tbSingle', message['tbSingle'])
    return render_template('admin.html', single=message['tbSingle'])


# 增加单品
@app.route('/admin/insertMenu', methods=['POST', 'GET'])
def admin_insertMenu():
    data = request.get_json()
    dataForm = data.get('dataForm')
    print(dataForm)
    db.insertMenu(dataForm)
    return 'OK'


# 增加套餐
@app.route('/admin/insertMul', methods=['POST', 'GET'])
def admin_insertMul():
    data = request.get_json()
    dataForm = data.get('dataForm')
    db.insertMul(dataForm)
    return 'OK'


# 将单品组合套餐
@app.route('/index/cal_sum', methods=['POST', 'GET'])
def cal_sum():
    data = request.get_json()
    li = data.get('list')
    cal_da = {}
    for per in li:
        # print(per)
        cal_da[per['id']] = per['count']
    # zuhe={}
    cost, zuhe = cal.cal(cal_da)
    target_single, target_min, target_dict = cal.add_cal(cal_da)
    # print('计算中')
    # print('cost', cost)
    # print('zuhe', zuhe)
    tem_s, tem_m = db.query_car(zuhe)
    target_s, target_m = db.query_car(target_dict)
    result = {
        'cost': cost,
        'tem_s': tem_s,
        'tem_m': tem_m,
        'num': zuhe,
        'target_single': target_single,
        'target_min': target_min,
        'target_s': target_s,
        'target_m': target_m,
        'target_num': target_dict
    }

    return json.dumps(result)


# 支付
@app.route('/index/sub_mit', methods=['POST', 'GET'])
def sub_mit():
    data = request.get_json()
    li = data.get('list')
    cost = data.get('cost')
    n_cost = data.get('new_cost')
    db.insertCar(li, cost, n_cost)
    return 'OK'


# 404
@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
