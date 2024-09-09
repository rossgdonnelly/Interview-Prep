
#Between 2 sorted arrays!!!

def commonElem (list1, list2):

    pointer1 = 0
    pointer2 =  0
    elems = []

    while pointer1 < len(list1) & pointer2<len(list2):
        if list1[pointer1] == list2[pointer2]:
            elems.append(list1[pointer1])
            pointer1+=1
            pointer2+=1
        elif list1[pointer1] > list2[pointer2]:
            if list1[pointer1] % list2[pointer2] == 0:
                elems.append(list1[pointer1])
            pointer2 +=1

        elif list1[pointer1] < list2[pointer2]:
            if list2[pointer2] % list1[pointer1] == 0:
                elems.append(list1[pointer1])
            pointer1+=1




    return elems
    


        
print (commonElem([1,2,3], [1,3]))