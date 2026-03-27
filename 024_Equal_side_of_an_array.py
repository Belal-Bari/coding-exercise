# You are going to be given an array of integers. Your job is to take that
#  array and find an index N where the sum of the integers to the left of
#  N is equal to the sum of the integers to the right of N.

# If there is no index that would make this happen, return -1.

# For example:
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because the sum of left side of
#  the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because the sum of left side of 
# the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.

# Note: Please remember that in most languages the index of an array starts at 0.

# Input
# An integer array of length 0 < arr < 1000. The numbers in the array 
# can be any integer positive or negative.

# Output
# The lowest index N where the side to the left of N is equal to the side 
# to the right of N. If you do not find an index that fits these rules, then you will return -1.

# Note
# If you are given an array with multiple answers, return the lowest correct index.

def find_even_index(arr):
    for indx,n in enumerate(arr):
        if indx == 0: 
            if (sum(arr[1:]) == 0): return 0
        
        if indx == len(arr)-1:
            if (sum(arr[:len(arr)-1]) == 0): return indx
            
        if (sum(arr[:indx]) == sum(arr[indx+1:])) : return indx
    return -1

print(find_even_index([10,-80,10,10,15,35,20]))