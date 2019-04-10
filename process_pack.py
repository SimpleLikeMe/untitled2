from multiprocessing import Process


class MyProcess(Process):
    """
        继承进程类
    """

    def run(self):
        """重写进程类的run方法，当创建进程类实例时自动绑定run方法"""
        print("实例调用start方法时,自动调用run方法")


def main():
    # 创建自定义进程类
    my_process = MyProcess()
    # 启动进程
    my_process.start()


if __name__ == "__main__":
    main()
