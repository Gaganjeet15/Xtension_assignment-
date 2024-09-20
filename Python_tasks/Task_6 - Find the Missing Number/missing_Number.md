Given a list of n-1 integers from the range 1 to n, write a function find_missing(arr, n) to find the missing number.

**Because the values are in range of 1 to n so i have used cyclic sort to solve this problem**

Explanation:
1. The functions takes an array or list and length of array as input.
2. Using the while loop i have sorted the array in place using cyclic sort or swap sort
   * (Cycle sort is an in-place, unstable sorting algorithm that is particularly useful when sorting arrays containing elements with a small range of values)
3. after  sorting the array i have used for loop which will check that i values of the array are at their correct index.
4. Return - If the values of array is not at correct index then we return i+1 which will be the missing number. 
5. Time complexity: O(n), Space complexity: O(1).
