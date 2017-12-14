import input
import rw
import output

#main block

eventlist=input.geteventlist()
threadlist=[]                                                                                                           #maybe no needs of list?
for i in range(1,eventlist[0].counter):                                                                                 #create RWthreads
    rw_lock=rw.RWLock
    if eventlist[i].showtype()==1:
        threadlist.append(rw.Writer(rw_lock,sleeptime=eventlist[i].showdelay(),exctime=eventlist[i].showtime()))        #maybe no needs of list?

    else:
        threadlist.append(rw.Reader(rw_lock,sleeptime=eventlist[i].showdelay(),exctime=eventlist[i].showtime()))        #maybe no needs of list?

