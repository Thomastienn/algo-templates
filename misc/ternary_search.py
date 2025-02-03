def f(x):
    return (x+2)**2-5

def ternary_search(l, r):
    eps = 10**(-6)
    while r-l > eps:
        m1 = l+(r-l)/3
        m2 = r-(r-l)/3
        
        f1 = f(m1)
        f2 = f(m2)
        if f1 < f2:
            r = m2
        else:
            l = m1
    
    return round(f(l)), round(l)

print(ternary_search(-10, 10))