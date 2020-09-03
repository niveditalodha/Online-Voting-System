from tkinter import *
import subprocess
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='nivedita')

cur=db.cursor()
def d():
	root.destroy()
	subprocess.call(["python", "C:/Users/nirmal/first.py"])

def a():
	if(e1.get()=="" or e2.get()=="" or e3.get()==""):
		print("Enter all details")
	else:
		name=""
		cur.execute("select name,DOB from candidate where VoterId=%s;",e3.get())
		name=cur.fetchall()
		for row in name:
			n=row[0]
			dob=row[1]
			
		
		if(str(n) == str(e1.get()) and str(dob)==str(e2.get()) ):
		
			cur.execute("select VoterId from voted;")
			v=cur.fetchall()
			
			k=len(v)
			j=1
			if(k==0):
					cur.execute("insert into voted values (%s)",e3.get())
					db.commit()
					cur.close()
					db.close()
					root.destroy()
					subprocess.call(["python", "C:/Users/nirmal/proj2.py"])
			
			for row in v:
				


				if(str(row[0])==str(e3.get())):
					l1=Label(text="You can vote only once",bg='white',fg="red",height=1,width=20,font=('comic sans',10,'italic'))
					l1.place(x=150,y=330)
					break
				if(j==k):
					cur.execute("insert into voted values (%s)",e3.get())
					db.commit()
					cur.close()
					db.close()
					root.destroy()
					subprocess.call(["python", "C:/Users/nirmal/proj2.py"])
				j=j+1
				
		else:
			l1=Label(text="Wrong details or you are not registered",bg='white',fg="red",height=1,width=30,font=('comic sans',10,'italic'))
			l1.place(x=150,y=330)


root=Tk()
root.title("CANDIDATE DETAILS")
f=Frame(root,height=480,width=715)
photo =PhotoImage(file='elec.png')
label = Label(f,image=photo,highlightthickness=6,bg='black').place(x=0,y=0)
root.resizable(width=False, height=False)

l1=Label(text="WELCOME TO ELECTIONS 2018",bg='brown',fg="yellow",height=1,width=30,font=('comic sans',20,'bold italic'))
l1.place(x=120,y=20)
l2=Label(text="Enter your details",height=1,width=15,font=('comic sans',15,'italic'))
l2.place(x=80,y=150)
l3=Label(text="Name:",height=1,width=7,font=('comic sans',12,'bold'))
l3.place(x=80,y=200)
l4=Label(text="D.O.B.:",height=1,width=7,font=('comic sans',12,'bold'))
l4.place(x=80,y=240)
l4=Label(text="Voter ID:",height=1,width=7,font=('comic sans',12,'bold'))
l4.place(x=80,y=300)
l5=Label(text="(yyyy-mm-dd)",height=1,width=9,font=('comic sans',10,''))
l5.place(x=80,y=265)
b=Button(f,text="Proceed to vote",font=('comic sans',15,'bold'),command=a)
b.place(x=200,y=360)
b1=Button(f,text="BACK",font=('comic sans',15,'bold'),command=d)
b1.place(x=450,y=360)
e1=Entry(f,width=20,fg="black",bg="grey",font=('comic sans',13,'italic'))
e1.place(x=200,y=200)
e2=Entry(f,width=20,fg="black",bg="grey",font=('arial',13,'italic'))
e2.place(x=200,y=240)
e3=Entry(f,width=20,fg="black",bg="grey",font=('arial',13,'italic'))
e3.place(x=200,y=300)

f.pack()
root.mainloop()