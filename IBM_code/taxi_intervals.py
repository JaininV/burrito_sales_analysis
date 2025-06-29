start = [1,2,3,4,5,6,7,8,9]
end = [2,3,4,5,6,7,8,9,10]

# function for remove intervals of taxi
def remove_taxi_interval(start, end):
    route = []
    for i in range(len(start)):
        route.append([start[i], end[i]])
    
    route = sorted(route, key=lambda x: x[0])
    demo = [route[0]]

    # found total interval:
    for i in range(1, len(route)):
        last = demo[-1]
        current = route[i]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            demo.append(current)

    print(len(demo))
remove_taxi_interval(start, end)