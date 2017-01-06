"""
CP1404 ASSIGNMENT 1
Name: Sudheer Paturi
ID: 13391146
Started: 28/12/2016
Completed: 02/01/2017

Reading list: Displays a list of books and lets the user choose either list required books, completed books, add a new book or mark a book as completed.

Pseudocode:

FILENAME - variable used to identify main csv file
file_list - an open array created to add books later on as required, completed or marked.

function read_file:(used the code posted on the github by lecturer)
    file_pointer = open()
      created a variable called file_pointer which opens the csv file
    for index,data in enumerate()
      enumerated each item in file_pointer using enumerate option
    data.strip
      all the data is cleaned of extra things like '\n' etc using data.strip
    data.split
      data is separated by commas using data.split(",")
    file_list.append
      then all the data is added to file_list array using file_list.append(datum)
    file_pointer.close()
      function ends here

function main:(main function which performs all the calculatoins)
    print(reading list by sudheer, 4 books loaded from csv file)
      A welcome message is displayed and the number of total books are displayed.
    while ans = true
      created a while for the whole function to run
    print("menu:
    Required books
    Completed books
    Mark as completed
    Add a new book
    Quit
    ")
      menu is diapled to the user with options to choose from
    ans = input("enter a value")
      variable created for the user to give input
    if ans = "R" or "C" or "M" or "A" or "Q"
      if loop is created for each value the user can choose
      the code in each if loop runs if that value is input by the user
    when the user chooses to quit,
    writer=csv.writer(csvfile)
    writer.writerrows(file_list)
      the code at the end writes all the file_list data to the books.csv and the program exits saying "good bye"

"""

from operator import itemgetter
import csv
FILENAME = "books.csv"
file_list = []

def read_file():
    global file_list
    file_pointer= open(FILENAME, "r")
    for index, data in enumerate(file_pointer.readlines()):
        data = data.strip()
        datum = data.split(",")
        file_list.append(datum)
        file_list.sort(key=itemgetter(1,2))
    file_pointer.close()
read_file()

def main():
    print("""
    Reading list by - Sudheer Paturi
    {} books loaded from books.csv
    """ .format(len(file_list)))
    ans = True
    while ans:

        counter = 0
        print("""
        Menu:
        (R) List Required books
        (C) List Completed books
        (A) Add new book
        (M) Mark a book as completed
        (Q) Quit
        """)
        ans = input("Please enter a value \n  ")
        if ans == "R" or ans == "r":
            required_list=[]
            print("\nRequired Books")
            for item in range(0, len(file_list)):
                if file_list[item][3] == "r":
                    required_list.append(file_list[item])
            if len(required_list) == 0:
                    print("No books required to be completed")
            else:
                for i, data in enumerate(file_list, 0):
                    if data[-1] == "r":
                        print(i, "-", data[0], "   by", data[1], "  ", data[2], "pages")
                        counter += 1
                totalPage = int()
                for i in file_list:
                    if i[-1] == "r":
                        totalPage += int(i[2])
                print("Total pages for {} books: ".format(counter), totalPage)

        elif ans == "C" or ans == "c":

            for i,data in enumerate(file_list):
                if data[-1] == "c":
                    print(i, "-", data[0], "   by", data[1], "  ", data[2], "pages")
                    counter += 1

            totalPage = int()
            for i in file_list:
                if i[-1] == "c":
                    totalPage += int(i[2])
            print("Total pages for {} books: " .format(counter), totalPage)

        elif ans == "A" or ans == "a":
            print("\n Add new book")
            add_book = open(FILENAME, "r")

            book_title= str(input("Enter Title of book"))
            while book_title == "":
                print("Input cannot be blank")
                book_title = str(input("Enter Title of book"))
            book_author= str(input("Enter Authors name"))
            while book_author == "":
                print("Input should not be blank")
                book_author = str(input("Enter Authors name"))
            while True:
                try:
                    book_pages = int(input("Enter number of pages"))
                    if float(book_pages)>0:
                        break
                    else:
                        continue
                except ValueError:
                    print("Invalid input, Enter a number")
                    continue

            new_book = [book_title, book_author, book_pages, 'r']
            file_list.append(new_book)
            add_book.close()

        elif ans == "M" or ans == "m":
            for i, data in enumerate(file_list, 0):
                if data [-1] == "r":
                    print(i, "-",data[0],"   by", data[1],"  ",data[2],"pages")
                    counter += 1
            totalPage = int()
            for i in file_list:
                if i[-1] == "r":
                    totalPage += int(i[2])
            print("Total pages for {} books: " .format(counter) , totalPage)
            print("Enter the number of the book to be marked as completed")

            while True:
                try:
                    specify_number = int(input(">>>"))
                    if specify_number < 0 or specify_number > len(file_list):
                        print("Invalid item number")
                    else:
                        file_list[specify_number][3] = "c"
                        print("{} by {} marked as completed".format(file_list[specify_number][0],file_list[specify_number][1]))
                        break
                except ValueError:
                    print("Invalid input; enter a number")


        elif ans == "Q" or ans == "q":
            print ("\n Good bye")
            with open(FILENAME,'w',newline="") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerows(file_list)
            break
        else:
            print("\n Not Valid Choice Try again")


main()

