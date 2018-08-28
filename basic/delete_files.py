import os

import time

path = '/opt/varun/my_work/test/'

def delete_files():
    for cur_dir,_,files in os.walk(path):
        for f in files:
            os.remove(os.path.join(cur_dir,f))


if __name__ == '__main__':
    while True:
        delete_files()
        time.sleep(60)
