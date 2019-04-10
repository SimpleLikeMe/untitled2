# 导入Flask获取app对象，模板模块用于联系templates下的html文件,request与请求有关的处理,重定向redirect
from flask import Flask, render_template, request, redirect, make_response
from orm import ormmanage

# 用当前模块__name__创建app对象
app = Flask(__name__)


@app.route("/")
def index():
    # 主页处理逻辑
    # 将系统首页渲染出来
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # 用户登录逻辑处理
    if request.method == "GET":
        return render_template("/login.html")
    elif request.method == "POST":
        # 获取表单数据

        account = request.form["account"]
        password = request.form["password"]
        if account and ormmanage.check_user(account=account, password=password):
            # 若用户输入的账号密码正确,跳转到用户主页
            res = make_response(redirect("/user_home"))
            user = ormmanage.query_user(account)
            res.set_cookie("account", account)
            res.set_cookie("user_name", user.name)
            return res
        else:
            # 登录失败
            print("登录失败")
            return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """用户登录逻辑处理"""
    if request.method == "GET":
        return render_template("/login.html")

    elif request.method == "POST":
        # 获取表单输入的数据
        account = request.form["account"]
        password = request.form["password"]
        # 验证用户合法性
        if account and not ormmanage.query_user(account):
            # 账号在数据库中不存在，将用户插入数据库
            print("注册成功")
            ormmanage.insert_user(account=account, password=password)
            # 将页面跳转到系统首页
            return redirect("/")

        else:
            print("注册失败")
            return render_template("/login.html")


@app.route("/user_home")
def user_home():
    """用户主页逻辑处理"""
    # 查询数据库获取记录列表
    article_list = ormmanage.query_article_all()
    user_name = request.cookies.get("user_name")
    return render_template("user_home.html", user_name=user_name, article_list=article_list)


@app.route("/record_list")
def record_list():
    # 查询数据库获取记录列表
    record_list = ormmanage.query_record_all()
    if record_list:
        return render_template("user_home.html", record_list=record_list)
    else:
        render_template("user_home.html", record_list=record_list)


@app.route("/detail/<id>")
def detail(id):
    """详情页面"""
    article = ormmanage.query_article_one(id)
    article.read_count += 1
    ormmanage.session.commit()
    return render_template("detail.html", article=article)


@app.route("/publish", methods=["GET", "POST"])
def publish():
    if request.method == "GET":
        return render_template("publish.html")
    elif request.method == "POST":
        # 获取表单内容
        title = request.form["title"]
        content = request.form["content"]
        # 获取当前用户的id
        account = request.cookies.get("account")
        # 将文章写入数据库
        ormmanage.insert_article(title=title, user_id=account, content=content)
        return redirect("/user_home")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
        return render_template("update.html")
    elif request.method == "POST":

        content = request.form["content"]
        # 将文章写入数据库
        ormmanage.update_record_one(id=id, content=content)
        return redirect("/user_home")


@app.route("/delete_article/<int:id>")
def delete_article(id):
    ormmanage.del_article(id)
    article_list = ormmanage.query_article_all()
    user_name = request.cookies.get("user_name")
    return render_template("manage_article.html", user_name=user_name, article_list=article_list)


@app.route("/manage_article")
def manage_article():
    article_list = ormmanage.query_article_all()
    user_name = request.cookies.get("user_name")
    return render_template("manage_article.html", user_name=user_name, article_list=article_list)


@app.route("/comment")
def comment():
    # comemnt = request.form["name"]
    print(request.args[0])

    return redirect("/user_home")



# from flask import Flask, render_template, request, make_response, redirect
# import datetime
# from hashlib import md5
#
# app = Flask(__name__)
#
# # 更新缓存
# app.send_file_max_age_default = datetime.timedelta(seconds=1)
# app.debug = True
#
#
# # print(app.config)
#
#
# @app.route('/')
# def index():
#     name = request.cookies.get("name")
#     user_set = None
#     if name:
#         user_set = mysql_get_data()
#         print(user_set)
#     return render_template('index.html', user_set=user_set, name=name)
#
#
#
#
# def mysql_get_data():
#     db = pack_mysql.PackMysql()
#     user_set = db.query_all("select * from student")
#     return user_set
#
#
# @app.route('/news/<int:page>')
# def news(page):
#     db = pack_mysql.PackMysql()
#     user_set = db.query_all("select * from student where id limit %s, %s", ((page - 1) * 20, page + 19))
#     return render_template('news.html', user_set=user_set, page=page)
#
#
# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "GET":
#         print("收到注册get请求")
#         args = request.args
#         username = args.get("name")
#         password = args.get("value1")
#         print(username, password)
#         return render_template('register.html')
#     elif request.method == "POST":
#         print("收到注册post请求")
#         user_set = mysql_get_data()
#         username = request.form["username"]
#         password = request.form["password"]
#         m = md5()
#         m.update(password.encode("utf8"))
#         pwd = m.hexdigest()
#         # print(username, pwd)
#         db = pack_mysql.PackMysql()
#         if not db.query_one("select * from user where account=%s" % username):
#             db.add("insert into user values (%s, %s, '待完善')", (username, pwd))
#             return redirect('/login')
#         else:
#             return redirect('/register')
#
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "GET":
#         print("登录get请求")
#         return render_template("login.html")
#
#     elif request.method == "POST":
#         print("登录post请求")
#         username = request.form["username"]
#         password = request.form["password"]
#         print(type(password))
#         print(password)
#         m = md5()
#         m.update(password.encode("utf8"))
#         pwd = m.hexdigest()
#         print(username, pwd)
#         db = pack_mysql.PackMysql()
#         print(db.query_one("select * from user where account='%s'" % username))
#         if db.query_all("select * from user where account=%s and password=%s ", (username,pwd)):
#             print("登陆成功")
#             res = make_response(redirect("/"))
#             res.set_cookie("name", username, expires=datetime.datetime.now()+datetime.timedelta(days=7))
#             return res
#         else:
#             print("登录失败")
#             return render_template("login.html")
#


if __name__ == "__main__":
    # 绑定ip端口号启动程序
    app.run(host="192.168.12.147", port=8888, debug=True)
    # git获取路径
    git = "https://github.com/zzy0371/Py1901Advance.git"
