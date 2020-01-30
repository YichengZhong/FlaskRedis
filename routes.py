from __init__ import app      # 从hello包中导入app实例
@app.route("/")               # 使用装饰器对下面的视图函数index进行装饰
def index():
    return "你好，喵星在线！"     # 这里返回的内容，会直接送到浏览器中显示出来