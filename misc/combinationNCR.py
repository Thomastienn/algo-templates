MOD = 10**9+7
MAXN = 10**3
MAXK = 102

# DP[i][j] : Total of i items, choose j of them
# O(N*K) query O(1)
dp = [[0]*MAXK for _ in range(MAXN)]
for i in range(MAXN):
    dp[i][0] = 1
for i in range(1, MAXN):
    for j in range(1, MAXK):
        dp[i][j] = (dp[i][j] + dp[i-1][j-1] + dp[i-1][j])%MOD
    

# FASTER WAY WITH FACTORIAL
# O(NLOG(MOD)) query O(1)
fact =[1]
inv = [1]
for i in range(1,(MAXN+1)):
    fact.append(pow(fact[-1]*i,1,MOD))
    inv.append(pow(fact[-1],-1,MOD))

def comb(n, k):
    if n < k:
        return 0
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD
        
        
    
# FASTEST WAY
# O(N + LOG(MOD))
# OR QUERY in O(1) WITH FERMAT LITTLE THEOREM
fact = [1] * (MAXN + 1)
inv = [1] * (MAXN + 1)

for i in range(2, MAXN + 1):
    fact[i] = fact[i - 1] * i % MOD

# Compute modular inverses using Fermat's Little Theorem
inv[MAXN] = pow(fact[MAXN], MOD - 2, MOD)  # Modular inverse of MAXN!
for i in range(MAXN - 1, 0, -1):
    inv[i] = inv[i + 1] * (i + 1) % MOD

# Function to compute nCr % MOD
def nCr(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD

# Example usage:
print(nCr(20, 6))