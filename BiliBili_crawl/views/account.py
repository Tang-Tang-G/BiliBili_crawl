from utils import db
from flask import Blueprint, render_template, request

ac = Blueprint('account', __name__)

@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    #使用request。form。get获取数据,连接数据库，解析校验
    role = request.form.get('role')
    mobile = request.form.get('mobile')
    pwd = request.form.get('pwd')
    print(role,mobile,pwd)
    data = db.fetch_login("select * from bilbili where mobile =%s and pwd =%s",[mobile,pwd])
    if data:
        return "登录成功"
    return render_template( "login.html",error = "登录失败")#"登录失败

ac.route('/user')
def user():
    return "用户列表"

