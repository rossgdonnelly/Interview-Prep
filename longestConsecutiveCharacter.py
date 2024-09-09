def longestConsecutiveCharacter(string):
    print(string)
    listStr = list(string)
    current = listStr[0]
    maxCount = 0 
    currentCount = 0
    i=0
    max_char = ''
    while i<len(listStr):
        current = listStr[i]
        if (current == listStr[i-1]):
            currentCount +=1
            if currentCount>=maxCount:
                maxCount = currentCount
                max_char = current
        else:
            currentCount = 0
        i +=1
    return {max_char: maxCount+1}

      

    

    #Sum up the even numbers


if __name__ == '__main__':
    string = "ROsssssss"
    # Function call
    print("Output: ",longestConsecutiveCharacter(string))
