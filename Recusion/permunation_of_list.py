def permute(array):
    if len(array)==0:
        return [[]]
    else:
        permu=[]
        for i in range(len(array)):
            new_array=array[:]
            new_array.remove(array[i])
            for j in permute(new_array):
                permu.append([array[i]] + j)
        return permu
                
            
print(permute([1,2,3,10]))
