
def tower_of_hanoi(n,from_rod,to_rod,temp,count):
    if n==1:

        print("Moving the 1 disk from ", from_rod, "to ",to_rod,"rod.")
    else:
        tower_of_hanoi(n-1,from_rod,temp,to_rod,count+1)
        print("Moving the disk ",n,"from ",from_rod," to the ",to_rod,"rod.")
        tower_of_hanoi(n-1,temp,to_rod,from_rod,count+1)
        

tower_of_hanoi(5,"source","temp","Dest",0) 

print(2**5)
        
#time complexity of this problem is O(2^n)
