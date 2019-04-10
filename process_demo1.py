import time
import os
from multiprocessing import Process, Pool, Queue
import threading


def pool_handle():
    time.sleep(1)
    print("进程处理函数当前进程：%d，当前进程父进程：%d" % (os.getpid(), os.getppid()))
    th1 = threading.Thread()
    print(dir(th1))


def main():
    # 创建进程池容器
    pool = Pool(4)
    print(os.getpid(), os.getppid())
    pool.apply_async(pool_handle)

    # 关闭进程池，但是已经开辟的进程仍然可以用
    pool.close()
    # 终止进程池中所有进程
    # pool.terminate()

    # 阻塞主进程
    pool.join()

    # print(Process)
    # print(dir(Process()))
    print(dir(pool))
    # print(dir(Queue()))
    # print(dir(os))
    q = Queue(1)
    q.put(1)
    q.put(1, block=False)


# threading模块中的Thread类
t = ['daemon', 'getName', 'ident', 'isAlive', 'isDaemon', 'is_alive', 'join', 'name', 'run', 'setDaemon', 'setName',
     'start']
# multiprocessing模块中的Process类
t1 = ['authkey', 'close', 'daemon', 'exitcode', 'ident', 'is_alive', 'join', 'kill', 'name', 'pid', 'run', 'sentinel',
      'start', 'terminate']
# multiprocessing模块中的Pool类
t2 = ['Process', 'apply', 'apply_async', 'close', 'imap', 'imap_unordered', 'join', 'map', 'map_async', 'starmap',
      'starmap_async', 'terminate']
# 模块中的Queue类
t3 = ['cancel_join_thread', 'close', 'empty', 'full', 'get', 'get_nowait', 'join_thread', 'put', 'put_nowait', 'qsize']

o = ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM',
     'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH',
     'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX',
     'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
     '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv',
     '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange',
     'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl',
     'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode',
     'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable',
     'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep',
     'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe',
     'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir',
     'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile',
     'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd',
     'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size',
     'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk',
     'write']

if __name__ == "__main__":
    main()
