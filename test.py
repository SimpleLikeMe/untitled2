import os
import logging

# logging.basicConfig(filename="sys_test.log", level=logging.ERROR)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")


# 创建日志模块
loginLogger = logging.getLogger("main")

# 设置日志等级
loginLogger.setLevel(logging.ERROR)

# 创建日志输出类型
fileHandle = logging.FileHandler("loginRegister.log", encoding="utf-8")

# 指定日志格式
fileFormatter = logging.Formatter("%(name)s-%(lineno)d-%(asctime)s-%(message)s")

# 将文件绑定日志格式
fileHandle.setFormatter(fileFormatter)

# 将日志处理方法添加到日志工具
loginLogger.addHandler(fileHandle)

# 写日志
loginLogger.debug("debug")
loginLogger.info("info")
loginLogger.warning("warning")
loginLogger.error("error")

import json,pickle


class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


goods_ls = {}
name = input("请输入商品名：")
price = input("请输入商品价格：")

goods = Goods(name, price)
# goods = Goods('name', 'price')

goods_ls[0] = str(goods)

with open(file="goods.txt", mode="wb") as f:
    f.write(pickle.dumps(goods))

with open(file="goods.txt", mode="rb") as f:
    goods1 = pickle.loads(f.read())
    print(goods1.name)


ls = [1, 5, 34, 6, 45, 67, 56, 34, 345, 343, 434, 54, 3434, 64, 34, 54, 34, 54, 231, 54, 243, ]

print(list(filter(lambda x: x % 2, ls)))
print(sorted(list(map(lambda x: x * 2, ls))))


