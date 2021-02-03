def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        pre = i - 1
        current_value = arr[i]
        while pre >= 0 and arr[pre] > current_value:
            arr[pre + 1] = arr[pre]
            pre -= 1
        arr[pre+1] = current_value
    return arr


def shell_sort(arr):
    length = len(arr)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            pre = i - gap
            current_value = arr[i]
            while pre >= 0 and arr[pre] > current_value:
                arr[pre + gap] = arr[pre]
                pre -= gap
            arr[pre + gap] = current_value
        gap = gap // 2
    return arr


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left[:])
    if len(right) > 0:
        result.extend(right[:])
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def partition(arr, left=None, right=None):
    pivot = left
    index = pivot + 1
    for i in range(index, right + 1):
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]
    return index - 1


def quick_sort(arr, left=None, right=None):
    left = 0 if left is None else left
    right = len(arr) - 1 if right is None else right
    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)
    return arr


global length2


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < length2 and arr[left] > arr[largest]:
        largest = left
    if right < length2 and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)


def build_max_heap(arr):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i)


def heap_sort(arr):
    global length2
    length2 = len(arr)
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        length2 -= 1
        heapify(arr, 0)
    return arr


def counting_sort(arr):
    max_value = max(arr)
    buckets = [0] * (max_value + 1)
    index = 0
    length = len(arr)
    for i in range(length):
        buckets[arr[i]] += 1
    for j in range(max_value + 1):
        while buckets[j] > 0:
            arr[index] = j
            index += 1
            buckets[j] -= 1
    return arr


def bucket_sort(arr):
    bucket_size = 5
    max_value = max(arr)
    min_value = min(arr)
    bucket_num = (max_value - min_value) // bucket_size + 1
    buckets = {i: [] for i in range(bucket_num)}
    for i in range(len(arr)):
        buckets[(arr[i] - min_value) // bucket_size].append(arr[i])
    result = []
    for i in range(bucket_num):
        insertion_sort(buckets[i])
        result.extend(buckets[i])
    return result


def radix_sort(arr):
    max_value = max(arr)
    max_digit = len(str(max_value))
    dev = 1
    mod = 10
    result = arr[:]
    for i in range(max_digit):
        buckets = {i: [] for i in range(mod)}
        for k in range(len(result)):
            key = (result[k] % mod) // dev
            buckets[key].append(result[k])
        result = []
        for j in range(mod):
            result.extend(buckets[j])
        dev *= 10
        mod *= 10
    return result
