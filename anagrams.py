# Calculates the minimum number of deletions required for two strings to be anagrams of each other 

def anagrams (strA, strB):
    # Count both Strings
    
    if len(strB)>len(strA):
       lnStr = strB
       srStr = strA
    else:
       lnStr = strA
       srStr = strB
    matchStr = []
    delCount = len(strB)+len(strA)
    # Find how many letters match 
    for letters in lnStr:
        for lets in srStr:
          if (letters == lets):
              #delete from both sides
              matchStr.append(letters)
              lnStr = lnStr.replace(letters,'',1)  
              srStr = srStr.replace(letters,'',1) 
               
    
    delCount = len(lnStr) + len(srStr)
            
    print(matchStr) 
    return (delCount)

if __name__ == '__main__':
    stringA = "fcrxzwscanmligyxyvym"
    stringB = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"


    # Function call
    print("Requires: ", anagrams(stringA, stringB), "to be anagrams")