n = 100
ca = [0]*(n+1)
ca[0] = ca[1] = 1
MOD = 10**5

for i in range(2, n+1):
    for j in range(i):
        ca[i] = (ca[i] + ca[j]*ca[i-j-1]%MOD)%MOD
