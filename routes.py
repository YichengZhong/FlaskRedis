from __init__ import app
from flask import render_template
@app.route("/")
def index():
    user = {'username': '开发人员'}
    # 日志由一个列表组成，其中里面包含两个字典，里面各有author和content字段
    posts = [
        {
            'author': {'username': 'EMS表'},
            'content': ['字段1','字段2']
        },
        {
            'author': {'username': '配置表'},
            'content': ['字段1','字段2','字段3']
        }
    ]
    return render_template('index.html', title='HomePage', html_user=user, html_posts=posts)