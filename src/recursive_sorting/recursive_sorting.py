# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    combined = arrA + arrB

    for index in range(0, len(merged_arr)):
        merged_arr[index] = combined[index]

    merged_arr.sort()

    return merged_arr

merge(
    [1, 5, 8, 4, 2, 9, 6, 0, 3, 7],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
)

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


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
