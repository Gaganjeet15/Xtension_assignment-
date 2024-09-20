# Problem: Write a function process_log_file(filename) that reads a log file, counts the number of lines that contain a specific keyword (e.g., "ERROR"), and prints the count.

Explanation:
1. Function process_log_file()
2. In the function we are taking input from user:
    * Enter the log file name
    * Enter the word you want to search for
3. I hava used try execpt block:
    * In the try block opening the file as file and reading mode. 
    * In except block "FileNotFoundError" handles when files is not found
4. The for loop run through the file and there is a variable count which is initially is set to zero.
5. If keyword is in file then the count is increased by 1. 
6. Else if keyword is not in file then count will be returned as zero.