import random
import time
from threading import *
import multiprocessing

# obj = Semaphore(4)
# obj1 = Semaphore(0)
#
# def display(name):
#     obj1.release()
#     obj.acquire()
#     print("hello "+name + " ")
#     time.sleep(0.5)
#     obj.release()
#
#
#
# t1 = Thread(target=display, args=("t1",))
# t2 = Thread(target=display, args=("t2",))
# t3 = Thread(target=display, args=("t3",))
# t4 = Thread(target=display, args=("t4",))
# t5 = Thread(target=display, args=("t5",))
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
#
#


# import random
# import time
# from multiprocessing import Process, Semaphore
#
# # Shared resources
# total_size = 100
# buffer = []
#
# # Semaphores
# producer_semaphore = Semaphore(total_size)
# consumer_semaphore = Semaphore(0)
#
# # Producer function
#
# def producer_thread():
#     while True:
#         item = random.randint(1, 100)  # Produce an item
#         producer_semaphore.acquire()  # Wait for an empty slot
#         buffer.append(item)
#         if len(buffer) > total_size or len(buffer) < 0:
#             print(f"Buffer size anomaly: {len(buffer)}")
#         consumer_semaphore.release()
#
# # Consumer function
# def consumer_thread():
#     while True:
#         consumer_semaphore.acquire()  # Wait for an item
#         item = buffer.pop()           # Remove an item from the buffer
#         producer_semaphore.release()  # Signal an empty slot is available
#         if len(buffer) > total_size or len(buffer) < 0:
#             print(f"Buffer size anomaly: {len(buffer)}")
#
# # Main function
# if __name__ == '__main__':
#     # Create and start producer and consumer processes
#     p1 = Process(target=producer_thread)
#     p2 = Process(target=producer_thread)
#     p3 = Process(target=producer_thread)
#     p4 = Process(target=producer_thread)
#     p5 = Process(target=producer_thread)
#     p6 = Process(target=producer_thread)
#     c1 = Process(target=consumer_thread)
#     c2 = Process(target=consumer_thread)
#     c3 = Process(target=consumer_thread)
#     c4 = Process(target=consumer_thread)
#     c5 = Process(target=consumer_thread)
#     c6 = Process(target=consumer_thread)
#     c7 = Process(target=consumer_thread)
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     p5.start()
#     p6.start()
#     c1.start()
#     c2.start()
#     c3.start()
#     c4.start()
#     c5.start()
#     c6.start()
#     c7.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     p5.join()
#     p6.join()
#
#     c1.join()
#     c2.join()
#     c3.join()
#     c4.join()
#     c5.join()
#     c6.join()
#


shared_list = []

def add_to_list(n):
    for _ in range(n):
        shared_list.append(1)

def remove_from_list(n):
    for _ in range(n):
        if len(shared_list)>0:
            shared_list.pop()


if __name__ == '__main__':
    p = multiprocessing.Process(target=add_to_list, args=(500000, ))
    p2 = multiprocessing.Process(target=remove_from_list, args=(500000, ))

    p.start()
    p2.start()

    p.join()
    p2.join()

    print(shared_list)