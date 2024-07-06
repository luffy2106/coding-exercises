import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Manager, Process, Pool, cpu_count
from typing import Callable, Iterable, Dict, Any
import time
import signal
from functools import partial
from os import getpid, kill
import signal
import multiprocessing
import sys


def kill_pool(pool):
    """
        Kill all the process of a pool
    """
    pool._state = multiprocessing.pool.TERMINATE
    pool._worker_handler._state = multiprocessing.pool.TERMINATE
    for process in pool._pool:
        kill(process.pid, signal.SIGKILL)
    while any(process.is_alive() for process in pool._pool):
        pass
    pool.terminate()


def handler_with_pool(pool, signum, frame):
    """
        Handler to kill all the process of a pool and
        the current process
    """
    print('Signal handler called with signal',
          signum, file=sys.stderr, flush=True)
    kill_pool(pool)
    my_pid = getpid()
    kill(my_pid, signal.SIGKILL)


def handler_without_pool(signum, frame):
    """
        Handler to kill the current process
    """
    print('Signal handler called with signal',
          signum, file=sys.stderr, flush=True)
    my_pid = getpid()
    kill(my_pid, signal.SIGKILL)


def get_double(x):
    if x==3:
        print("start wait for 5 seconds")
        time.sleep(100)
        return x * 2
    else:
        print("return immediately")
        return x * 2        

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    # raise OSError("Couldn't open device!")
    # return get_double(2)
    raise Exception("end of time")

def main():
    # numbers = [1,2,3,4]
    # nb_process = int(0.8 * cpu_count())
    # pool = Pool(nb_process)
    # signal.signal(signal.SIGTERM, partial(handler_with_pool, pool))
    # double_numbers = pool.map(get_double, numbers)
    # pool.close()
    # signal.signal(signal.SIGTERM, handler_without_pool)
    # print(double_numbers)
    # signal.signal(signal.SIGALRM, handler)
    # signal.alarm(2)
    # print(get_double(3))
    # signal.alarm(0)

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(2)
    x = 0
    try:
        x = get_double(3)
    except Exception:
        x =  get_double(2)
    print(x)
if __name__ == '__main__':
    main()