from tkinter import *
import random
root=Tk()
root.title("list")
root.geometery("444x444")
list1=['water','cookies','donuts','bag','box','blanket']
label1=Label(root)
label1["text"]=list1
label2=Label(root)
def randomlist():
    randomlist=random.sample(range(0,3),1)
    label1["text"]="Listed itmes"+str(list1)
    label2["text"]="Put item no"+str(randomlist)
btn=Button(root,text="Which item to put in the bag?", bg="indigo",fg="white")
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label2.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()