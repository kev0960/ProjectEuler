def primes(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

def div_sum(num, pr):
    ori = num
    exp_cnt = {}
    for p in pr:
        if num == 1:
            break
        while num % p == 0:
            cur = exp_cnt.get(p, 0)
            exp_cnt[p] = cur + 1
            num //= p 
    total = 1
    for b, e in exp_cnt.items():
        total *= (b ** (e + 1) - 1) // (b - 1)
    total -= ori
    return total

p = primes(10000)

divset = {}
rev_div_set = {}

for n in range(1, 10001):
    d = div_sum(n, p)
    divset[n] = d
    ls = rev_div_set.get(d, [])
    ls.append(n)
    rev_div_set[d] = ls

total = 0
amicable = []
for n, d in divset.items():
    if d in divset and n != d:
        nd = divset[d]
        if nd == n:
            amicable.append(n)  
print(amicable)
print(sum(amicable))