from tkinter import *
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='nivedita')
cur=db.cursor()
cur.execute("select BJP from parties;")
w=cur.fetchall()
for row in w:
	a=int(row[0])
x=cur.execute("select INC from parties;")
w=cur.fetchall()
for row in w:
	b=int(row[0])
y=cur.execute("select BSP from parties;")
w=cur.fetchall()
for row in w:
	c=int(row[0])
z=cur.execute("select CPI from parties;")
w=cur.fetchall()
for row in w:
	d=int(row[0])
objects = ('BJP', 'INC', 'BSP', 'CPI')
y_pos = np.arange(len(objects))
performance = [a,b,c,d] 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of votes')
plt.title('Current Election Statistics')
 
plt.show()