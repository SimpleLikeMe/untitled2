import os, time
from multiprocessing import Process


def p2_process():
    for i in range(5):
        print("p2开始输出%d" % i)
        time.sleep(2)


def p1_process():
    print("p1进程，进程id：%d" % os.getpid())
    # 在子进程中创建一个子进程
    # time.sleep(3)
    p2 = Process(target=p2_process)
    p2.start()
    # p2.join()
    for i in range(5):
        print("p1开始输出%d" % i)
        time.sleep(1)


def main():
    print("主进程启动，进程id：%d, pycharm进程id：%d" % (os.getpid(), os.getppid()))
    # 创建进程,target绑定入口函数
    p1 = Process(target=p1_process)
    # 启动进程
    p1.start()
    # p1.join()
    time.sleep(2)
    # 判断进程是否存活
    print("p1是否存活：", p1.is_alive())
    # 终止p1进程，但是进程还可以存活
    p1.terminate()
    # 杀手p1进程
    p1.kill()
    print("p1是否存活：", p1.is_alive())

    print("主进程结束")


if __name__ == "__main__":
    main()
