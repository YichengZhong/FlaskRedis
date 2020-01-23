from flask import Flask
import sys
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Test'

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