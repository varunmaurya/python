import os
import time
from multiprocessing import Manager
from multiprocessing.pool import Pool


class globals:
    def __init__(self, count, value):
        self.count = count
        self.value = value

    def __str__(self):
        return str(self.count) + ',' + str(self.value)


class PoolTest:
    def f(self, i, l, d):
        time.sleep(2)
        print('Printing in actual function : ' + str(os.getppid()) + ':' + str(os.getpid()) + ': ' + str(i * i))
        d[i] = globals(i, i ** 3)
        l[i] = i ** 3
        return str(os.getppid()) + ':' + str(os.getpid()) + ': ' + str(i * i)

    def call_pool(self):
        p = Pool(5)
        x = []
        l = {}  # regular dict
        d = Manager().dict()  # manager dict
        for j in range(10):
            x.append(p.apply_async(self.f, args=[j, l, d, ]))

        p.close()
        p.join()
        for z in x:
            print('printing from return obj : ' + str(z.get()))

        print('Printing regular dict : ' + str(l))
        for item in d.keys():
            g = d[item]
            print('Printing manager dict  key : %d  value %d - %d' % (item, g.count, g.value))


if __name__ == '__main__':
    t = PoolTest()
    t.call_pool()