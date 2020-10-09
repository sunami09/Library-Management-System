from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as c
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
db=c.connect(user='root',password='SD21012003',host='localhost',database='library')
if db.is_connected():
    print("successfully connected")
mc=db.cursor()

def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    publication = bookInfo4.get()
    if bid=="":
        pass
    else:
        query="insert into "+"books"+" values"+"("+"'"+bid+"'"+","+"'"+title+"'"+","+"'"+author+"'"+","+"'"+publication+"'"+","+"'Available')"
        mc.execute(query)
        db.commit()
    bookInfo1.delete(0,END)   
    bookInfo2.delete(0,END) 
    bookInfo3.delete(0,END) 
    bookInfo4.delete(0,END)  
def addBook():
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, bookTable, root1

    root1=Tk()
    root1.title("Add Book")
    root1.geometry("600x500")
    Canvas1=Canvas(root1)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame2 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame2.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame2, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    lb1 = Label(labelFrame,text="Book ID : ", bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    lb4 = Label(labelFrame,text="Publication : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    SubmitBtn = Button(root1,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root1,text="Quit",bg='#f7f1e3', fg='black',       command=root1.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

def deleteBook():
    bid1 = bookInfo5.get()
    query1 = "delete from books"+" where BID="+"'"+bid1+"'"
    mc.execute(query1)
    db.commit()
    messagebox.showinfo('Success',"Book Record Deleted Successfully")
    bookInfo5.delete(0, END)
def delete():
    global bookInfo5
    root3 = Tk()
    root3.title("Delete Book")
    root3.geometry("500x400")
    Canvas1 = Canvas(root3)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root3,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root3,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   

    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root3,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root3,text="Quit",bg='#f7f1e3', fg='black', command=root3.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)


def View():
    
    root12=Tk()
    root12.config(bg="grey")
    def clear():
        query= "select * from books"
        mc.execute(query)
        rows = mc.fetchall()
        update(rows)
        ent.delete(0,END)
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',values=i)

    def search():
        q2=q.get()
        query="select * from books where BID like '%"+q2+"%' or Title like '%"+q2+"%' or Author like '%"+q2+"%' or Publication like '%"+q2+"%'"
        mc.execute(query)
        rows = mc.fetchall()
        update(rows)
        
    q=StringVar()
    lbl1=Label(root12,bg="grey",text="List Of All Books",font=('times',15,'italic bold underline'))
    lbl1.pack()
    trv= ttk.Treeview(root12, columns=(1,2,3,4,5),show="headings",height="20")
    trv.pack()
    trv.heading(1,text="BID")
    trv.heading(2,text="Title")
    trv.heading(3,text="Author")
    trv.heading(4,text="Publication")
    trv.heading(5,text="Status")
    query= "select * from books"
    mc.execute(query)
    rows = mc.fetchall()
    update(rows)
    lbl =Label(root12,text="Search:",bg="grey",font=('times',15,'bold'),height="2")
    lbl.pack(side=tk.LEFT,padx=10)
    ent = Entry(root12,textvariable=q)
    ent.pack(side=tk.LEFT,padx=6)
    btn= Button(root12,text="Search",command=search)
    btn.pack(side=tk.LEFT,padx=6)
    cbtn= Button(root12,text="Clear",command=clear)
    cbtn.pack(side=tk.LEFT,padx=6)
    cbtn= Button(root12,text="Quit",command=root.destroy)
    cbtn.pack(side=tk.LEFT,padx=6)
    

def issue():
    bid = inf1.get()
    issueto = inf2.get()
    query4="UPDATE books set Status="+"'issued'"+" where BID="+"'"+bid+"'"
    mc.execute(query4)
    db.commit()
    query5="insert into issuedbook1 values("+"'"+bid+"'"+","+"'"+issueto+"')"
    mc.execute(query5)
    db.commit()



def issueBook():
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="orange")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="blue",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)

    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

def returnn():
    bid=bookInfo7.get()
    try:

        query="update books set Status='Available' where BID='"+bid+"'"
        mc.execute(query)
        db.commit()
        query="delete from issuedbook where BID='"+bid+"'"
        mc.execute(query)
        db.commit()
        messagebox.showinfo('Success',"Book Returned Successfully")
    except:
        messagebox.showinfo("Error","Book ID not present") 

def returnBook():
    global bookInfo7,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo7 = Entry(labelFrame)
    bookInfo7.place(relx=0.3,rely=0.5, relwidth=0.62)
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
#============================================================================
def on_enterbtn1(e):
    btn1['bg'] = 'yellow'
def on_leavebtn1(e):
    btn1['bg']='black'
def on_enterbtn2(e):
    btn2['bg'] = 'yellow'
def on_leavebtn2(e):
    btn2['bg']='black'
def on_enterbtn3(e):
    btn3['bg'] = 'yellow'
def on_leavebtn3(e):
    btn3['bg']='black'
def on_enterbtn4(e):
    btn4['bg'] = 'yellow'
def on_leavebtn4(e):
    btn4['bg']='black'
def on_enterbtn6(e):
    btn6['bg'] = 'yellow'
def on_leavebtn6(e):
    btn6['bg']='black'

root = Tk()
root.title("Library Management")
root.geometry('700x600')
same=True
n=1

background_image =Image.open('lib.jpg')
[imageSizeWidth, imageSizeHeight]=background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,280,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel1= Label(headingFrame1,text="Welcome To Library",bg='black',fg='white',font=('Courier',15))
headingLabel1.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Books",bg='black',font=20, fg='green', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black',font=20, fg='green', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View All Book",bg='black',font=20, fg='green', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black',font=20, fg='green', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn6 = Button(root,text="Return Book",bg='black',font=20, fg='green', command = returnBook)
btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

btn1.bind('<Enter>',on_enterbtn1)
btn1.bind('<Leave>',on_leavebtn1)
btn2.bind('<Enter>',on_enterbtn2)
btn2.bind('<Leave>',on_leavebtn2)
btn3.bind('<Enter>',on_enterbtn3)
btn3.bind('<Leave>',on_leavebtn3)
btn4.bind('<Enter>',on_enterbtn4)
btn4.bind('<Leave>',on_leavebtn4)
btn6.bind('<Enter>',on_enterbtn6)
btn6.bind('<Leave>',on_leavebtn6)

root.mainloop()
#=======================================================================================
