def sumPairs(arr, k):
    seen = set()
    output = set()


    for number in arr:
      target = k - number
      if target not in seen:
         seen.add(number)
      else:
         output.add((number, target)) 
            

       

            

    return map(str, list(output))

      



if __name__ == '__main__':
    arr = [1,3,2,2]
    k = 4
    # Function call
    print("Output: ",sumPairs(arr, k))
