import concurrent.futures
import time
import random



def merge(leftArr, rightArr):
    result = []
    left = 0
    right = 0
    while left < len(leftArr) and right < len(rightArr):
        if leftArr[left] <= rightArr[right]:
            result.append(leftArr[left])
            left += 1
        else:
            result.append(rightArr[right])
            right += 1

    result.extend(leftArr[left:])
    result.extend(rightArr[right:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def parllel_merge_sort(arr, max_workers):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        leff_future = executor.submit(merge_sort, left)
        right_future = executor.submit(merge_sort, right)

        left_arr = leff_future.result()
        right_arr = right_future.result()
    return merge(left_arr, right_arr)


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(50000000)]
    # start = time.time()
    # sorted_arr = merge_sort(arr)
    # time_taken = time.time() - start
    # # print(sorted_arr)
    # print(time_taken)

    start = time.time()

    max_workers = 4
    sorted_arr = parllel_merge_sort(arr, max_workers)

    elapsed_time = time.time() - start

    # print(sorted_arr)
    print(f"Time taken: {elapsed_time}")


