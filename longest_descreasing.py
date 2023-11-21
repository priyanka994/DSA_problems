import sys
#Longest decreasing subsequence length = 5
nums=[20,8,12,16,10,9,18,7,3]

def get_lds(num,i,prev):
    if i==len(nums):
        return 0
    incl=0
    if nums[i]<prev:
        incl=1+get_lds(num, i+1,nums[i])
    excl=get_lds(nums,i+1,prev)
    return max(incl,excl)
print(sys.maxsize)
print(get_lds(nums,0,sys.maxsize))
