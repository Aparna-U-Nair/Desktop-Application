"""
A program that stores this book info:
Title, Year, Author, ISBN

User can do the following within GUI:
View All records
Search an entry
Add an entry
Update 
Delete
Close
"""
from tkinter import *
import backend

def getSelectedRowId(event):
    try:
        global selected
        idx = list1.curselection()[0]
        selected = list1.get(idx)
        e1.delete(0, END)
        e1.insert(END, selected[1])
        e2.delete(0, END)
        e2.insert(END, selected[2])
        e3.delete(0, END)
        e3.insert(END, selected[3])
        e4.delete(0, END)
        e4.insert(END, selected[4])
    except:
        pass

def viewCommand():
    list1.delete(0,END)
    for row in backend.viewAll():
        list1.insert(END,row)

def searchCommand():
    list1.delete(0,END)
    for row in backend.search(title.get(),author.get(),year.get(),isbn.get()):
        list1.insert(END, row)

def insertCommand():
    backend.insert(title.get(),author.get(),year.get(),isbn.get())
    list1.delete(0,END)
    list1.insert(END,(title.get(),author.get(),year.get(),isbn.get())) 

def updateCommand():
    backend.update(selected[0], title.get(),author.get(),year.get(),isbn.get())

def deleteCommand():
    backend.delete(selected[0])

window = Tk()
window.wm_title('Book Store')

#All labels
l1 = Label(window, text = 'Title')
l1.grid(row = 0, column =0)
l2 = Label(window, text = 'Author')
l2.grid(row = 0, column =2)
l3 = Label(window, text = 'Year')
l3.grid(row = 1, column =0)
l4 = Label(window, text = 'ISBN')
l4.grid(row = 1, column =2)

#All User Input fields
title = StringVar()
e1 = Entry(window, textvariable = title)
e1.grid(row = 0, column = 1)
author = StringVar()
e2 = Entry(window, textvariable = author)
e2.grid(row = 0, column = 3)
year = StringVar()
e3 = Entry(window, textvariable = year)
e3.grid(row = 1, column = 1)
isbn = StringVar()
e4 = Entry(window, textvariable = isbn)
e4.grid(row = 1, column = 3)

#Listbox to show the entries
list1 = Listbox(window, height = 10, width = 35)
list1.grid(row = 2, column = 0, rowspan = 8, columnspan = 2)

#Vertical scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)
#Configure the listbox list1 to scrollbar sb1
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#To get the selected row of list
list1.bind('<<ListboxSelect>>', getSelectedRowId)

#All the buttons for user to make one click modifications
b1 = Button(window, text = "View All", width = 16, command = viewCommand)
b1.grid(row = 2, column = 3)
b2 = Button(window, text = "Search Entry", width = 16, command = searchCommand)
b2.grid(row = 3, column = 3)
b3 = Button(window, text = "Add Entry", width = 16, command = insertCommand)
b3.grid(row = 4, column = 3)
b4 = Button(window, text = "Update Selected", width = 16, command = updateCommand)
b4.grid(row = 5, column = 3)
b5 = Button(window, text = "Delete Selected", width = 16, command = deleteCommand)
b5.grid(row = 6, column = 3)
b6 = Button(window, text = "Close", width = 16, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()