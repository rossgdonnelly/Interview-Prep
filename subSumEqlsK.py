def subArraySum (arr, k):
    sumCount=0
    i=0      
    while i<len(arr)-1:
        sum = arr[i+1]+arr[i] 
        if(sum == k):
            sumCount+=1
        i+=1
    return (sumCount)

if __name__ == '__main__':
    arr = [1,2,3]
    K = 3   

    # Function call
    print("Sums: ",subArraySum(arr, K))
    