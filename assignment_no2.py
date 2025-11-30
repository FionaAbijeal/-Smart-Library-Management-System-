class Book:

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {'Yes' if self.available else 'No'}")
        print("-----------------------------")

    def mark_issued(self):
        self.available = False
        print(f"Book '{self.title}' has been issued.")

    def mark_returned(self):
        self.available = True
        print(f"Book '{self.title}' has been returned.")


b1 = Book(1, "Python Programming", "John Smith")
b2 = Book(2, "Data Science Basics", "Sarah Lee")

b1.display_info()
b2.display_info()


class Member:

    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.name = name
        self.issued_books = []

    def get_member_id(self):
        return self.__member_id

    def set_member_id(self, new_id):
        self.__member_id = new_id

    def issue_book(self, book):
        self.issued_books.append(book)
        print(f"{self.name} issued the book: {book.title}")

    def return_book(self, book):
        if book in self.issued_books:
            self.issued_books.remove(book)
            print(f"{self.name} returned the book: {book.title}")
        else:
            print(f"{self.name} does not have this book to return.")

    def display_member_info(self):
        print(f"Member ID: {self.__member_id}")
        print(f"Name: {self.name}")
        print("Issued Books:")
        if len(self.issued_books) == 0:
            print("  No books issued")
        else:
            for b in self.issued_books:
                print(f"  - {b.title}")
        print("-----------------------------")


m1 = Member(101, "Fiona Abijeal")
m1.issue_book(b1)
m1.issue_book(b2)
m1.display_member_info()
m1.return_book(b1)
m1.display_member_info()


class StudentMember(Member):

    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.borrow_limit = 3

    def issue_book(self, book):
        if len(self.issued_books) >= self.borrow_limit:
            print(f"Student limit reached! {self.name} can only borrow {self.borrow_limit} books.")
        else:
            super().issue_book(book)

    def display_member_info(self):
        print("Student Member")
        super().display_member_info()


class TeacherMember(Member):

    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.borrow_limit = 5

    def issue_book(self, book):
        if len(self.issued_books) >= self.borrow_limit:
            print(f"Teacher limit reached! {self.name} can only borrow {self.borrow_limit} books.")
        else:
            super().issue_book(book)

    def display_member_info(self):
        print("Teacher Member")
        super().display_member_info()


s1 = StudentMember(201, "Amna")
s1.issue_book(b1)
s1.issue_book(b2)
s1.issue_book(b1)
s1.display_member_info()

t1 = TeacherMember(301, "Sir Bilal")
t1.issue_book(b1)
t1.issue_book(b2)
t1.display_member_info()


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.get_member_id() == member_id:
                return member
        return None

    def issue_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print(f"Member with ID {member_id} not found.")
            return
        if not book:
            print(f"Book with ID {book_id} not found.")
            return
        if not book.available:
            print(f"Book '{book.title}' is already issued.")
            return

        member.issue_book(book)
        book.mark_issued()

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print(f"Member with ID {member_id} not found.")
            return
        if not book:
            print(f"Book with ID {book_id} not found.")
            return
        if book not in member.issued_books:
            print(f"Book '{book.title}' was not issued to {member.name}.")
            return

        member.return_book(book)
        book.mark_returned()

    def display_all_books(self):
        print("===== All Books in Library =====")
        for book in self.books:
            book.display_info()

    def display_all_members(self):
        print("===== All Library Members =====")
        for member in self.members:
            member.display_member_info()


lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.register_member(s1)
lib.register_member(t1)
lib.issue_book(201, 1)
lib.issue_book(301, 2)
lib.display_all_books()
lib.display_all_members()
lib.return_book(201, 1)
lib.display_all_books()
