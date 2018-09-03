def primes(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

def num_divs(num, pr):
    exp_cnt = {}
    for p in pr:
        if num == 1:
            break
        while num % p == 0:
            cur = exp_cnt.get(p, 0)
            exp_cnt[p] = cur + 1
            num /= p 
    total = 1
    for _, e in exp_cnt.items():
        total *= (e + 1)
    return total

p = primes(2000000)

for n in range(1, 2000000):
    tri = n * (n + 1) // 2
    if num_divs(tri, p) >= 500:
        print(tri)
        break