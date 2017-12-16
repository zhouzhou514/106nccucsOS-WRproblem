import Tkinter as tk

#create a window object
root = tk.Tk()
#name the window as'Group 14'
root.title('Group 14 12/21 RW Problem')
#define the size of the window
root.geometry('1000x800')

#create a label which display on the 'Group 14'window, and define its attributes
ltopic = tk.Label(root,text='RW Problem by Group 14', bg = 'light blue',font = ('Times New Roman',14), width = 30, height = 2)

#Create a LabelFrame for input area
lf = tk.LabelFrame(root, text='Input',font=('Tims New Roman',14))

#Create 4 labels
l1 = tk.Label(lf,text='Input the amount of events (1~10000)  ',font = ('Times New Roman',12))
l2 = tk.Label(lf,text='Input the proportion of reader and writer   ',font = ('Times New Roman',12))
l3 = tk.Label(lf,text='Input the maximum produce delay (1~100)   ',font = ('Times New Roman',12))
l4 = tk.Label(lf,text='Input the maximum access time (1~100)  ',font = ('Times New Roman',12))

#Create an entry for the input
e1 = tk.Entry(lf,show=None)
e2 = tk.Entry(lf,show=None)
e3 = tk.Entry(lf,show=None)
e4 = tk.Entry(lf,show=None)

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


#create a button
b = tk.Button(lf,text='Start',font=('Times New Roman',12),width=10, height=1)
b.grid(row=6,column=0)


root.mainloop()