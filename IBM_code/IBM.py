# ---------------------------------------------------------------------------------------------------------------hcf---------------------------------------------------------------------------------------------------------------------
val = []
for i in range(1, 3):
    x = int(input("Enter value: "))
    val.append(x)

# write a code for checking possible HCF for each
hcf_1 = []
hcf_2 = []

val_1 = []
val_2 = []

for i in range(1, val[0]+1):
    val_1.append(i)

for i in range(1, val[1]+1):
    val_2.append(i)

# check which value give division 0
for i in val_1:
    x = val[0]%i
    if x == 0:
        hcf_1.append(i)
    

for i in val_2:
    x = val[1]%i 
    if x == 0:
        hcf_2.append(i)

# give same hcf
sam_val = []
for i in range(1, len(hcf_1)):
    if hcf_1[i] in hcf_2:
        sam_val.append(hcf_1[i])

print(sam_val)


# ------------------------------------------------------------------------------------------task2-------------------------------------------------------------------------------------