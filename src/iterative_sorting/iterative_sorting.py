# TO-DO: Complete the selection_sort() function below 
    
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        smallest_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
            
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr