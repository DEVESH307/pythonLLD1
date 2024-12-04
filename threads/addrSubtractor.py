# import threading
#
# shared_variable = 0
#
# lock = threading.Lock()
# def addr():
#     global shared_variable
#     for i in range(1000000):
#         lock.acquire()
#         shared_variable = shared_variable + 1
#         lock.release()
#
#
# def subtr():
#     global shared_variable
#     for i in range(1000000):
#         lock.acquire()
#         shared_variable = shared_variable - 1
#         lock.release()
#
#
# # addr()
# # subtr()
# # print(shared_variable)
#
#
# thread1 = threading.Thread(target=addr)
# thread2 = threading.Thread(target=subtr)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
# print(shared_variable)
import concurrent.futures
import threading

counter = 0


def increment_counter():
    global counter
    for _ in range(100000000):
        counter += 1


def decrement_counter():
    global counter
    for _ in range(100000000):
        counter -= 1


threads = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=decrement_counter)
ts = [threads, t2]
for t in ts:
    t.start()

for t in ts:
    t.join()
print(f"Final counter value: {counter}")


concurrent.futures.as_completed()