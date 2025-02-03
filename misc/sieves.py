n = 100
primes = [True for _ in range(n+1)]
primes[0]=primes[1] = False

i = 2
while i * i <= n:
    if primes[i]:
        for j in range(i*i,n+1,i):
            primes[j] = False
    i += 1
    
print(primes.count(True))