Write a function fizz_buzz(n) that prints the numbers from 1 to n. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

Explanation:

1. It takes an integer n as input.
2. It iterates through the numbers from 1 to n using a for loop.
3. For each number:
   * If it's divisible by both 3 and 5, it prints "FizzBuzz".
   * If it's only divisible by 3, it prints "Fizz".
   * If it's only divisible by 5, it prints "Buzz".
   * If it's not divisible by 3 or 5, it prints the number itself.