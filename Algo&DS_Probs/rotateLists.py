
#Must be unique Elements in each array

def rotate (list1, list2):

    if(len(list2) != len(list1)):
        return False

    start = list1[0]
    index = -1

    for x in range(len(list2)):
        if (start == list2[x]):
            index = x
            break
    if(index ==-1):
        return False

    for i in range(len(list1)):
        l2index = (index + i) % len(list1)
        if list1[i] != list2[l2index]:
            return False 
        
    return True
        
print (rotate([1,2,3,1,1,1], [3,1,1,1,1,2]))