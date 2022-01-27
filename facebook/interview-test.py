# Write a function that takes two arguments: 1) an array of integers and 2) a “target” integer. 
# Return any two unique indices (as a tuple or array) in the input array that have values that sum together to equal the target. 
# Return (-1, -1) if no such indices exist.

# Input/output examples:
# function([2,14,1], 3) -> (0, 2)
# function([2,14,1], 0) -> (-1, -1)
# function([2,14,-2], 0) -> (0, 2)


def ind_output(num_list, target_int):
    for i in range(len(num_list) -1):
        for j in range(i +1, len(num_list)):
            total = num_list[i] + num_list[j]
            if total == target_int:
                return i,j
    return -1, -1    
