from multiprocessing import Process

# creating a deamon process which would do a specific work

def work(count):
    print(count*count)

process_list = []
for i in range(5):    
    p = Process(target = work, args=(i,))
    p.start()
    process_list.append(p)
    
for process in process_list:
    process.join()
