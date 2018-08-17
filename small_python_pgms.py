
# Find all factors of n


def find_factors(n):
    factors = []

    for i in range(1, n+1):
        if (n % i ) == 0:
            factors.append(i)
    return factors


# number = int(input("please enter number: "))
# print("factors are ", find_factors(number))

# Primes up to n


def primes_upn(n):
    prime = []

    for i in range(2, n+1):
        if find_factors(i) == [1, i]:
            prime.append(i)
    return prime


# list_nprimes = int(input("Enter prime up to which number you want: "))
# print("list of prime", primes_upn(list_nprimes))


# First n primes

def first_nprimes(n):
    first_np = []
    count = 0
    start = 2
    while count < n:
        if find_factors(start) == [1, start]:
            first_np.append(start)
            count = count + 1

        start = start + 1

    return first_np


first_np = int(input("Enter number for first n prime: "))
print(first_nprimes(first_np))


