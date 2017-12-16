
import colorsys

def R_Access(id):
    print('\033[0;31;40m','Reader:','\033[0;30m',id,'is accessing resource now')

def R_leave(id):
    print('\033[0;31;40m', 'Reader:','\033[0;30;46m',id, 'has finished access resource')

def W_Access(id):
    print('\033[0;35;40m', 'Writer:', '\033[0;30m', id, 'is accessing resource now')

def W_leave(id):
    print('\033[0;35;40m', 'Writer:','\033[0;30;46m',id, 'has finished access resource')



'''R_Access(3023)
R_leave(2411)
W_Access(3023)
W_leave(2411)'''