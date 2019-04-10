import os
import time

from multiprocessing import Process
import threading


def ticket_window(win):
    # print(type(win))
    lock = threading.Lock()

    for i in range(10):
        lock.acquire()
        time.sleep(1)
        print("%s：售出第%d张票" % (win, i))
        lock.release()



def main():
    # 创建进程
    win1 = threading.Thread(target=ticket_window, args=["武汉站", ])
    win2 = threading.Thread(target=ticket_window, args=["长沙站", ])
    win1.start()
    win2.start()
    win1.join()
    print("等待win1结束")
    win2.join()
    print("主进程结束")


if __name__ == "__main__":
    main()
