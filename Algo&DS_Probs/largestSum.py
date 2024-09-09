def largestSum(arr):


    #Check if big enough first 
    if len(arr) ==0:
       return 

    maxSum = currentSum = arr[0]
    for num in arr[1:]:
      currentSum = max(currentSum + num, num)
      maxSum = max(currentSum, maxSum)
    
        

    return maxSum

      



if __name__ == '__main__':
    arr = [1,3,-5,2,2]

    # Function call
    print("Output: ",largestSum(arr))
