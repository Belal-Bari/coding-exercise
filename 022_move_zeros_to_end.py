# Write an algorithm that takes an array and moves all of the zeros 
# to the end, preserving the order of the other elements.
# Example:
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    new_ary = [num for num in lst if num != 0]
    zeros_ary = [num for num in lst if num == 0]    
    return new_ary + zeros_ary

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))