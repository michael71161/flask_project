
from flask import Flask ,render_template,json,request
import sqlite3
import tools.customers as custlib
import tools.books as booklib 
import tools.loans as loanlib 

con = sqlite3.connect('library.db', check_same_thread=False)
cur = con.cursor()


api = Flask(__name__)
def initDB():
    try:
      cur.execute("CREATE TABLE  books  (bookID INTEGER PRIMARY KEY AUTOINCREMENT , Name text, Author text, Year_published int, Type int , available text )")
      cur.execute("CREATE TABLE  customers (customerID INTEGER PRIMARY KEY AUTOINCREMENT,  Name text, City text , Age int )")
      cur.execute("CREATE TABLE  loans (customer_id int ,book_id int, loan_date int, return_date int )")
       
    except:
      print ("The tables already created")
    
    con.commit()
#test
def testInsertBooks():
  con = sqlite3.connect('library.db', check_same_thread=False)
  cur = con.cursor()

  cur.execute('INSERT INTO books VALUES(not null, "The Lord of the Rings", "J. R. R. Tolkien", 1954, 1, "Yes")')
  cur.execute('INSERT INTO books VALUES(not null,"The Alchemist","Paulo Coelho",1988,1,"yes")')
  for row in cur.execute('SELECT * FROM books'):
       print(row)
    
       con.commit
#test
def testInsertCustomers():
     con = sqlite3.connect('library.db', check_same_thread=False)
     cur = con.cursor()

     cur.execute('INSERT INTO customers VALUES(not null, "Michael Mogilianski", "Beer Sheva", 26)')
     cur.execute('INSERT INTO customers VALUES(not null,"Sophia Badalov","Beer sheva",27)')
     for row in cur.execute('SELECT * FROM customers'):
       print(row)
    
     con.commit


    
initDB()
#testInsertBooks()
#testInsertCustomers()

@api.route('/', methods=['GET'])
def menu():
    return render_template('mainMenu.html') 

@api.route('/Books', methods=['GET'])
def booksMenu():
    return render_template('secondaryMenuBooks.html')

@api.route('/Customers', methods=['GET'])
def customersMenu():
    return render_template('secondaryMenuCustomers.html')

@api.route('/Loans', methods=['GET'])
def loansMenu():
    return render_template('secondaryMenuLoans.html')


@api.route('/addcustomer', methods=['GET','POST'])
def addCustomer():
   return custlib.Customers.addCustomer(custlib)


   
@api.route('/showpage' ,methods=['GET','POST'])
def showall():
  return  custlib.Customers.showall(custlib)

@api.route('/findcustomer' ,methods=['GET','POST'])
def findCustomer():
  return custlib.Customers.findCustomer(custlib)

@api.route('/removecustomer' ,methods=['GET','POST'])
def removecustomer():
  return custlib.Customers.removeCustomer(custlib)

@api.route('/addbook', methods=['GET','POST'])
def addBook():
   return booklib.Books.addBook(booklib)


   
@api.route('/showbooks' ,methods=['GET','POST'])
def showbooks():
  return  booklib.Books.showbooks(booklib)


@api.route('/findbook' ,methods=['GET','POST'])
def findBook():
  return booklib.Books.findBook(booklib)

@api.route('/removebook' ,methods=['GET','POST'])
def removeBook():
  return booklib.Books.removeBook(booklib)


@api.route('/loanbook', methods=['GET','POST'])
def loanbook():
  return loanlib.Loans.loanBook(loanlib)

@api.route('/returnbook', methods=['GET','POST'])
def returnbook():
  return loanlib.Loans.returnbook(loanlib)

@api.route('/displayallloans', methods=['GET','POST'])
def displayallloans():
  return loanlib.Loans.displayallloans(loanlib)

@api.route('/displaylateloans', methods=['GET','POST'])
def displaylateloans():
  return loanlib.Loans.displaylateloans(loanlib)









if __name__ == '__main__':
    api.run(debug=True)


 