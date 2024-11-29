import threading

shared_variable = 0

lock = threading.Lock()
def addr():
    global shared_variable
    for i in range(1000000):
        lock.acquire()
        shared_variable = shared_variable + 1
        lock.release()


def subtr():
    global shared_variable
    for i in range(1000000):
        lock.acquire()
        shared_variable = shared_variable - 1
        lock.release()


# addr()
# subtr()
# print(shared_variable)


thread1 = threading.Thread(target=addr)
thread2 = threading.Thread(target=subtr)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(shared_variable)
