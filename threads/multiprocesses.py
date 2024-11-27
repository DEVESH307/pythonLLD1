import multiprocessing
import time


def helloWorld(t):
    time.sleep(t)
    print(f"Hello World from {multiprocessing.current_process().name}")


if __name__ == '__main__':
    time1 = time.perf_counter()
    p1 = multiprocessing.Process(target=helloWorld, args=(4,))
    p2 = multiprocessing.Process(target=helloWorld, args=(4,))
    p3 = multiprocessing.Process(target=helloWorld, args=(4,))
    p10 = multiprocessing.Process(target=helloWorld, args=(4,))
    p11 = multiprocessing.Process(target=helloWorld, args=(4,))
    p12 = multiprocessing.Process(target=helloWorld, args=(4,))

    p1.start()
    p2.start()
    p3.start()
    p10.start()
    p11.start()
    p12.start()
    p1.join()
    p2.join()
    p3.join()
    p10.join()
    p11.join()
    p12.join()
    time2 = time.perf_counter()
    print(time2 - time1)
