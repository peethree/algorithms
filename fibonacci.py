def fib(n):
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    grandparent = 0  
    parent = 1          

    # n-2 times 
    for i in range(1, n):
        # Calculate the next Fibonacci number
        current = parent + grandparent
        
        # Update parent and grandparent for the next iteration
        grandparent = parent
        parent = current

    return current