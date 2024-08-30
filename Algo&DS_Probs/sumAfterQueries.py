def sumEvenAfterQueries(nums, queries):
    print(nums)
    sum=0
    sums = []

    for query in queries:
        position = query[1]
        command = query[0]
        nums[position] += command
        for numbers in nums:
            if(numbers%2==0):
                sum+=numbers
        sums.append(sum)
        print(sums)
        sum=0

    #Sum up the even numbers


if __name__ == '__main__':
    nums = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    # Function call
    print("Output: ",sumEvenAfterQueries(nums, queries))
    print(nums)