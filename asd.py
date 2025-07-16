bookset=set()
def add_book():
    global bookset
    numofBooks = int(input("Enter number of books to add: "))
    for i in  range(numofBooks):
     book = input(f"Enter book name {i+1}: ")   
     bookset.add(book)
    print(f"{numofBooks} books added successfully!")
    
    print("Books in the library:", bookset)
    

def remove_book():
    global bookset
    namebook= input("Enter the name of the book to remove: ")
    if namebook in bookset:
        bookset.discard(namebook)
        print(f"Book '{namebook}' removed successfully!")
    else:
        print(f"Book '{namebook}' not found in the library.")
def search_book():
    global bookset
    namebook = input("Enter the name of the book to search: ")
    if namebook in bookset:
        print(f"book '{namebook}' is available in the library.")
    else:
        print(f"book '{namebook}' is not available in the library.")
def display_books():
    global bookset
    print("Books in the library:")
    for book in bookset:
        print(f"- {book}")

def display_message():
    print("          HALLO IN LIBRARY         ")
    print('          -----------------         ')
    print("          1. Add Book              ")
    print("          2. Remove Book           ")
    print("          3. Search Book           ")
    print("          4. Display Books          ")
    print("          5. Exit                  ")
    print('          -----------------         ')
    
while True:
    
    display_message()
    choise=int(input("Enter your choice: "))
    if choise == 1:
        add_book()
        y=bool(input("Do you want to continue? (True/False): "))
        if y:
         continue
        else:
         break
         
    elif choise == 2:
        remove_book()
        y=bool(input("Do you want to continue? (True/False): "))
        if y:
         continue
        else:
         break
         
    elif choise == 3:
        search_book()
        y=bool(input("Do you want to continue? (True/False): "))
        if y:
         continue
        else:
         break
         
    elif choise == 4:
        display_books()
        y=bool(input("Do you want to continue? (True/False): "))
        if y:
         continue
        else:
         break
         
    elif choise == 5:
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")