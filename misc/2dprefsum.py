a = [[10, 20, 30], [5, 10,20], [2, 4, 6]]

for r in a:
    print(r)
print()

pref = [[0 for _ in range(3)] for _ in range(3)]

pref[0][0] = a[0][0]
for i in range(1, 3):
    pref[0][i] = pref[0][i-1] + a[0][i]
    pref[i][0] = pref[i-1][0] + a[i][0]
    
for i in range(1, 3):
    for j in range(1, 3):
        pref[i][j] = pref[i-1][j] + pref[i][j-1] \
                    - pref[i-1][j-1] + a[i][j]

for r in pref:
    print(r)