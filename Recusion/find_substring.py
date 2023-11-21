def getsubsequences(word):
    if len(word)==0:
        return " "
    first_char=word[0]
    res=getsubsequences(word[1:])  # n-1 O(n)
    result=""
    
    for substring in res.split(","):  #
        
        result +=","+first_char+substring
        result +=","+substring
    return result[1:]
    
print(getsubsequences("fxyz"))

#time complexity is O(2^n)
#space complexity is O(n)
