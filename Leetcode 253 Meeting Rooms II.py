#Leetcode 253 Meeting Rooms II

class Meeting_Time():
    def __init__(self,start,end,lst):
        self.start = start
        self.end = end
        lst.append(self)
def Find_Room(lst):
    '''list of the meeting time'''
    lst.sort(key = lambda x : x.start)
    room_required = 1
    new_lst = [lst[0]]
    for i in range(1,len(lst)-1):
        if lst[i].start < new_lst[0].end:
            room_required += 1
            #new_lst.append(lst[i])
        else:
            new_lst.pop(0) 
        new_lst.append(lst[i])
    
    return room_required
lst=[]

A = Meeting_Time(1,4,lst)
B = Meeting_Time(2,8,lst)
C = Meeting_Time(5,7,lst)
D = Meeting_Time(5,9,lst)
E = Meeting_Time(3,4,lst)
#print (lst)
#lst = [A,B,C,D,E]
result = Find_Room(lst)
print (result)