# contact03.class.py
'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
# Importing libraries
from datetime import datetime
import pickle

FILENAME = "contacts.dat"

choices = {'a':'Add contact', 'p': "Print Contacts", 'q': "Quit", 'h': "Help"}

class Person:
    """ Class Documentation """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = None
        self.office = None
        self.__private = None
        self.email = None
        self.address = None
        self.age = None
        self.date = self.__current_date()[0]
        self.time = self.__current_date()[1]
    
    def full_name(self):
        return self.first_name.title() +" " + self.last_name.title()

    def add_mobile_phone(self, number):
        """ Method documentation """
        
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_email(self, email):
        self.email = email

    def __current_date(self):
        now = datetime.now()
        day = now.day
        month = now.month
        year = now.year
        hour = now.hour
        minute = now.minute
        second = now.second
        return [f'{day}/{month}/{year}', f'{hour}:{minute}:{second}']

    def add_private_phone(self, number):
       self.__private = number

    def get_private_phone(self):
        try:
            return self.__private
        except:
            return False

    def save(self, obj, filename):
        with open(filename, 'ab') as file:
            pickle.dump(obj, file)

def cHelp(e=''):
    print(f"\n{e}") if e != '' else print()
    print ("""
        Usage operation:
            h                    Display this usage message
            a                    Add
            p                    Print
            q                    Quit
        """)

def menu():
    print("\n",f" Contacts ".title().center(50, '='), '\n')
    choice = input("              Enter choice (" + ''.join(((i+'|') for i in choices.keys()))+"):")
    
    return str(choice.lower()) if choice.lower() != '' else 'h'

def printContacts():
    with open(FILENAME, "rb") as file:
        data = []
        try:
            while True:
                data.append(pickle.load(file))
        except EOFError:
            pass
        p = input("\nDo you want to see with contacts a private phones ? (y|n): ")
        if p == "y" :
            for contact in data:
                print(f"\nИмя: {contact['first_name']} {contact['last_name']} \tOffice phone: {contact['office']} \tAdded At: {contact['date']} :{contact['time']} \tPrivate: {contact['_Person__private']}")
        else:
            for contact in data:
                print(f"\nИмя: {contact['first_name']} {contact['last_name']} \tOffice phone: {contact['office']} \tAdded At: {contact['date']} :{contact['time']}")
            
                


                
while True:
    choice = menu()

    if choice == 'q':
        print('{!s}'.format('\n             Thank You for using contact!'))
        break 
    
    if choice == 'h':
        cHelp()
        continue

    if choice == 'p':
        printContacts()
        
    
    if choice == 'a':
        print("\nAdd New Record To PhoneBook")

        first_name = input("\nFirst Name: ")
        last_name = input("\nLast Name: ") 
        office_phone = input("\nOffice Phone Number: ")
        
        person = Person(first_name, last_name)
        person.add_office_phone(office_phone)
        
        private = input("\nHave a private phone? (y|n): ")

        if (private == 'y'):
            private_phone = input("n\Private Phone Number: ")
            person.add_private_phone(private_phone)

        person.save(person.__dict__, FILENAME)
