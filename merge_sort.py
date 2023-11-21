def merge(arr,l,m,u):
    n1=m-l+1
    n2=u-m
    
    left=[0]*n1
    right=[0]*n2
    for x in range(0,n1):
        left[x]=arr[l+x]
    for y in range(n2):
        right[y]=arr[m+1+y]
        
    #merge array
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if left[i]<right[j]:
            arr[k]=left[j]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
        
    while i<n1:
        arr[k]=left[i]
        i=+1
        k+=1
    while j<n2:
        arr[k]=right[j]
        j+=1
        k+=1
def mergesort(arr,l,u):
    mid=0
    if l<u:
        mid=(l+(u-1))//2
        mergesort(arr,l,mid)
        mergesort(arr,mid+1,u)
        merge(arr,l,mid,u)
   
arr=[1,5,9,2]
mergesort(arr,0,3) 
print(arr)
