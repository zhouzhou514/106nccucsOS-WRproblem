


def R_Created(id,sleeptime,exctime):
    print '\033[0;31;40m', 'Reader:','\033[0;30m',id,'is created','\033[0;31m','sleeptime:',sleeptime,'exctime',exctime

def R_Access(id):
    print '\033[0;31;40m','Reader:','\033[0;33;42m',id,'is accessing resource now'

def R_leave(id):
    print '\033[0;31;40m', 'Reader:','\033[0;33;46m',id, 'has finished access resource'

def W_Created(id,sleeptime,exctime):
    print '\033[0;35;40m', 'Writer:','\033[0;30m',id,'is created','\033[0;31m','sleeptime:',sleeptime,'exctime',exctime

def W_Access(id):
    print '\033[0;35;40m', 'Writer:', '\033[0;33;42m', id, 'is accessing resource now'

def W_leave(id):
    print '\033[0;35;40m', 'Writer:','\033[0;33;46m',id, 'has finished access resource'


'''R_Created(1000)
R_Access(3023)
R_leave(2411)
W_Access(3023)
W_leave(2411)
W_Created(1880)'''