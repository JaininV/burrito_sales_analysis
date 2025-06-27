num = int(input("Enter nummber: "))

def convert_number_iin_digit(data):
    n = data
    sum = 0
    while n > 0:
        i = n%10
        sum = i + sum
        n = int(n/10)
    
    return sum
result = convert_number_iin_digit(num)
print(result) 