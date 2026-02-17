def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(numbers):
    primes = []
    for n in numbers:
        if is_prime(n):
            primes.append(n)
    return primes


result = get_primes([1, 4, 6, 7, 13, 9, 67])
print(result)  