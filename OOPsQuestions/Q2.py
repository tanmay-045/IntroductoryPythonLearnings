from datetime import date

class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=True


class Member:
    def __init__(self,mem_name,mem_id,borrow_limit=3):
        self.mem_name=mem_name
        self.mem_id=mem_id
        self.borrow_limit=borrow_limit
        self.borrowed_books=[]
        self.transaction_history=[]
        self.fees_due=0
        
    def borrow_book(self,book,borrow_date):
        if len(self.borrowed_books)<self.borrow_limit:
            if book.available:
                book.available=False
                self.borrowed_books.append((book,borrow_date))
                self.transaction_history.append((book, " borrowed on ",borrow_date))
                print(f'{self.mem_name} has borrowed {book.title} on {borrow_date}')
            else:
                print(f'The book {book.title} is unavailable')
        else:
            print('Borrow Limit Exceeded!')


    def return_book(self,book,return_date,fee_per_day=3): # assuming late fees of Rs.3
        for borrowed_book, borrowed_date in self.borrowed_books:
            if borrowed_book==book:
                days_borrowed = (return_date-borrowed_date).days
                if days_borrowed>10:
                    overdue_days = days_borrowed-10
                    fee = overdue_days*fee_per_day
                    self.fees_due+=fee
                    print(f"Book {book.title} returned {overdue_days} days late. Late Fees : {fee} (Rs.3.0/Day)")
                book.available=True
                self.borrowed_books.remove((book,borrowed_date))
                self.transaction_history.append((book, " returned on ", borrowed_date))
                return
        print('This book is not isuued to this person')



class Library:
    def __init__(self):
        self.books=[]
        self.members=[]

    def add_book(self,title,author,isbn):
        book=Book(title,author,isbn)
        self.books.append(book)
        print(f"'{title}' book added.")

    def add_member(self,mem_name,mem_id):
        member=Member(mem_name,mem_id)
        self.members.append(member)
        print(f'New Member Added\nWelcome {mem_name}')

    def borrow_book(self, mem_id,isbn,borrow_date):
        member= self.find_member(mem_id)
        book=self.find_book(isbn)
        if member and book:
            member.borrow_book(book,borrow_date)

    def return_book_lib(self,mem_id,isbn,return_date):
        member = self.find_member(mem_id)
        book = self.find_book(isbn)
        if member and book:
            member.return_book(book,return_date)

    def find_book(self,isbn):
        for book in self.books:
            if book.isbn==isbn:
                return book
        print("No book found with ",isbn)

    def find_member(self,mem_id):
        for mem in self.members:
            if mem.mem_id==mem_id:
                return mem
        print('No member found with ',mem_id)

    def print_mem_details(self):
        print('Members in Library : ')
        for mem in self.members:
            print(f'{mem.mem_id} {mem.mem_name}')

    def print_books_details(self):
        print('Books in Library : ')
        for book in self.books:
            print(f'{book.isbn}      {book.title} ({book.author})')


    def print_transaction_history(self):
        print('\n-----TRANSACTION HISTORY----\n')
        for mem in self.members:
            for b_obj, strr, d_date in mem.transaction_history:
                print(f"Book '{b_obj.title}' {strr} {d_date}")


lib = Library()

lib.add_book('Think & Grow Rich','Napolean Hill', '12300')
lib.add_book('Alchemist','Paul C','12400')
lib.add_book('Cant Hurt Me','David Goggins','12500')
lib.add_book('How to Win Friends','Andrew C','12600')

print()
print()

lib.add_member('Tanmay','L001')
lib.add_member('Utkarsh','L002')
lib.add_member('Abhishek','L003')

print()
print()

lib.borrow_book('L001','12300',date(2024,11,1))
lib.borrow_book('L002','12500',date(2024,11,14))
lib.borrow_book('L001','12400',date(2024,11,16))


print()
print()

lib.return_book_lib('L001','12300',date(2024,11,28))
lib.return_book_lib('L002','12500',date(2024,11,20))

print()

lib.find_member('L003')

print()

print(lib.find_book('12300').title)

print()

lib.print_mem_details()

print()

lib.print_books_details()

print()

lib.borrow_book('L002','12300',date(2024,11,15))

print()
print()


lib.print_transaction_history()















