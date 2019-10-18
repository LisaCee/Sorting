# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(0, len(arr) - 2):
            if arr[j] > arr[i]:
                pass
            else:
                smallest_index = j
                temp = arr[i]
        # TO-DO: swap
        arr[i] = arr[j]
        arr[j] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
