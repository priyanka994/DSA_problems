#Product sum of and Arrays.
#ex: [1,2,[3,2],6,[[2,4],1],7]

def sum_of_list(list_1,depth):
    sum_is =0
    for ele in list_1:
        if isinstance(ele,list):
            sum_is+=sum_of_list(ele,depth+1)
        else:
            sum_is+=ele
    return sum_is*depth
    
arr=[1,2,[3,2],6,[[2,4],1],7]

print(sum_of_list(arr,1))

#Time Complexity is O(N)
