def factorial(k):
    if k < 2:
     return 1
    else:
        return k * factorial(k-1)
n = int(input('Enter a number: '))
result = factorial(n)
print('Factorial of ' , n ,' is:',result)