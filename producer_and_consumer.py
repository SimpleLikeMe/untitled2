import time
from multiprocessing import Process, Queue, Pool,Manager
import random


def production(q):
    # print(type(q))
    while True:
        time.sleep(1.5)
        # data = random.randint(10)
        # print("生产者生产了数字：%d" )
        print("生产者生产了数字：%d" % 1)
        q.put(1)


def consumption(q):
    # print(type(q))
    while True:
        time.sleep(2)
        data = q.get()
        print("消费者消费了数字：%d" % data)


def main():
    # 获取一个队列
    queue_container = Manager().Queue(10)
    # 获取进程池
    pool = Pool(processes=4)
    # 异步开启进程,
    for i in range(2):
        # 开启两个生产者进程
        pool.apply_async(production, args=(queue_container,))
        # 开启两个消费者进程
        pool.apply_async(consumption, args=(queue_container,))
        # print("创建进程结束")

    # 关闭线程池
    pool.close()
    # 主进程等待子进程的执行
    pool.join()
    print("主进程结束")
    # time.sleep(5)


if __name__ == "__main__":
    main()
