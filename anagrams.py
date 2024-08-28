# Calculates the minimum number of deletions required for two strings to be anagrams of each other 

def anagrams (strA, strB):
    # Count both Strings 
    delCount = len(strB) + len(strA)
    # Find how many letters match 
    for letters in strB:
        for lets in strA:
          if(lets==letters):
            delCount -= 2
            

    
    return (delCount)

if __name__ == '__main__':
    stringA = "eeeee"
    stringB = "aef"


    # Function call
    print("Requires: ", anagrams(stringA, stringB), "to be anagrams")