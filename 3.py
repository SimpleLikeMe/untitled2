import time


def time_count(fun):
    """统计程序运行时间装饰器"""
    def t():
        start = time.time()
        fun()
        end = time.time()
        print(fun.__name__, "消耗", end - start, "秒")
        return end - start

    return t


# 用time_count装饰器装饰函数，统计函数print_count()运行的时间
@time_count
def print_count():
    """
    裴波拉契数列生成函数
    :return:None
    """
    def fun():
        a, b = 0, 1
        count = 0
        while count < 10000:
            yield a
            a, b = b, a + b
            count += 1

    for f in fun():
        print(f, "\n")


# 用time_count装饰器装饰函数，统计函数print_list()运行的时间
@time_count
def print_list():
    # 生成迭代器
    ls = (x for x in range(10))
    # for循环获取迭代器的内容
    for i in ls:
        print(i)


# 调用被装饰器装饰的函数
print_count()
# 调用被装饰器装饰的函数
print_list()


class User:
    """定义用户类"""

    def __init__(self, account, password, name="新用户", integration=100):
        """
        初始化用户对象的属性
        :param account: 用户的账号
        :param password: 用户的密码
        :param name: 用户的昵称
        :param integration: 用户的积分
        """
        self.account = account
        self.name = name
        self.password = password
        self.integration = integration


# 装饰器，用户验证用户是否合法
def check(fun):
    def check_user(user=None):

        if isinstance(user, User) and user.account == "admin" and user.password == "admin":
            fun()
            return True
        else:
            print("登陆失败")
            return False

    return check_user


# 用户登录成功后的主页
def show_index():
    print("登陆成功")
    print("显示主页")


# 用装饰器装饰login函数，用于验证用户的合法性
@check
def login():
    return show_index()


# 调用被装饰器装饰的函数，该函数具有了验证密码的功能
res = login(User(account="admin", password="admin"))
print(res)


