Write a function fibonacci(n) that returns the first n numbers of the Fibonacci sequence (where each number is the sum of the two preceding ones, starting from 0 and 1).


Explanation:
1. The functions takes an integer as input.
2. The if and elif condions check that whether the number is less than or equal to 0.
   * if the number is less than or equal to 0 then it raises value error.
   * if the number is 1 it return 0 
   * if the number is 2 it return 1 
3. Else there is list "fib_sequence" which initially holds 0 and 1.
4. There is a for loop which handles the logic for appending the values in fib_sequence till n.
5. The function returns the fib_sequence which hold the result of the fibonacci.

