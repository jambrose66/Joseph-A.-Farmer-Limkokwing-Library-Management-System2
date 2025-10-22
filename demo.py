# ==========================================
#  LIMKOKWING MINI LIBRARY SYSTEM - DEMO SCRIPT
# ==========================================


from operation import (
    add_books, add_members, search_books, update_books,
    update_members, delete_members, borrow_book, return_book,
    display_members, display_books, book_genres
)


# --------- SAMPLE DATA ---------
members = [
    {"Member_Id": 905005032, "Name": "Joseph A. Farmer", "Email": "jambrosefarmer@gmail.com", "Borrowed_Books": []},
    {"Member_Id": 905005030, "Name": "Tommy A. Farmer", "Email": "tambrosefarmer@gmail.com", "Borrowed_Books": []},
]

isbn_book_details = {
    "101": {"ISBN": "101", "Title": "Invisible Man", "Author": "Ralph Ellison", "Genre": "BIOGRAPHY", "Total Copies": 5, "Available Copies": 5},
    "102": {"ISBN": "102", "Title": "Python Basics", "Author": "Mark Lutz", "Genre": "NON-FICTION", "Total Copies": 3, "Available Copies": 3},
    "103": {"ISBN": "103", "Title": "Haunting of Hill House", "Author": "Shirley Jackson", "Genre": "HORROR", "Total Copies": 4, "Available Copies": 4}
}

# --------- MAIN MENU ---------
def main_menu():
    while True:
        print("""
===============================
 LIMKOKWING MINI LIBRARY MENU
===============================
1. Add Book
2. Add Member
3. Search Book
4. Update Book
5. Update Member
6. Delete Member
7. Borrow Book
8. Return Book
9. Display All Members
10. Display All Books
0. Exit
""")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_books(isbn_book_details, book_genres)
        elif choice == "2":
            add_members(members)
        elif choice == "3":
            search_books(isbn_book_details)
        elif choice == "4":
            update_books(isbn_book_details)
        elif choice == "5":
            update_members(members)
        elif choice == "6":
            delete_members(members)
        elif choice == "7":
            borrow_book(members, isbn_book_details)
        elif choice == "8":
            return_book(members, isbn_book_details)
        elif choice == "9":
            display_members(members)
        elif choice == "10":
            display_books(isbn_book_details)
        elif choice == "0":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# --------- RUN PROGRAM ---------
if __name__ == "__main__":
    main_menu()
