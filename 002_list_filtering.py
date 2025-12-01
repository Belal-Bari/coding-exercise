# def filter_list(l):
#     new_list = []
#     new_list = [val for val in l if isinstance(val, (int,float))]
#     print(new_list)
#     return new_list

# filter_list([1, 2, 'a', 'b'])

# Refactored shorter version-->
def filter_list(l):
    new_list = [val for val in l if isinstance(val, (int,float))]
    return new_list