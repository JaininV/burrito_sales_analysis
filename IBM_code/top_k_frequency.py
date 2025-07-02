# Enter the values:
arr = [1,1,1,2,3,1,2,5,5,4,4,5,6,4,1,2,3]
k = int(input("Enter Frequency: "))

# Funcion for geting frequent values:
def most_frequent_values(num, k):
    n = 0
    l = len(num)
    for i in range(l-1):
        for j in range(l - i -1):
            if num[j] > num[j+1]:
                n = num[j]
                num[j] = num[j+1]
                num[j+1] = nqs  sAS
    
    # Make disc for frequency of each element
    disc = {}
    for i in range(l):
        x = num[i]
        if x in disc:
            disc[x] = disc[x] + 1

        else:
            disc[x] = 1
    
    # return output
    result = {}
    for i in disc:
        if disc[i] >= k:
            result[i] = disc[i]
    
    return result
# call funtion
result = most_frequent_values(arr, k)
print(result)