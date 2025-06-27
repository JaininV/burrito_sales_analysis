# start code
str = input("Give your input: ")

# sort array
def sorting_arr(data):
    arr = data
    l = len(arr)
    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                k = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = k
    return arr

# converting ascii value in chr
def convert_chr(data):
    result = ""
    print(data)
    for i in data:
        x = chr(i)
        result += x
    return result
    
def convert_string(str):
    result = ""
    for i in str: 
        x = ord(i)
        if 48<= x <= 57:
            continue
        else:
            result += i
    
    # convert in acd order
    asc_val = []
    for i in result:
        asc = ord(i)
        if asc not in asc_val:
            asc_val.append(asc)
    
    # call sorting array code
    asc_val = sorting_arr(asc_val)
    clean_chr = convert_chr(asc_val)            
 
    return clean_chr

print(convert_string(str))