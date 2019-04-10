import threading
from multiprocessing import Process, Queue, Manager, Pool
import time
import requests

q = Queue(10)
q3 = Queue(50)
q4 = Queue(50)


def time_count(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, "消耗", end - start)

    return fun


class MyThread(threading.Thread):
    """继承线程类"""

    def run(self):
        """重写线程调用start方法第一次执行的run方法"""
        while True:
            # 每隔0.5秒打印hi
            time.sleep(0.5)
            print("线程输出：hi")


class MyProcess(Process):
    """继承进程类"""

    def run(self):
        """重写run方法"""
        while True:
            # 每隔0.5秒输出hi
            time.sleep(0.5)
            print("进程输出：hi")


def production():
    while True:
        time.sleep(1.5)
        # data = random.randint(10)
        # print("生产者生产了数字：%d" )
        # 用put方法向队列中加入数据
        for i in range(3):
            q.put(i)
            print("生产者生产了数字：%d" % i)


def consumption():
    # print(type(q))
    while True:
        time.sleep(1)
        data = q.get()
        print("消费者消费了数字：%d" % data)


def production1(q):
    # print(type(q))
    while True:
        time.sleep(1.5)
        # data = random.randint(10)
        # print("生产者生产了数字：%d" )
        print("生产者生产了数字：%d" % 1)
        q.put(1)


def consumption1(q):
    # print(type(q))
    while True:
        time.sleep(2)
        data = q.get()
        print("消费者消费了数字：%d" % data)


def get_img():
    img_url = q3.get()
    img = requests.get(img_url)
    print("线程：%d从地址%s获取到图片" % (threading.current_thread().ident, img_url))
    # 将图片加入图片队列
    q4.put(img)


@time_count
def main():
    # 1，编写进程，线程封装类，实现功能每隔1秒打印hi
    # 获取线程对象
    # t = MyThread()
    # # 启动线程
    # t.start()
    # # 获取进程对象
    # p = MyProcess()
    # # 启动进程
    # p.start()
    # # 主进程等待线程结束
    # t.join()
    # # 主进程等待进程结束
    # p.join()

    # 2，编码验证队列put、get、put_nowait、get_nowait方法使用
    # 获取队列对象，并设置队列容量
    # t_list = list()
    # # 分别创建5个生产者和消费者线程，并启动线程
    # for i in range(5):
    #     t1 = threading.Thread(target=production)
    #     t2 = threading.Thread(target=consumption)
    #     t1.start()
    #     t2.start()
    #     t_list.append(t1)
    #     t_list.append(t2)
    #
    # # 主线程等待子线程
    # for t in t_list:
    #     t.join()
    # 创建一个队列，并设置队列容量
    q1 = Queue(10)
    # 用put方法向队列中加入数据
    # for i in range(9):
    #     q1.put(i)
    #     print(q1)
    # # 用get方法取出队列中的数据,队列中数据不足时不够报错，只会阻塞。若设置超时参数timeout则在超时后队列中还为空抛出Empty异常
    # for i in range(12):
    #     data = q1.get()
    #     # data = q1.get(timeout=5)
    #     print(data)
    #
    # # 用put方法向队列中加入数据，当队列满时只会阻塞，若设置超时时间，超时后队列还为满则抛出Full异常
    # for i in range(15):
    #     q1.put(i)
    #     # q1.put(i, timeout=5)
    #     print(q1)

    # # 用put_nowait方法向队列中加入数据,若队列满则抛出Full异常
    # for i in range(15):
    #     q1.put_nowait(i)
    #     print(q1)
    # # 用get_nowait方法向队列中加入数据,若队列为空则抛出Empty异常
    # for i in range(15):
    #     data = q1.get_nowait()
    #     print(data)

    # 3，利用进程池和队列模拟任务队列功能
    # # 获取一个队列
    # queue_container = Manager().Queue(10)
    # # 获取进程池
    # pool = Pool(processes=4)
    # # 异步开启进程,
    # for i in range(2):
    #     # 开启两个生产者进程
    #     pool.apply_async(production1, args=(queue_container,))
    #     # 开启两个消费者进程
    #     pool.apply_async(consumption1, args=(queue_container,))
    #     # print("创建进程结束")
    #
    # # 关闭线程池
    # pool.close()
    # # 主进程等待子进程的执行
    # pool.join()
    # print("主进程结束")

    # 4，使用单进程单线程 ，多进程，多线程完成图片下载保存功能
    # 定义img列表
    img_list = list()
    # 定义img的url列表
    img_url_list = [
        'https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=bc9be6a0336d55fbc3c672265d224f40/b3119313b07eca80ff34b3999f2397dda144839f.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=cb250cb54d166d223e77119476220945/cb8065380cd7912309031f0aa3345982b3b780e9.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=4ed4331a9aeef01f4b141cc5d0ff99e0/bba1cd11728b4710434977b2cdcec3fdfc03236e.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=97a7118d77310a55c224daf487444387/a8ec8a13632762d097922fc1aeec08fa513dc624.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0ca80270bf3533faf3b6972e98d2fdca/0824ab18972bd407208a588375899e510fb3097a.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=b54a4692df00baa1bc2c43bb7711b9b1/faedab64034f78f0dd41118d77310a55b3191c01.jpg',
        'https://imgsa.baidu.com/news/q%3D100/sign=0c3d18a206fa513d57aa68de0d6c554c/c75c10385343fbf22fa32b5dbe7eca8064388fc5.jpg',
    ]
    # # 单线程下载图片
    # for img_url in img_url_list:
    #     # 获取图片
    #     img = requests.get(img_url)
    #     print("从地址%s获取到图片" % img_url)
    #     # 将图片加入图片列表
    #     img_list.append(img)

    # 多线程获取图片
    # 将图片加入队列
    # for img_url in img_url_list:
    #     q3.put(img_url)
    # tt_list = list()
    # # 开启线程获取图片
    # for i in range(10):
    #     t2 = threading.Thread(target=get_img)
    #     t2.start()
    #     tt_list.append(t2)
    #
    # for t in tt_list:
    #     t.join()



if __name__ == "__main__":
    main()
