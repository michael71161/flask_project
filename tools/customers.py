from flask import Flask ,render_template,json,request
import sqlite3

con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()


class Customers:
    def __init__(self):
        pass

    def addCustomer(self):
        if request.method=='POST':
            Name = request.form.get('Name')
            City = request.form.get('City')
            Age = request.form.get('Age')
            cur.execute(f'''INSERT INTO customers VALUES(not null, "{Name}", "{City}", {int(Age)})''')
            SQLcust=(f'''SELECT *  FROM customers WHERE Name LIKE  "%{Name}%" ''')
            cur.execute(SQLcust)
            addedcust=cur.fetchall()
            con.commit()
            return render_template("/addCustomer.html" ,addedcust=addedcust)
        return render_template("/addCustomer.html")
        

    def showall(self):
        con = sqlite3.connect('library.db', check_same_thread=False)
        cur = con.cursor()


        SQL = "SELECT *  FROM customers"
    
        cur.execute(SQL)
        customers=cur.fetchall()
        return render_template("/showpage.html" , customers=customers )
    
    def findCustomer(self):
         if request.method=='POST':
             Find= request.form.get('Name')
             SQLfind=(f'''SELECT * FROM customers WHERE Name LIKE  "%{Find}%" ''')
             cur.execute(SQLfind)
             person=cur.fetchall()
             return render_template ("/findcustomer.html" , person=person)
         return render_template ("/findcustomer.html")

    def removeCustomer(self):
        con=sqlite3.connect("library.db", check_same_thread=False)
        cur=con.cursor()

        if request.method=='POST':
            remove=request.form.get('Name')
            SQLremove=(f'''DELETE  FROM customers WHERE Name LIKE "%{remove}%" ''')
            cur.execute(SQLremove)
            
            rmvperson=cur.fetchall()
            con.commit()
            
    
           
           
            return render_template ("/removecustomer.html" , rmvperson=rmvperson)
        return render_template ("/removecustomer.html")
    

             

             





