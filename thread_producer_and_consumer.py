import threading
import random
import time

print(dir(threading))


def time_count(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, "消耗", end - start)

    return fun


def production():
    # data = random.randint(100)
    print("生产者生产了数字：%d" % 4)
    time.sleep(1)


def consumption():
    pass


@time_count
def main():
    t_list = []
    # 获取线程
    for i in range(5):
        # 创建线程对象
        t = threading.Thread(target=production)
        # 将线程加入列表
        t_list.append(t)
        # 启动线程
        t.start()

    for t in t_list:
        # 主线程等待子线程结束
        t.join()


if __name__ == "__main__":
    main()

t = ['Barrier', 'BoundedSemaphore', 'BrokenBarrierError', 'Condition', 'Event', 'Lock', 'RLock', 'Semaphore',
     'TIMEOUT_MAX', 'Thread', 'ThreadError', 'Timer', 'WeakSet', 'activeCount', 'active_count', 'currentThread',
     'current_thread', 'enumerate', 'get_ident', 'local', 'main_thread', 'setprofile', 'settrace', 'stack_size']

