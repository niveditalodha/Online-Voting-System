from tkinter import *
import subprocess
def a():
	root1.destroy()
	subprocess.call(["python", "C:/Users/nirmal/bar.py"])
def d():
	root1.destroy()
	subprocess.call(["python", "C:/Users/nirmal/proj.py"])
root1=Tk()
root1.title("ELECTIONS")
f1=Frame(root1,height=335,width=580)
photo =PhotoImage(file='vote.png')
label = Label(f1,image=photo,highlightthickness=6,bg='black').place(x=0,y=0)
b=Button(f1,text="Vote",bg='light grey',font=('comic sans',17,'bold'),command=d)
b.place(x=20,y=200)
b1=Button(f1,text="Show Statistics",bg='light grey',font=('comic sans',17,'bold'),command=a)
b1.place(x=300,y=200)
f1.pack()
root1.mainloop()
