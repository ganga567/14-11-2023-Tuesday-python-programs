def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(limit):
    for num in range(2, limit):
        if prime(num):
            print(num)

# Set the limit to 20
limit = 20

# Print prime numbers less than 2
primes(limit)
