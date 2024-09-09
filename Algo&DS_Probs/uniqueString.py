
def unique (str):
    str = str.replace(' ',',')
    print(str)
    elems = []


    for i in str:
        if i not in elems:
            elems.append(i)
        else:
            return False
    return True
    

    
print(unique("abcdefghijklmnoap"))