# f = open("file.txt", "r+")
# to_do_list = []
# def show_list():
#     print("\nto_do_list:")
#     print("1. Vazifa yozish")
#     print("2. Vazifa ko'rish")
#     print("3. Vazifa o'chirish")
#     print("4. Tugadi")
    
# def shart():
#     shart = input("Vazifa kiriting:")
#     to_do_list.append(shart)
#     print("Vazifa qushildi:{shart}")
    
# def kursatish():
#     if not to_do_list:
#         print("Ro'yxat bo'sh")
#         for idx, task in enumerate(todo_list, start=1):
#             print(f"{int}. {shart}")
    

# def remove_task():
#     try:
#         view_tasks()
#         task_number = int(input("O'chirish uchun vazifa raqamini kiriting: "))
#         if 0 < task_number <= len(to_do_list):
#             removed_task = todo_list.pop(task_number - 1)
#             print(f"Vazifa o'chirildi: {removed_task}")
#         else:
#             print("Noto'g'ri raqam.")
#     except ValueError:
#         print("Faqat raqam kiriting.")


# while True:
#     show_menu()
#     choice = input("\nBuyruqni tanlang (1-4): ")
    
#     if choice == '1':
#         add_task()
#     elif choice == '2':
#         view_tasks()
#     elif choice == '3':
#         remove_task()
#     elif choice == '4':
#         print("Dasturni yopish...")
#         break
#     else:
#         print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")


# class Book:
#     def __init__ (self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def display_info(self):
#         print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")
# my_book = Book ("Anjir gullari", "F.Shahzoda", "2005")
# my_book.display_info()

# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year

#     def get_age(self):
#         from datetime import datetime
#         current_year = datetime.now().year
#         return current_year - self.publication_year

# my_book = Book("2024", "George Orwell", 2003)
# print(f"Book: {my_book.title}, Year: {my_book.get_age()} yil")

# class Book:
#     def __init__(self, title, author, year, page_count):
#         self.title = title
#         self.author = author
#         self.year = year
#         self,page_count = page_count


# class Ebook(Book):
#     def __init__(self, file_size):
#         super().__init__(title, author, year, page_count)
#         self.file_size = file_size

#     def charge(self):
#         print(f" File size: {self.file_size} 128")

# Flowers = Ebook("Fig flowers", "Louis", 2023, 128)


# 4
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"{amount} deposited. New balance: {self.__balance}")
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount} withdrawn. New balance: {self.__balance}")
#         else:
#             print("Insufficient funds")
#     def get_balance(self):
#         return self.__balance

# deposit = BankAccount(1000)
# deposit.deposit(500)
# print("Balance:", deposit.get_balance())



# 5
# class Book:
#     def __init__(self, title):
#         self.title = title
# class Author:
#     def __init__(self,name):
#         self.name = name
#         self.books = []
#     def add_book(self, title):
#         book = Book(title)
#         self.books.append(book)
#     def get_books(self):
#         return [book.title for book in self.books]

# author = Author("John Doe")
# author.add_book("Book One")
# author.add_book("Book Two")
# print(author.name)
# print(author.get_books())



# 6
class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books
    def add_book(self, name, books):
        book = books(name)
        self.books.append(book)
        print(f"add_book")
    def remove_book(self, name, books):
        book = books(name)
        self.books.remove(book)
        print(f"remove_book")
    def get_book(self):
        return [self.books]
