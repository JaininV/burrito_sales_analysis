num = int(input("Enter your number: "))

def convert_binary(data):
    bin = []
    n = data    
    while n>0:
        i = n%2
        bin.append(i)
        n = int(n /2)
    
    return bin

result = convert_binary(num)
print(result) 
