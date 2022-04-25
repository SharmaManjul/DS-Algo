from heapq import *

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end

def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)

    min_rooms, room_counter = 0, 0
    min_heap = []

    for meeting in meetings:
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)
            room_counter -= 1
        heappush(min_heap, meeting)
        room_counter += 1
        min_rooms = max(min_rooms, room_counter)
    return min_rooms

def min_meeting_rooms_two_pointer(meetings):
    start_times = sorted([meeting.start for meeting in meetings])
    end_times = sorted([meeting.end for meeting in meetings])

    start, end, min_rooms, room_counter = 0, 0, 0, 0

    while start < len(start_times):
        if start_times[start] < end_times[end]:
            start += 1
            room_counter += 1
        else:
            end += 1
            room_counter -= 1
        min_rooms = max(min_rooms, room_counter)
    return min_rooms

def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
    str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
    str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
    str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))

main()
