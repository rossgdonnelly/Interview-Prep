

#Simplest Method
def fibonacci(seq):
    result = 0
    i = 0
    a = 1
    b = 1
    if seq==1:
        return(1)
    elif seq>1:
        #find it
        while i<=seq:
            result = a+b
            b = a
            a = result
            i+=1
            print(result)
    return(result) 

# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    seq = 0
  
    # Function call
    print("Output: ",fibonacci(seq))