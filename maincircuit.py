import rw
#main block

def mainblock(eventlist):

    threadlist=[]

    for i in range(0,eventlist[0].counter):#create RWthreads
        rw_lock=rw.RWLock()
        if eventlist[i].showtype()==1:
            threadlist.append(rw.Writer(rw_lock,sleeptime=eventlist[i].showdelay(),exctime=eventlist[i].showtime(),id=eventlist[i].showid()))
        else:
            threadlist.append(rw.Reader(rw_lock,sleeptime=eventlist[i].showdelay(),exctime=eventlist[i].showtime(),id=eventlist[i].showid()))

    for i in range(0,eventlist[0].counter):#run RWthreads
        threadlist[i].run()
