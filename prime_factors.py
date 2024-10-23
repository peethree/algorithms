import math

def prime_factors(n):
    # return list of prime factors 
    # 8->[2, 2, 2]
    # 10->[2, 5]
    # 24->[2,2,2,3]  
    list = []

    while n % 2 == 0:
        n = n/2
        list.append(2)

    if n == 1:
        return list    
    
    n = int(n)

    odd_numbers = []
    # At this point, n must be odd. Start a loop that iterates over all odd numbers 
    # from 3 to the square root of n inclusive. Use math.sqrt().    
    for i in range(3, n + 1, 2):
        odd_numbers.append(i)

    # For each number i, if n can be divided evenly by i, then divide n by i and append i to the list. 
    # Repeat this (nested loop) until i can't divide evenly into n, then move on to the next i.
    for num in odd_numbers:
        while n % num == 0:
            n = n/num
            list.append(num)

    return list      
    


"""
import math


def prime_factors(n):

    prime_factors = []
    while n % 2 == 0:
        n /= 2
        prime_factors.append(2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= i
            prime_factors.append(i)

    if n > 2:
        prime_factors.append(int(n))
        
    return prime_factors

    """