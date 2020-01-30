from flask import Flask,request, url_for, redirect, flash,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from sqlalchemy import create_engine
import sys
import os
import time
import click
app = Flask(__name__)

#加个表单

#尝试本地Sqlite实现
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class EMS_Info(db.Model):
    '''
    表名将会是 EMS_Info（自动生成，小写处理）
    '''
    id = db.Column(db.Integer, primary_key=True) # 主键
    time=db.Column(db.String(20),nullable=True) #入库时间
    info = db.Column(db.String(128),nullable=True) #入库内容

class User(db.Model):
    '''
    用户信息存储
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20)) # 用户名
    password_hash = db.Column(db.String(128)) # 密码散列值

    def set_password(self, password): # 用来设置密码的方法，接受密码 作为参数
        self.password_hash = generate_password_hash(password) # 将生成的密码保持到对应字段

    def validate_password(self, password): # 用于验证密码的方法，接 受密码作为参数
        return check_password_hash(self.password_hash, password) # 返回布尔值

@app.route('/insertTestData')
def InitData():
    #db.drop_all()
    db.create_all()
    try:
        for i in range(0,10):
            EMS_Info_temp=EMS_Info(id=i,time=str(time.time()),info=str(i))
            db.session.add(EMS_Info_temp)
        db.session.commit()
        return 'InitData Success'
    except:
        db.session.rollback()
        return 'InitData Failed'

@app.route('/showTestData')
def ShowData():
    str_out="EMS_Info:<br/>"
    EMS_Info_L=EMS_Info.query.all()
    for i in range(0,len(EMS_Info_L)):
        id = EMS_Info_L[i].id
        time = EMS_Info_L[i].time
        info = EMS_Info_L[i].info
        str_out=str_out+str(id)+" "+time+" "+info+"<br/>"
    return str_out

@app.route('/InsertData/<table>/<value>')
def InsertData(table,value):
    '''
    根据表名进行匹配，按照value里面&进行区分
    :param table:
    :param value:
    :return:
    '''
    value_L=str(value).split('&')
    if(len(value_L)!=3):
        return "Value Format is Wrong"

    id = value_L[0]
    time = value_L[1]
    info = value_L[2]

    #插入之前先根据主键查询是否已经存在
    EMS_Info_L = EMS_Info.query.get(int(id))
    if(EMS_Info_L is not None):
        return ('InsertData:%s,Value:%s is Exist' % (table, value))

    EMS_Info_temp = EMS_Info(id=id, time=time, info=info)
    try:
        db.session.add(EMS_Info_temp)
        db.session.commit()
        return ('InsertData:%s,Value:%s Success' % (table, value))
    except:
        db.session.rollback()
        return ('InsertData:%s,Value:%s Failed' % (table, value))

@app.route('/InsertData/<table>/<primarykey>')
def SearchData(table,primarykey):
    '''
    根据主键进行查询
    :param table:
    :param value:
    :return:
    '''
    EMS_Info_L = EMS_Info.query.get(int(primarykey))
    if (EMS_Info_L is None):
        return ('SearchData:%s,Value:%s is Not Exist' % (table, EMS_Info_L))

    str_out = "EMS_Info:<br/>"
    for i in range(0,len(EMS_Info_L)):
        id = EMS_Info_L[i].id
        time = EMS_Info_L[i].time
        info = EMS_Info_L[i].info
        str_out=str_out+str(id)+" "+time+" "+info+"<br/>"
    return str_out

@app.route('/')
def hello():
    return 'Test'

@app.route('/Retrieve/<table>/<value>')
def RetrieveDate(table,value):
    '''
    根据表名查询数据
    :param table: 表名
    :param value: 数据
    :return:
    '''
    return  ('Table:%s,Value:%s' % (table,value))

@app.route('/formtest', methods=['GET', 'POST'])
def formtest():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        str_sql = request.form.get('SQL')  # 传入表单对应输入字段的 name 值
        print(str_sql)
        # 验证数据
        if not str_sql :
            flash('Invalid input.')  # 显示错误提示
            return ('title:is format wrong')

        #执行SQL语句
        str_sql="select * from EMS__info"
        try:
            sql_reslut=db.session.execute(str_sql).fetchall()
            print(sql_reslut, dir(sql_reslut))
            for i in range(0,len(sql_reslut)):
                print(sql_reslut[i])
            db.session.commit()


            return ('SQL execute is Sucess\n')
        except Exception as e:
            db.session.rollback()
            raise e

    return render_template("SQL_Input.html")

@app.route('/syspara')
def getSysPara():
    '''
    显示系统参数
    :return:
    '''
    pythonVersion=sys.version
    return pythonVersion

if __name__ == '__main__':
    app.run()#执行flask的运行