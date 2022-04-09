from re import A


a = 24
b = 90
c = 8
d = 13
x = a + b
y = c*c + a 
z = x + y + d

#Calculates nth fibonacci number
#what is fibonacci number f(n) = f(n-1) + f(n-2)
#e.g. if n = 3 f(3) = f(2) + f(1) => f(3) = f(1) + f(0) + f(1)
# => f(3) = 1 + 0 + 1 = 2
# Another example f(5) = f(4) + f(3) => f(3) + f(2) + f(3) => 2 + 1 + 2 => 5
def fibonacci(n : int) :
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))