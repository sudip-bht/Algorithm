def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        swap(arr, i, min_index)
    return arr;

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

