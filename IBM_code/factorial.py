# get input by user
def factorial(number):
    x = number
    fac = 1
    while 1 <= number:
        fac = fac*number
        number = number - 1
    
    return f"Factorial of {x} is {fac}."

num = int(input("Enter your desire number: "))
result = factorial(num)
print(result) 