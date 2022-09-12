from flask import Flask ,render_template,json,request
import sqlite3
from datetime import datetime

con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()


class Loans:
    def __init__(self) :
        pass

    def loanBook(self):
         res=[]
         if request.method == "POST":
            for row in cur.execute('''SELECT available from books '''):
                    isavailable=row[0]
                    if(isavailable == 'no'):
                        res.append("book isn't available right now")
                    else:
                         custid=request.form.get("customerid")
                         bookid=request.form.get("bookid")
                         loandate=request.form.get("loandate")
                         cur.execute("INSERT INTO loans (customer_id,book_id,loan_date) VALUES (?,?,?)",(custid,bookid,loandate))
                         cur.execute("UPDATE books SET available ='no' WHERE bookID=?",(bookid))
                         con.commit()
                         res.append("book is loaned")
                         return render_template("/loanbook.html", res=res)
            return render_template("/loanbook.html", res=res)
         return render_template("/loanbook.html")
       
    def displayallloans(self):
       
        SQL= '''SELECT * FROM loans'''
        cur.execute(SQL)
        loans = cur.fetchall()
        return render_template("/displayallloans.html", loans=loans)


    def returnbook(self):
        if request.method== "POST":
           bookid=request.form.get("bookid")
           self.return_date=datetime.now()
           cur.execute("DELETE FROM loans WHERE book_id =?",(bookid))
           cur.execute('''UPDATE books SET available = 'yes'  WHERE bookID=?''',(bookid))
           con.commit()
           return render_template("/returnbook.html")
        return render_template("returnbook.html")    



    def displaylateloans(self):
        global booktype,row
        dis=[]
        if request.method=='POST':
            bookid=request.form.get("bookid")
            for row in cur.execute('''SELECT loans.book_id, books.Type, loans.loan_date FROM loans
                                            INNER JOIN books ON loans.book_id = books.bookID
                                            WHERE BookID=?''',(bookid)):
                            
                booktype=row[1]
                mdate1= datetime.now() - datetime.strptime(row[2], "%Y-%m-%d")
                Dtype1= (mdate1).days > 10
                Dtype2= (mdate1).days > 5
                Dtype3= (mdate1).days > 2
                if(booktype == 1 and Dtype1):
                    dis.append(("Book is late by" ,((mdate1).days-10),"days"))
                    return render_template("/displaylateloans.html",dis=dis)
                elif(booktype == 2 and Dtype2):
                    dis.append(("Book is late by" ,((mdate1).days-5),"days"))
                    return render_template("/displaylateloans.html",dis=dis)
                elif(booktype == 3 and Dtype3):
                    dis.append(("Book is late by" ,((mdate1).days-2),"days"))
                    return render_template("/displaylateloans.html",dis=dis)
                else:
                    dis.append(("book isn't late"))
                    return render_template("/displaylateloans.html",dis=dis)
        return render_template("/displaylateloans.html",dis=dis)