def leftRotate (arr, n):
    tempArr = []
    tempArr2 = []

    index = 0
    while index<n:
        tempArr2.append(arr[index])
        index+=1
    index=n
    while index < len(arr):
        tempArr.append(arr[index])
        index+=1
    
    arr = tempArr + tempArr2
    
    return (arr)

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    N = 4   

    # Function call
    print("New Array",leftRotate(arr, N))