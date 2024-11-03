numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
k = 0

for i in numbers:
    for j in range(1, len(numbers)):
        if i % j == 0:
            k +=1
    if k > 2:
        not_primes.append(i)
    else:
        primes.append(i)
    k = 0

print(primes)
print(not_primes)