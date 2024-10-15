# Iterative Approach
num = int(input("Enter the number: "))
f = 1
for i in range(1, num + 1):
    f = f * i

print("Iterative Approach \nFactorial of", num, "is", f)
print()

# Recursive Function
def factorial(n):
    if n < 1:
        return 1
    else:
        fact = n * factorial(n - 1)
        return fact

num = int(input("Enter the number: "))
print("Recursive Approach \nFactorial is:", factorial(num))
