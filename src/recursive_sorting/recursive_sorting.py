# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    print(arrA, arrB)

    # * COUNTERS
    left = 0 
    right = 0 
    total = 0

    # * APPEND INDEXES TO MERGED ARRAY
    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr[total] = arrA[left]
            left += 1
        else:
            merged_arr[total] = arrB[right]
            right += 1
        total += 1

    # ? IS ARRAY A AND B EMPTY?
    while left < len(arrA):
        merged_arr[total] = arrA[left]
        left += 1
        total += 1

    while right < len(arrB):
        merged_arr[total] = arrB[right]
        right += 1
        total += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort(arr):
    
    if (len(arr) > 1):

        # * LEFT SIDE ARR
        left = merge_sort(arr[:len(arr) // 2 ])

        # * RIGHT SIDE ARR
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)

    return arr

# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
