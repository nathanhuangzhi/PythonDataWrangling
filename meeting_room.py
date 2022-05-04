# time_interval = [[10,20],[20,40],[50,60],[30,50], [40,50],[20,30],[25,35]]
#
# start_time = [x[0] for x in time_interval]
# start_time.sort()
# end_time = [x[1] for x in time_interval]
# end_time.sort()
#
# organized = [0]
# count = 0
# for i in range(1,len(start_time)):
#
#     if i in organized:
#         next
#     else:
#         for j in range(i,len(start_time)):
#             if (i == j):
#                 continue
#             else:
#                 if end_time[i] <= start_time[j]:
#                     organized.append(j)
#
#                 else:
#                     next
#         count = count + 1
# print(count)
#

def meeting_room(l):

    start_time = [x[0] for x in l]
    end_time = [x[1] for x in l]

    start_time.sort()
    end_time.sort()

    for i in range(len(start_time)-1):

        meeting_end = end_time[i]
        next_meeting = start_time[i+1]

        if meeting_end > next_meeting:
            return False


    return True


print(meeting_room([[10,20],[20,40],[50,60]]))
