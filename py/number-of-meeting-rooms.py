import heapq

def meetingRooms(meetings: [(int, int)]) -> int:
    """ returns the max number of meetings that fit in the schedule """
    meetings.sort() # n * log n

    maxRooms = 0
    endOfMeetings = []

    # get rid of all the meetings that end before the current meeting starts
    for mtg in meetings:
        while endOfMeetings and endOfMeetings[0] <= mtg[0]:
            heapq.heappop(endOfMeetings) # log n

        heapq.heappush(endOfMeetings, mtg[1]) # log n
        maxRooms = max(maxRooms, len(endOfMeetings))

    return maxRooms
















print(meetingRooms([(0, 10), (10, 20)])) # 1
print(meetingRooms([(20, 30), (10, 21), (0, 50)])) # 3