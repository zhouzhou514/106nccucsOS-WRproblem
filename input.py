import class_WR
import random
import UI_input

def getparameter():
    ins='f'
    while ins!='d'and ins!='s'and ins!='q':
        ins=raw_input("-use default file, input d\n-use your parameter,input s\n-input q to exit\n")
        if ins=='d':
            dff=open("defaultset.txt","r")
            numofevents,proportion,maxD,maxT=[int(x)for x in next(dff).split( )]
            dff.close()

        elif ins=='s':
            numofevents=int(input("in put the amounts of events (1~10000)"))
            proportion=int(input("input the proportion of reader:writer"))
            maxD=int(input("input the maximun produce delay (1~100)"))
            maxT=int(input("input the maximun access time (1~100)"))

        elif ins=='q':
            exit(0)
        else:
            pass

    paralist=[numofevents,proportion,maxD,maxT]
    return paralist



def geteventlist():
    #paralist=getparameter()
    paralist=UI_input.input_UI()
    #print(paralist)
    eventlist =[]

    for i in range(1, paralist[0]):

        if (random.randint(0,10000))<(10000/(paralist[1]+1)):
            eventlist.append( class_WR.events(1, paralist[2], paralist[3]))

        else:
            eventlist.append(class_WR.events(0,paralist[2],paralist[3]))


    return eventlist
