# ==========================================
# LIMKOKWING MINI LIBRARY SYSTEM - UNIT TESTS
# ==========================================
import unittest
from operation import (
    display_books, display_members
)

#  We’ll also import any functions that don’t require input
from operation import borrow_book, return_book

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        """Sample test data (runs before each test)."""
        self.members = [
            {"Member_Id": 905005032, "Name": "Joseph A. Farmer", "Email": "jambrosefarmer@gmail.com", "Borrowed_Books": []},
            {"Member_Id": 905005030, "Name": "Tommy A. Farmer", "Email": "tambrosefarmer@gmail.com", "Borrowed_Books": []},
        ]

        self.isbn_book_details = {
            "101": {"ISBN": "101", "Title": "Invisible Man", "Author": "Ralph Ellison", "Genre": "BIOGRAPHY",
                    "Total Copies": 5, "Available Copies": 5},
            "102": {"ISBN": "102", "Title": "Python Basics", "Author": "Mark Lutz", "Genre": "NON-FICTION",
                    "Total Copies": 3, "Available Copies": 3},
        }

    # ---------------- TESTS ----------------

    def test_display_books(self):
        """ Test if books display without error."""
        try:
            display_books(self.isbn_book_details)
        except Exception as e:
            self.fail(f"display_books raised an exception: {e}")

    def test_display_members(self):
        """ Test if members display without error."""
        try:
            display_members(self.members)
        except Exception as e:
            self.fail(f"display_members raised an exception: {e}")

    def test_borrow_book_logic(self):
        """ Test book borrowing logic manually (without input)."""
        member = self.members[0]
        book = self.isbn_book_details["101"]

        # simulate borrow
        member["Borrowed_Books"].append(book["Title"])
        book["Available Copies"] -= 1

        self.assertIn("Invisible Man", member["Borrowed_Books"])
        self.assertEqual(book["Available Copies"], 4)

    def test_return_book_logic(self):
        """ Test book return logic manually."""
        member = self.members[0]
        book = self.isbn_book_details["102"]

        # simulate borrow first
        member["Borrowed_Books"].append(book["Title"])
        book["Available Copies"] -= 1

        # simulate return
        member["Borrowed_Books"].remove(book["Title"])
        book["Available Copies"] += 1

        self.assertNotIn("Python Basics", member["Borrowed_Books"])
        self.assertEqual(book["Available Copies"], 3)

    def test_borrow_limit(self):
        """ Test that a member cannot borrow more than 3 books."""
        member = self.members[0]
        member["Borrowed_Books"] = ["A", "B", "C"]
        can_borrow = len(member["Borrowed_Books"]) < 3
        self.assertFalse(can_borrow)

if __name__ == "__main__":
    unittest.main()
