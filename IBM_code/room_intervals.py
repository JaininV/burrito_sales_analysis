# Set time
meeting = [[0, 30], [5, 10], [15, 20]]

# create function for counting iintervals
def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    # Step 1: Sort meetings by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: List to keep track of end times of meetings in rooms
    rooms = []

    for interval in intervals:
        start, end = interval
        room_found = False

        # Step 3: Try to reuse a room
        for i in range(len(rooms)):
            if start >= rooms[i]:  # Meeting can start after another ends
                rooms[i] = end     # Reuse room by updating end time
                room_found = True
                break

        if not room_found:
            # Need a new room
            rooms.append(end)

    return len(rooms)

result = min_meeting_rooms(meeting)
print(result)