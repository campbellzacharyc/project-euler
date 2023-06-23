# The prime factors of 13195 are 5, 7, 13, 29
# What is the largest prime factor of the number 600851475143

def prime_factors(num):
    prime_factors_list = []
    divisor = 2 
    
    while divisor <= num:
        if num % divisor == 0:
            prime_factors_list.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return print(prime_factors_list)

    
    
prime_factors(600851475143)