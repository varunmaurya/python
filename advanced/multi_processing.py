import os
import time
from multiprocessing import Process


def work(count):
    time.sleep(5)  # mimicking some work
    print('Parent Id : %d process_id : %d :: %d' % (os.getppid(), os.getpid(), count * count))


if __name__ == '__main__':

    process_list = []
    for i in range(5):
        p = Process(target=work, args=(i,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    print('Processing complete for all processes')