numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for el in numbers:
    if el < 2: continue
    is_prime = True
    for i in range(2, el // 2 + 1):
        if el % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(el)
    else:
        not_primes.append(el)
print('Primes:', primes)
print('Not Primes:', not_primes)