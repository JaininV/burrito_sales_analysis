# Enter the values:
arr = [1,1,1,2,3,1,2,5,5,4,4,5,6,4,1,2,3]
k = input(int("Enter Frequency: "))

# Funcion for geting frequent values:
def most_frequent_values(num, k):
    n = 0
    l = len(num)
    for i in range(0, l):
        for j in range(0, l - i -1):
            n = num[i]
            num[i] = num[j]
            num[j] = n
    
    print(num)

# call funtion
most_frequent_values()