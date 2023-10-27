#!/usr/bin/env python3

def count_unique(numstr):
    pass
    #---------------------- 
    # write your code here
    #---------------------- 
    num_list = [int(num) for num in numstr.split()]

    unique_count = {}
    count = 0

    for num in num_list:
        if num not in unique_count:
            unique_count[num] = 1
            count += 1

    return count
#---------------------------------------------------------------------
# you can modify the following to test your code more thoroughly
#---------------------------------------------------------------------
data = [
    "1 2 3 4 5 6 7 8 9",
    "1 1 1 1 1 1 1 1",
    "1 2 1 2 1 2 1 2",
    "1 2 3 1 2 3 1 2 3",
    "1 1 1 1 2",
    "1 2 2 3 3 4",
    "1 2 3 4 5 1 2 3 4",
    "1 2 3 4 1 2 3 4 5",
    "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
]


        
def main():
    global data
    for test_case in data:
        result = count_unique(test_case)
        print(result)
        
if __name__ == '__main__':
    main()