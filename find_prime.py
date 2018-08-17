
def check_even(n):
    if (n%2)==0:
        print(n, "is even")
    else:
        print(n,"is odd")
    return



for start in range(2,10):
    check_even(start)




# def check_prime(n):
#      isPrime = True
#      for start in range(2, n-1):
#         if (n % start) == 0:
#             isPrime = False
#             break
#
#      if (isPrime == False):
#          print(n,"is not prime")
#      else:
#          print(n, "is prime")
#      return
#
#
# for i in range(2, 5000000000000001):
#     check_prime(i)
