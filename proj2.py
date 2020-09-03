from tkinter import *
import subprocess
import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='nivedita')

cur=db.cursor()

def a():
	x=var.get()
	if(x==1):
		cur.execute("update parties set CPI=CPI+1;")
		db.commit()
		cur.close()
		db.close()
		root.destroy()
		subprocess.call(["python", "C:/Users/nirmal/bar.py"])
	elif(x==2):
		cur.execute("update parties set INC=INC+1;")
		db.commit()
		cur.close()
		db.close()
		root.destroy()
		subprocess.call(["python", "C:/Users/nirmal/bar.py"])
	elif(x==3):
		cur.execute("update parties set BJP=BJP+1;")
		db.commit()
		cur.close()
		db.close()
		root.destroy()
		subprocess.call(["python", "C:/Users/nirmal/bar.py"])
	elif(x==4):
		cur.execute("update parties set BSP=BSP+1;")
		db.commit()
		cur.close()
		db.close()
		root.destroy()
		subprocess.call(["python", "C:/Users/nirmal/bar.py"])
	else:
		l1=Label(text="You need to select a candidate",bg='white',fg='red',height=1,width=30,font=('comic sans',10,'italic'))
		l1.place(x=200,y=600)

root=Tk()
root.title("VOTE")
f=Frame(root,height=1000,width=1030)
photo =PhotoImage(file='party.png')
label = Label(f,image=photo,highlightthickness=6,bg='black').place(x=0,y=0)
root.resizable(width=False, height=False)
l1=Label(text="CHOOSE YOUR VOTE",bg='Green',height=1,width=30,font=('comic sans',30,'bold italic'))
l1.place(x=120,y=50)
var=IntVar()
r1=Radiobutton(f,text="Communist Party of India",variable=var,value=1,bg='grey',font=('comic sans',12,'bold'))
r2=Radiobutton(f,text="Indian National Congress",variable=var,value=2,bg='grey',font=('comic sans',12,'bold'))
r3=Radiobutton(f,text="Bhartiya Janata Party",variable=var,value=3,bg='grey',font=('comic sans',12,'bold'))
r4=Radiobutton(f,text="Bahujan Samaj Party",variable=var,value=4,bg='grey',font=('comic sans',12,'bold'))
r1.place(x=20,y=500)
r2.place(x=270,y=500)
r3.place(x=520,y=500)
r4.place(x=770,y=500)
b=Button(f,text="SUBMIT",bg='light grey',font=('comic sans',15,'bold'),command=a)
b.place(x=450,y=550)

f.pack()
root.mainloop()