import Tkinter as tk
from Tkinter import *
import ScrolledText
import ttk
from ttk import Treeview
import class_WR
import random
import rw

#create a window object
root = tk.Tk()
#name the window as'Group 14'
root.title('Group 14 12/21 RW Problem')

#create a label which display on the 'Group 14'window, and define its attributes
ltopic = tk.Label(root,text='RW Problem by Group 14', bg = 'light blue',font = ('Times New Roman',14), width = 30, height = 2)

#Create a LabelFrame for input area and log area
lf = tk.LabelFrame(root, text='Input',font=('Times New Roman',14))
lf_p = tk.LabelFrame(root, text='Log',font=('Times New Roman',14))
lf_o = tk.LabelFrame(root,text='Result',font=('Times New Roman',14))


#Create 4 labels for input area
l1 = tk.Label(lf,text='Input the amount of events (1~10000)  ',font = ('Times New Roman',12))
l2 = tk.Label(lf,text='Input the proportion of reader and writer   ',font = ('Times New Roman',12))
l3 = tk.Label(lf,text='Input the maximum produce delay (1~100)   ',font = ('Times New Roman',12))
l4 = tk.Label(lf,text='Input the maximum access time (1~100)  ',font = ('Times New Roman',12))

#create scrollbar for Log and Result table
scrlbr = tk.Scrollbar(lf_p)
scrRs = tk.Scrollbar(lf_o)

#Create table for Log
tree = ttk.Treeview(lf_p,yscrollcommand=scrlbr.set)
tree["columns"] = ["a","b","c","d","e"]
tree.column("a",width = 150,anchor = 'center')
tree.column("b",width = 150,anchor = 'center')
tree.column("c",width = 150,anchor = 'center')
tree.column("d",width = 150,anchor = 'center')
tree.column("e",width = 150,anchor = 'center')
tree.heading("a",text = 'R/W')# if it is the reader or the writer
tree.heading("b",text = 'Thread ID')
tree.heading("c",text = 'Access Time')#the time it enter the critical section
tree.heading("d",text = 'Sleeping Time')
tree.heading("e",text = 'Execution Time')#the time it costs to run the whole critical section

#Create table for Result
result = ttk.Treeview(lf_o,yscrollcommand=scrRs.set)
result["columns"] = ('A','B','C','D')
result.column("A",width = 70,anchor = 'center')
result.column("B",width = 70,anchor = 'center')
result.column("C",width = 70,anchor = 'center')
result.column("D",width = 70,anchor = 'center')
result.heading("A",text = 'Order')#The order of running
result.heading("B",text = 'R Amount')
result.heading("C",text = 'W Amount')
result.heading("D",text = 'Winner')#Reader or Writer is the winner

#bind the table and the scrollbar
scrlbr.config(command=tree.yview)
scrRs.config(command=result.yview)

#open defaultset.txt, read it, split it, turn into list, and convert each list's element to int, then put them back to the original list
dftset = open('defaultset.txt')
r = dftset.read()#type(r) is a string
r_list = list(r.split())
for i in range(len(r_list)):
	r_list[i] = int(r_list[i])

#Create a StringVar object, and set each value as the elements of r_list
e1t = StringVar(lf,value = r_list[0])
e2t = StringVar(lf,value = r_list[1])
e3t = StringVar(lf,value = r_list[2])
e4t = StringVar(lf,value = r_list[3])
#Create an entry for each input, with default value in each entry
e1 = tk.Entry(lf,font = ('Times New Roman',12),textvariable = e1t)
e2 = tk.Entry(lf,font = ('Times New Roman',12),textvariable = e2t)
e3 = tk.Entry(lf,font = ('Times New Roman',12),textvariable = e3t)
e4 = tk.Entry(lf,font = ('Times New Roman',12),textvariable = e4t)


#arrange the locations
ltopic.grid(row=0,column=0,ipadx=5)
lf.grid(columnspan=3,rowspan=6,padx=5,pady=5,ipadx=5,ipady=5)
l1.grid(row=2,column=0,sticky='W')
e1.grid(row=2,column=1,sticky='E')
l2.grid(row=3,column=0,sticky='W')
e2.grid(row=3,column=1,sticky='E')
l3.grid(row=4,column=0,sticky='W')
e3.grid(row=4,column=1,sticky='E')
l4.grid(row=5,column=0,sticky='W')
e4.grid(row=5,column=1,sticky='E')

lf_p.grid(columnspan=6,rowspan=9,padx=5,pady=5,ipadx=5,ipady=5)
tree.grid(row=2,column=5,sticky='NSEW')
scrlbr.grid(row=2,column=8,sticky='NS')

lf_o.grid(columnspan=4,rowspan=9,padx=5,pady=5,ipadx=5,ipady=5)
result.grid(row=7,column=0,sticky='NSEW')
scrRs.grid(row=7,column=4,sticky='NS')

tree.rowconfigure(0,weight=1)
result.rowconfigure(6,weight=1)


#function of button start
def ClickStart():
     #global elist
     paralist = [int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get())]
     eventlist = []
     for i in range(0, paralist[0]):
         if (random.randint(0, 10000)) < (10000 / (paralist[1] + 1)):
             eventlist.append(class_WR.events(1, paralist[2], paralist[3]))
         else:
             eventlist.append(class_WR.events(0, paralist[2], paralist[3]))

             threadlist = []

     for i in range(0, eventlist[0].counter):  # create RWthreads
         rw_lock = rw.RWLock()
         if eventlist[i].showtype() == 1:
             threadlist.append(rw.Writer(rw_lock, sleeptime=eventlist[i].showdelay(), exctime=eventlist[i].showtime(),id=eventlist[i].showid()))
         else:
             threadlist.append(rw.Reader(rw_lock, sleeptime=eventlist[i].showdelay(), exctime=eventlist[i].showtime(),id=eventlist[i].showid()))

     for i in range(0, eventlist[0].counter):  # run RWthreads
         loglist=threadlist[i].run()
         TYPE=loglist[0]
         ID=loglist[1]
         ITIME=loglist[2]
         STIME=loglist[3]
         ETIME=loglist[4]
         tree.insert('', i, values=(TYPE,ID,ITIME,STIME,ETIME))
    
#create a button
b = tk.Button(lf,text='Start',font=('Times New Roman',12),width=10, height=1,command=ClickStart)
b.grid(row=6,column=1)




root.mainloop()
