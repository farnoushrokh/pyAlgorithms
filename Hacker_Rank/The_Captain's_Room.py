"""
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of  members per group where  ≠ .

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of  and the room number list.

Input Format

The first line consists of an integer, , the size of each group.
The second line contains the unordered elements of the room number list.
"""
#First Method
k = 5
rooms = [1,2,3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
def Captains(k, rooms):
    dict_ = dict()
    if k != 1:
        for i in range(len(rooms)):
            dict_[rooms[i]] = rooms.count(rooms[i])
        for k,v in dict_.items():
            if v == 1:
                return k
#Second Method
k=input();
rooms=input().split();
if k != 1:
    for i in sorted(rooms):
        if rooms.count(i) ==1:
            print(i)

#Third Method
k=input();
rooms=input().split();
set1=set();  #all unique room number
set2=set();  #all unique room number occur more than once
for i in rooms:
    if  i in set1:
        set2.add(i);
    else:
        set1.add(i);
set3=set1.difference(set2);
print(list(set3)[0])
