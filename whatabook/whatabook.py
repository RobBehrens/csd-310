# Robert Behrens
# 7/23/2022
# database/Database Security
# Henry Lee

import mysql.connector
whatabookdb = mysql.connector.connect( 
    user ="whatabook_user",
    password ="MySQL8IsGreat!",
    host="127.0.0.1",
    database="whatabook"
    )
mycursor = whatabookdb.cursor()
def userlogin(): # user login
    n = 1
    while n == 1:
        user_id = int(input("enter User id:"))
        if user_id > 0 and user_id <= 3:
            print("user id accepted")
            n = 0
        else:
            print("user id invalid")
    return user_id
            
        
def showwishlist(user_id): # displays all wishlist items
    mycursor.execute("SELECT book.book_id, book_name, author FROM wishlist INNER JOIN book ON wishlist.book_id = book.book_id WHERE user_id = {}" .format(user_id))
    myresult = mycursor.fetchall()
    print("displaying all books in wishlist")
    for x in myresult:
        print(" book_id: {} book name: {} author: {}" .format(x[0], x[1], x[2]))
def showavalablebooks(user_id): # show avalable books not in wishlist
    mycursor.execute("SELECT book_id, book_name, author, book_details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))
    myresult = mycursor.fetchall()
    print("displaying all books")
    for x in myresult:
        print("book_id: {} book_name: {} author: {} book_details: {}".format(x[0], x[1], x[2], x[3]))
def showallbooks():
    mycursor.execute("SELECT book_id, book_name, author, book_details FROM book")
    myresult = mycursor.fetchall()
    print("displaying all books")
    for x in myresult:
        print("book_id: {} book name: {} author: {} book_details: {}".format(x[0], x[1], x[2],x[3]))
def showstorelocation():
    mycursor.execute("SELECT store_id, store_locate FROM store")
    myresult = mycursor.fetchall()
    for x in myresult:
        print("store_id: {} store_location: {}".format(x[0], x[1]))
def addwishlistitem(user_id): # add an item to the users wishlist
    mycursor.execute("SELECT book_id, book_name, author, book_details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))
    myresult = mycursor.fetchall()
    i = 0
    while i == 0 :
        print("displaying avalable books")
        for x in myresult:
            print("book_id: {} book_name: {} author: {} book_details: {}".format(x[0], x[1], x[2], x[3]))
        book_id = int(input("enter the book id of the book you want to add to your wishlist:"))
        if book_id >= 1 and book_id <= 9:
            i = 1
            sql = "INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)"
            val = (user_id, book_id)
            mycursor.execute(sql, val)
            whatabookdb.commit()
            print(mycursor.rowcount, "book added")
        else:
            print("entry invalid")
def usermenu(): # this is the user menu module
    n = 0
    user_id = userlogin()
    while n == 0:
        print("user menu \n enter 1 to view wishlist. \n enter 2 to view avalable books. \n enter 3 to add a book to your wishlist. \n enter 4 to return to mainmenu")
        user_menu = int(input("enter choice:"))
        if user_menu == 1:
            showwishlist(user_id)
        elif user_menu == 2:
            showavalablebooks(user_id)
        elif user_menu == 3:
            addwishlistitem(user_id)
        elif user_menu == 4:
            n = 1
        else:
            print("invalid entry")

def mainmenu(): # this is the main menu module
    n = 0
    while n == 0:
        print("whatabook main menu\n enter 1 to display all store locations. \n enter 2 to display all books. \n enter 3 to access user menu. \n enter 4 to exit program.")
        user_menu = int(input("enter choice:"))
        if user_menu == 1:
            showstorelocation()
        elif user_menu == 2:
            showallbooks()
        elif user_menu == 3:
            usermenu()
        elif user_menu == 4:
            n = 1
        else:
            print("invalid entry")
mainmenu()