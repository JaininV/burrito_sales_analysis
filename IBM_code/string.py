# start code
str = input("Give your input: ")

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
    
    # sort array
    y = 0
    for j in range(len(asc_val)):
        for k in range(0, len(asc_val) - j - 1):
            if asc_val[k] >asc_val[k+1]:
                y = asc_val[j]
                asc_val[j] = asc_val[j+1]
                asc_val[j+1] = y
                
    # get string
    final_result = ""
    for i in asc_val:
        ch = chr(i)
        final_result += ch
    return final_result


print(convert_string(str))