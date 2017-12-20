import Tkinter as tk
from Tkinter import *
import ScrolledText
import ttk
from ttk import Treeview


#create a window object
root = tk.Tk()
#name the window as'Group 14'
root.title('Group 14 12/21 RW Problem')
#define the size of the window
root.geometry('1000x600')


#create a label which display on the 'Group 14'window, and define its attributes
ltopic = tk.Label(root,text='RW Problem by Group 14', bg = 'light blue',font = ('Times New Roman',14), width = 30, height = 2)


#Create a LabelFrame for input area and log area
lf = tk.LabelFrame(root, text='Input',font=('Tims New Roman',14))
lf_p = tk.LabelFrame(root, text='Log',font=('Tims New Roman',14))


#Create 4 labels for input area
l1 = tk.Label(lf,text='Input the amount of events (1~10000)  ',font = ('Times New Roman',12))
l2 = tk.Label(lf,text='Input the proportion of reader and writer   ',font = ('Times New Roman',12))
l3 = tk.Label(lf,text='Input the maximum produce delay (1~100)   ',font = ('Times New Roman',12))
l4 = tk.Label(lf,text='Input the maximum access time (1~100)  ',font = ('Times New Roman',12))


#create scrollbar
scrlbr = tk.Scrollbar(lf_p)


#
#Create table
tree = ttk.Treeview(lf_p,yscrollcommand=scrlbr.set)
tree["columns"] = ["a","b","c"]
tree.column("a",width = 100,anchor = 'center')
tree.column("b",width = 100,anchor = 'center')
tree.column("c",width = 100,anchor = 'center')
tree.heading("a",text = 'Thread ID')
tree.heading("b",text = 'Access Time')
tree.heading("c",text = 'Waiting Time')
scrlbr.config(command=tree.yview)


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
ltopic.grid(row=0,column=3)
lf.grid(columnspan=20,rowspan=20,padx=5,pady=5,ipadx=5,ipady=5)
l1.grid(row=2,column=0,sticky='W')
e1.grid(row=2,column=1,sticky='E')
l2.grid(row=3,column=0,sticky='W')
e2.grid(row=3,column=1,sticky='E')
l3.grid(row=4,column=0,sticky='W')
e3.grid(row=4,column=1,sticky='E')
l4.grid(row=5,column=0,sticky='W')
e4.grid(row=5,column=1,sticky='E')
lf_p.grid(row = 0,column=25,columnspan=55,rowspan=150,padx=5,pady=5,ipadx=5,ipady=5)

tree.grid(row=0,column=25,sticky='NSEW')
scrlbr.grid(row=0,column=84,sticky='NS')

#function of button start
<<<<<<< HEAD
    def ClickStart():
        global elist
        elist = [int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get())]
=======
def ClickStart():
     global elist
     elist = [int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get())]
     root.destroy()
>>>>>>> 79b676ac128ed7f20fd39e73f794acc415e14ac4


#create a button
b = tk.Button(lf,text='Start',font=('Times New Roman',12),width=10, height=1)
b.grid(row=6,column=0)



root.mainloop()
