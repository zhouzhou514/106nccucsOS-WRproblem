import input
import rw
#main block

eventlist=input.geteventlist()
threadlist=[]                                                                                                           #maybe no needs of list?
for i in range(0,eventlist[0].counter-1):                                                                                 #create RWthreads
    rw_lock=rw.RWLock()
    #print(eventlist[i].showdelay())
    if eventlist[i].showtype()==1:
        threadlist.append(rw.Writer(rw_lock,sleeptime=eventlist[i].showdelay(),exctime=eventlist[i].showtime(),id=1+eventlist[i].showid()))#maybe no needs of list?
        threadlist[i].run()
    else:
        threadlist.append(rw.Reader(rw_lock,sleeptime=eventlist[i].showdelay(),exctime=eventlist[i].showtime(),id=1+eventlist[i].showid()))#maybe no needs of list?
        threadlist[i].run()
