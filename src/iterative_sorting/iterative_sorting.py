# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    if not arr:
        return arr
    # if its not an array, just return
    for i in range(len(arr)-1):
        # looping from 0 to array length - 1
        currentIndex = i
        minIndex = currentIndex
        # minIndex for reference
        for j in range(i+1, len(arr)):
            # looping from 1 to end of array
            if arr[j] < arr[minIndex]:
                # if lower index item is larger than bigger index item
                minIndex = j
                # temp holder of lowest index
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        # smallest index location, bigger index location swap
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swaps = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps = swaps + 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
