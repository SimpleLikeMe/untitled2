import sys
import json
from collections.abc import Iterator, Iterable
import logging
logging.basicConfig(level=logging.DEBUG, filename="sys.log", format="%(levelno)s-%(levelname)s-%(lineno)s")
# logging.basicConfig(filename="sys.log", )

logging.error("系统错误")
logging.info("系统错误")
logging.warning("系统错误")
logging.debug("系统错误")
# logging.name("系统错误")


# 列表生成式
# list1 = [x for x in range(100000)]
#
# print(sys.getsizeof(list1))
#
# # 生成器
# list2 = (x for x in range(100000000))
# print(sys.getsizeof(list2))
#
# list3 = (x for x in range(10000000))
# print(sys.getsizeof(list3))

# buf = []
# index = 0


# for f in list2:
#     buf.append(f)
#     if len(buf) >= 1000:
#         with open("1.txt", mode="a", encoding="utf8") as fp:
#             index += 1
#             fp.write(json.dumps(buf))
#             fp.write("\n")
#             print(index)
#         buf.clear()


# 裴波拉契数列函数式生成器
# def fun(num):
#     a, b = 0, 1
#     count = 0
#
#     while count < num:
#         yield a
#         a, b = b, a + b
#         # print(count)
#         count += 1
#
#
# for f in fun(10):
#     print(f)

# for g in fun(10000):
#     buf.append(g)
#     if len(buf) >= 100:
#         with open("1.txt", mode="a", encoding="utf8") as fp:
#             index += 1
#             fp.write(json.dumps(buf))
#             fp.write("\n")
#             print(index)
#         buf.clear()


# print([], isinstance([], Iterable))
# print([], isinstance([], Iterator))

# ls = [1, 3, 5, 7, 9]
# itls = iter(ls)

# class Goods:
#     def __init__(self, addr):
#         self.addr = addr
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.addr):
#             result = self.addr[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
#
#
# ls = [1, 3, 5]
# goods = Goods(ls)
#
# print(isinstance(goods, Iterable))
#
# print(next(goods))


class User:
    """定义user类"""

    def __init__(self, account, password, name="新用户", integration=100):
        self.account = account
        self.name = name
        self.password = password
        self.integration = integration


# 装饰器
def check(fun):
    def check_user(user=None):

        if isinstance(user, User) and user.account == "admin" and user.password == "admin":
            fun()
            return True
        else:
            print("登陆失败")
            return False

    return check_user


def show_index():
    print("登陆成功")
    print("显示主页")


@check
def login():
    return show_index()


res = login(User(account="admin", password="admin"))
print(res)

# list1 = [1,2,[3,4]]
# print(list1)
# list2 = list1
# print(list2)
# list1.append(5)
# print(list1,list2)
# list1[2].append(3.5)
# print(list1,list2)


# import copy
# list1 = [1, 2, [3, 4]]
# print(list1)
# list2 = copy.copy(list1)
# print(list2)
# list1.append(5)
# print(list1, list2)
# list1[0] = 9
# list1[2].append(3.5)
# print(list1, list2)


#
# import copy
# list1 = [1,2,[3,4]]
# print(list1)
# list2 = copy.deepcopy(list1)
# print(list2)
# list1.append(5)
# list1[0] = 9
# print(list1,list2)
# list1[2].append(3.5)
# print(list1,list2)


import time


def time_count(fun):
    def t():
        start = time.time()
        fun()
        end = time.time()
        print(fun.__name__, "消耗", end - start, "秒")
        return end - start

    return t


@time_count
def print_count():
    def fun():
        a, b = 0, 1
        count = 0

        while count < 100000:
            yield a
            a, b = b, a + b
            count += 1

    for f in fun():
        # pass
        print(f, "\n")


@time_count
def print_list():
    ls = (x for x in range(100000000))
    for i in ls:
        pass
        # print(i)


# print_count()

# print_list()






