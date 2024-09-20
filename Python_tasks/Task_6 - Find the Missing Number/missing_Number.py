## Because the values are in range of 1 to n so i have used cyclic sort to solve this problem 
def find_missing(arr, n):
    i = 0 
    while i < n-1:
        correct_index = arr[i] - 1
        if arr[i] > 0 and arr[i] < n and arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i+=1
    for i in range(n - 1):
        if  arr[i] != i+1:
            return i+1
    return n

arr = [1, 2, 3, 4]
n = 5
print(find_missing(arr, n))  
            
            