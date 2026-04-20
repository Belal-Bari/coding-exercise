# Given an n x n array, return the array elements arranged from 
# outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the 
# next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# NOTE: The idea is not sort the elements from the lowest value to the highest; 
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
def snail(snail_map):
    print(len(snail_map[0]))
    loop = (len(snail_map[0]) // 2) + (len(snail_map[0]) % 2)
    print(loop)
    temp_ary = snail_map
    res_ary = []
    for i in range(loop):
        print(f"loop: {i}")
        for ind, n in enumerate(temp_ary):
            for j in range(len(temp_ary[i])):
                res_ary.append(temp_ary[i].pop(0))
            if (len(temp_ary)-1 == ind):
        
    print(res_ary)
    print(temp_ary)
    return 

snail([[1,2,3],[4,5,6],[7,8,9]])