# TO-DO: Complete the selection_sort() function below 


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        smallest_index = i

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if (arr[smallest_index] > arr[j]):
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] #O(1)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    l = len(arr)
    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# selection & bubble sort: O(n^2)
