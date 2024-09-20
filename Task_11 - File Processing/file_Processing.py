def process_log_file():
    filename = input("Enter the log file name: ")
    keyword = input("Enter the word you want to search for: ")
    
    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                if keyword in line:
                    count += 1
            print(f"Number of lines containing '{keyword}': {count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

process_log_file()
