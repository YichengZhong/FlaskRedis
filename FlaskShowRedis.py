from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
app = Flask(__name__)

#尝试本地sqlite数据显示

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