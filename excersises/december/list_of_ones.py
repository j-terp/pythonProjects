FibArray = [0,1] 
  
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib
def prime(val):
    # If num is divisible by any number   
    # # between 2 and val, it is not prime  
    if val > 1: 
        for n in range(2, val): 
            if (val % n) == 0: 
                break
    else: 
        print(val)
list_of_fibonacci = []
list_of_prime = []
for i in range(200):
    list_of_fibonacci.append(fibonacci(i + 1))
    list_of_prime.append(prime(i + 1))
print(list_of_fibonacci)
print(list_of_prime)