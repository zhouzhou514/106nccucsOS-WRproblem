import class_WR
import input

#main block

eventlist=input.geteventlist()
print(eventlist[0].counter)
for i in range(0,eventlist[0].counter):
    print(eventlist[i].showid())
