from dbm import error

from flask import Blueprint, render_template, request

ac = Blueprint('account', __name__)

@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    #使用request。form。get获取数据,连接数据库，解析校验
    return "ok"
''' 
   import  pymysql
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='bilibili')
    cursor = conn.cursor()
    cursor.execute('select * from user where .....')
    data = cursor.fetchall()#
    cursor.close()
    conn.close()
    if data:
        return "登录成功"
    return render_template( "login.html",error = "登录失败")#"登录失败
'''
ac.route('/user')
def user():
    return "用户列表"

