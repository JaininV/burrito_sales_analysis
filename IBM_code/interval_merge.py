# # define class
# class intervals:
#     def __init__(self):
#         # 

inp = [[1, 4], [4, 5], [10, 12], [11, 15], [20, 25], [22, 30]]

# making a function for remove intervals
def remove_intervals(arr):
    arr = sorted(arr, key=lambda x: x[0])
    out = [arr[0]]
    
    for i in range(1, len(arr)):
        last = out[-1]
        current = arr[i]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        
        else:
            out.append(current)
        
    print(out)


remove_intervals(inp)