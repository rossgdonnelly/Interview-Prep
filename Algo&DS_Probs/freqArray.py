
def freq (arr):
    if(arr[0] == None ):
        return
    
    count = {}
    max_count = 0
    max_elem = None

    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1

        if count[i]>max_count:
            max_count = count[i]
            max_elem = i

    return max_elem
    
print(freq([1,2,3,-1,1,13,4,5,6,3,1]))