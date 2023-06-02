def large_prime_factor(num):


    primeFactor = 1
    i=2 
    while i<=num/1:
        if num % i == 0:
            primeFactor = i
            num=num/i
        else:
            i = i +1
    if primeFactor<num:
        primeFactor = num
    return primeFactor

print(large_prime_factor(600851475143))

