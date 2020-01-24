from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
import os
import click
app = Flask(__name__)

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
    Info = db.Column(db.String(128),nullable=True) #入库内容

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