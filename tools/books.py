import sqlite3 
from flask import Flask ,render_template,json,request

con = sqlite3.connect('library.db' , check_same_thread=False)
cur = con.cursor()


class Books :
    def __init__(self) :
        pass



    def addBook(self):
        
       if request.method=='POST':
           
            Bookname = request.form.get('Name')
            Authorname = request.form.get('Authorname')
            Year = request.form.get('year')
            Type = request.form.get('type')
            isavailable= request.form.get('available')
            
            
            
            cur.execute(f'''INSERT INTO books VALUES(not null, "{Bookname}", "{Authorname}", {int(Year)} ,{int(Type)},"{isavailable}")''')
            SQLadded=(f'''SELECT *  FROM books WHERE Name LIKE  "%{Bookname}%" ''')
            cur.execute(SQLadded)
            added=cur.fetchall()
            con.commit()
            return render_template("/addbook.html" , added=added  )
       return render_template("/addbook.html")

    def showbooks(self):

      SQLB="SELECT *  FROM BOOKS"
      cur.execute(SQLB)
      books=cur.fetchall()
      return render_template ("/showbooks.html" , books=books)

    def findBook(self):
        if request.method=='POST':
             Findb= request.form.get('Name')
             SQLfindb=(f'''SELECT * FROM books WHERE Name LIKE  "%{Findb}%" ''')
             cur.execute(SQLfindb)
             book=cur.fetchall()
             return render_template ("/findbook.html" , book=book)
        return render_template ("/findbook.html")


    def removeBook(self):
        if request.method=='POST':
            
            id=request.form.get('id')
            

            SQLrmv=(f'''DELETE  FROM books WHERE bookID = {int(id)} ''')
            cur.execute(SQLrmv)
            rmvbook=cur.fetchall()
            
            
            con.commit()
            return render_template ("/removebook.html" ,  rmvbook=rmvbook)
        return render_template ("/removebook.html")
    



    



