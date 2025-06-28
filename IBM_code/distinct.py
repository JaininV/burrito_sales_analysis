txt = input("Enter your text: ")
k = int(input("Enter limit: "))

# define a function
def disticnt_txt(txt, limit):
    txt = txt.replace(" ", "")
    txt = txt.lower()
    l = len(txt)
    dis_arr = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    if l>=limit:
        for i in range(limit):
            if txt[i] in dis_arr:
                count += 1

            else:
                continue
        return count
    
    else:
        return "Text length is lower than limit!"

result = disticnt_txt(txt, k)
print(result)