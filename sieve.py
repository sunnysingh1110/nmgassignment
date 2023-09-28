#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sieve_eratosthenes(limit):
    # Create a boolean array "is_prime" of size (limit+1) and initialize all entries as True
    is_prime = [True] * (limit + 1)
    
    # 0 and 1 are not prime numbers
    is_prime[0] = is_prime[1] = False
    
    # Start with the first prime number, 2
    p = 2
    while p**2 <= limit:
        # If is_prime[p] is still True, then it is a prime number
        if is_prime[p]:
            # Mark all multiples of p as composite
            for i in range(p**2, limit+1, p):
                is_prime[i] = False
        p += 1
    
    # Collect the prime numbers into a list
    primes = [p for p in range(2, limit+1) if is_prime[p]]
    
    return primes

# Example usage
limit = 50
prime_numbers = sieve_eratosthenes(limit)
print("Prime numbers up to", limit, "are:", prime_numbers)

