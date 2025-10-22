# ==========================================
#  LIMKOKWING MINI LIBRARY SYSTEM - FUNCTIONS
# ==========================================

# --------- GLOBAL VARIABLES ---------
book_genres = (
    "FICTION", "NON-FICTION", "SCI-FI", "FANTASY",
    "HORROR", "ROMANCE", "HISTORY", "BIOGRAPHY"
)

# --------- ADD BOOK ---------
def add_books(isbn_book_details, book_genres):
    isbn = input("Enter the ISBN of the book: ").strip()

    if isbn in isbn_book_details:
        print("This book ISBN already exists.")
        return

    genre_detail = input("Enter the genre of the book: ").upper()
    if genre_detail not in book_genres:
        print("Invalid genre. Allowed genres are:")
        print(", ".join(book_genres))
        return

    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    total_copies = int(input("Enter total copies available: "))

    book_details = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Genre": genre_detail,
        "Total Copies": total_copies,
        "Available Copies": total_copies
    }

    isbn_book_details[isbn] = book_details
    print(f" Successfully added book: {title} ({genre_detail})")

# --------- ADD MEMBER ---------
def add_members(members):
    new_member_id = int(input("Enter the student ID: "))

    for member in members:
        if member["Member_Id"] == new_member_id:
            print("A member with the same ID already exists.")
            return

    name = input("Enter member name: ")
    email = input("Enter member email: ")

    member_detail = {
        "Member_Id": new_member_id,
        "Name": name,
        "Email": email,
        "Borrowed_Books": []
    }

    members.append(member_detail)
    print(f" {name} added to the library system!")

# --------- SEARCH BOOK ---------
def search_books(isbn_book_details):
    print("___SEARCH OPTION___:\n1. ISBN\n2. TITLE\n3. AUTHOR")
    option = input("Choose a search option: ").strip()
    query = input("Enter your search value: ").strip().lower()
    found = False

    for book in isbn_book_details.values():
        if option == "1" and book["ISBN"].lower() == query:
            print(book); found = True
        elif option == "2" and book["Title"].lower() == query:
            print(book); found = True
        elif option == "3" and book["Author"].lower() == query:
            print(book); found = True

    if not found:
        print("Book not found.")

# --------- UPDATE BOOK ---------
def update_books(isbn_book_details):
    isbn = input("Enter ISBN of book to update: ")

    if isbn not in isbn_book_details:
        print("Book not found.")
        return

    field = input("Enter field to update (Title/Author/Genre/Total Copies): ").title()
    new_value = input(f"Enter new {field}: ")

    if field == "Total Copies":
        new_value = int(new_value)
        isbn_book_details[isbn]["Available Copies"] = new_value

    isbn_book_details[isbn][field] = new_value
    print(" Book updated successfully!")

# --------- UPDATE MEMBER ---------
def update_members(members):
    member_id = int(input("Enter member ID to update: "))

    for member in members:
        if member["Member_Id"] == member_id:
            field = input("Enter field to update (Name/Email): ").capitalize()
            new_value = input(f"Enter new {field}: ")
            member[field] = new_value
            print(" Member updated successfully!")
            return

    print("Member not found.")

# --------- DELETE MEMBER ---------
def delete_members(members):
    del_name = input("Enter the name of the member you want to delete: ")

    for member in members:
        if member["Name"].lower() == del_name.lower():
            members.remove(member)
            print(f" Successfully deleted {del_name}")
            return

    print("No member found with that name.")

# --------- BORROW BOOK ---------
def borrow_book(members, isbn_book_details):
    member_id = int(input("Enter member ID: "))
    isbn = input("Enter ISBN of the book to borrow: ").strip()

    member = next((m for m in members if m["Member_Id"] == member_id), None)
    if not member:
        print("Member not found.")
        return

    if isbn not in isbn_book_details:
        print("Book not found.")
        return

    book = isbn_book_details[isbn]

    if book["Available Copies"] <= 0:
        print(f"Sorry, '{book['Title']}' is currently unavailable.")
        return

    if len(member["Borrowed_Books"]) >= 3:
        print("Borrowing limit reached (max 3 books).")
        return

    member["Borrowed_Books"].append(book["Title"])
    book["Available Copies"] -= 1
    print(f" '{book['Title']}' has been borrowed by {member['Name']}.")

# --------- RETURN BOOK ---------
def return_book(members, isbn_book_details):
    member_id = int(input("Enter member ID: "))
    isbn = input("Enter ISBN of the book to return: ").strip()

    member = next((m for m in members if m["Member_Id"] == member_id), None)
    if not member:
        print("Member not found.")
        return

    if isbn not in isbn_book_details:
        print("Book not found in library records.")
        return

    book = isbn_book_details[isbn]

    if book["Title"] not in member["Borrowed_Books"]:
        print(f"{member['Name']} did not borrow '{book['Title']}'.")
        return

    member["Borrowed_Books"].remove(book["Title"])
    book["Available Copies"] += 1
    print(f" '{book['Title']}' has been returned by {member['Name']}.")

# --------- DISPLAY MEMBERS ---------
def display_members(members):
    print("\nCURRENT MEMBERS AND THEIR BORROWED BOOKS:")
    if not members:
        print("No members found.")
        return
    for member in members:
        print(f"{member['Name']} ({member['Member_Id']}) -> Borrowed: {member['Borrowed_Books']}")

# --------- DISPLAY BOOKS ---------
def display_books(isbn_book_details):
    print("\n AVAILABLE BOOKS:")
    if not isbn_book_details:
        print("No books found.")
        return
    for book in isbn_book_details.values():
        print(f"{book['Title']} by {book['Author']} ({book['Genre']}) — Available: {book['Available Copies']}")
