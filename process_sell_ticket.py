import os
import time

from multiprocessing import Process
import threading


def son_method():
    print("在子进程中创建的进程：%d,其父线程为：%d" % (os.getpid(), os.getppid()))

def ticket_window(win):
    print(type(win))
    # 在子进程中创建进程
    pson = Process(target=son_method)
    # 启动进程
    pson.start()
    if (type(win).__name__ == 'list'):
        # 如果win是列表添加一个元素
        print(win)
        win.append("北京")
        print(win)
    for i in range(10):
        time.sleep(1)
        print("进程编号：%d, 父进程编号：%d, %s：售出第%d张票" % (os.getpid(), os.getpid(), win, i))


def main():
    ls = [["武汉"], ]
    # 获取主进程编号
    print("当前进程(main process)的编号 %d, 主线程的父进程编号：%d" % (os.getpid(), os.getppid()))
    # 创建进程，绑定入口函数，传递一个可迭代对象args给入口函数，也可以传递键值对kwargs，由于进程之间的数据是独立的，所以不能实现多窗口售票。
    win1 = Process(target=ticket_window, args=ls)
    win2 = Process(target=ticket_window, args=["长沙站", ])
    # 开启进程
    win1.start()
    win2.start()
    time.sleep(1)
    # 判断进程是否存活
    print(win1.is_alive())
    # 停止进程，需要一段时间
    win1.terminate()
    # 杀死进程，
    # win1.kill()
    time.sleep(1)
    print(win1.is_alive())
    # 将让主进程等待win1进程执行结束再执行后面程序
    win1.join()
    # win1进程执行结束,输出传递过去的列表是否被修改
    print(ls)
    # 当win1结束执行后面程序
    print("等待win1结束")
    win2.join()
    print("主进程结束")


if __name__ == "__main__":
    main()
