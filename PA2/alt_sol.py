def primes(a, b):
    if a > b or a < 1:
        raise ValueError("Invalid range.")
    if a == 1:
        a = 2
    ps = []
    for n in range(a, b+1):
        is_prime = True
        for k in range(2, n):
            if n % k == 0:
                is_prime = False
        if is_prime:
            ps.append(n)
    return set(ps)

def bezout_coeffs(a, b):
    def helper(a, b):
        if a == 0:
            return (0, 1)
        else:
            x, y = helper(b % a, a)
            return (y - (b // a) * x, x)
    return dict(zip([a, b], helper(a, b)))