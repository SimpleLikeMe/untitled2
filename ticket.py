import threading
import time

ticket_num = 200000


def time_count(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, "消耗", end - start)

    return fun


def add_num():
    global ticket_num

    for i in range(1000000):
        lock.acquire()
        ticket_num += 1
        lock.release()


def ticket_office():
    while True:
        # time.sleep(0.5)
        lock.acquire()
        global ticket_num
        ticket_num -= 1
        # print(type(threading.current_thread()) )
        print("线程：%d售出了一张票，剩余：%d张票" % (threading.current_thread().ident, ticket_num))

        if ticket_num <= 0:
            break
        lock.release()


lock = threading.Lock()


@time_count
def main():
    t_list = []
    for i in range(5):
        # t = threading.Thread(target=ticket_office)
        t = threading.Thread(target=add_num)
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()

    print(ticket_num)


if __name__ == "__main__":
    main()
