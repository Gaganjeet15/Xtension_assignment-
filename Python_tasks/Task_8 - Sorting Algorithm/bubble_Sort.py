## I have used Bubble Sort for sorting the list or array.
def bubble_sort(arr):
    n = len(arr)
    # Loop over the array
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
arr = [60, 4, 54, 2, 2, 7, 1, 1, 15, -1]
sorted_arr = bubble_sort(arr)
print("Sorted Array:", sorted_arr)
