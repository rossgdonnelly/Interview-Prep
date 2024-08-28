
import heapq

#Simplest Method
def simpleMethod(arr, k, N):
    arr.sort()
    return(arr[k-1]) 

#Time Complexity: O(N log N)
#Auxiliary Space: O(1) 

#Queue Method 
def queueMethod(arr,k):
    queue = []
    for num in arr:
        heapq.heappush(queue, -num)
        if(len(queue)>k):
            heapq.heappop(queue)
    return-queue[0]

if __name__ == '__main__':
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    K = 4    
    N = len(arr)
  
    # Function call
    print("K'th smallest element is",queueMethod(arr, K))