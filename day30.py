# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n*factorial(n-1)


# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
def fibo(n):
    if n <= 1:
        return n

    else:
        return (fibo(n-1)+fibo(n-2))


nterms = int(input("How many terms?"))
for i in range(nterms):
    print(fibo(i))
