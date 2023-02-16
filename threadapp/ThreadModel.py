import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, func, args=()):
        super(myThread, self).__init__()
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        print(self.name + "---------start--------")
        time0 = time.time()
        self.result1, self.result2 = self.func(*self.args)
        time1 = time.time()
        print(self.name + '--------end------用时:%s' % (time1-time0))


    def get_result(self):
        try:
            return self.result1, self.result2
        except Exception as e:
            return None


def thread1(name):
    print('%s:线程执行了' % name)
    list1 = ['thread1_1']
    list2 = ['thread1_2']
    return list1, list2


def thread2(name):
    print('%s:线程执行了' % name)
    list1 = ['thread2_1']
    list2 = ['thread2_2']
    return list1, list2


def main():
    threads = []
    result = []
    t1 = myThread('thread1', thread1, args=('thread1',))
    t1.start()
    threads.append(t1)

    t2 = myThread('thread2', thread2, args=('thread2',))
    t2.start()
    threads.append(t2)

    for t in threads:
        t.join()
        res1, res2 = t.get_result()
        result.append(res1)
        result.append(res2)
    print(result)

main()

