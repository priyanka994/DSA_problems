#Tail-Call Recursion.
#It reduces the Space Complexity.
# "a" is accumulator.
#fact of numbers.
def fact(n,a):
    if n<=1:
        return a
    else:
        return fact(n-1,n*a)
        
print(fact(4,1)) # 1 is base condiction
