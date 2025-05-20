#Personal Finance Tracker

import time
import pickle

def get_menu_option():
    user_option = 0
    while True:
        user_response = input("\nWhich option do you choose? ")
        try:
            user_option = int(user_response)
        except:
            print("\nPlease enter a valid number corresponding to the option you wish to select, the is the number presented like (6)")
            continue
        if user_option < 1 or user_option > 5:
            print("\nPlease enter a valid number corresponding to the option you wish to select, the is the number presented like (6)")
            continue
        break
    return user_option

def get_expense():
    while True:
        description = input("\nEnter expense description: ")
        if description == "":
            print("\nPlease enter a description")
            continue
        break
    
    while True:
        category = input("Enter category: ")
        if category == "":
            print("\nPlease enter a category")
            continue
        break
    
    while True:
        amount = input("Enter amount: ")
        try:
            amount = float(amount)
        except:
            print("\nPlease enter a float value")
            continue
        break
    return description, category, amount

def add_expense(data):
    while True:
        user_response = input("\nWould you like to enter a new expense? (y/n): ")
        if user_response.lower() == 'n':
            break
        elif user_response.lower() == 'y':
            pass
        else:
            print("\nPlease enter y or n")
            continue
        
        description, category, amount = get_expense()
        
        if category not in data.keys():
            data[category] = []
        data[category].append((description, amount))
        time.sleep(1)
        print("\nExpense added successfully")

def view_expenses(data):
    for category in data:
        time.sleep(1)
        print("\nCategory:", category)
        for expense in data[category]:
            time.sleep(1)
            print(f"\t- {expense[0]}: ${expense[1]}")
            
def total_amount(data):
    count = 0
    for expense in data:
        count += expense[1]
    return count

def view_summary(data):
    time.sleep(1)
    print("\nSummary:")
    for category in data:
        time.sleep(1)
        print(f"{category}: ${total_amount(data[category])}")

def clear_expense(data):
    while True:
        user_response = input("\nAre you sure you want to clear all expenses? (y/n): ")
        if user_response.lower() == 'n':
            break
        elif user_response.lower() == 'y':
            pass
        else:
            print("\nPlease enter y or n")
            continue
        print("\nClearing all expenses...")
        time.sleep(1.5)
        data.clear()
        break
        
def menu_action(user, data):
    if user == 1:
        add_expense(data)
    elif user == 2:
        view_expenses(data)
    elif user == 3:
        view_summary(data)
    else:
        clear_expense(data)
        
file_path = "C:\\Users\\tyagi\\Documents\\CognizantExternship\\python-capstone-finance-tracker\\data.pkl"
try:
    with open(file_path, "rb") as file:
        expenses = pickle.load(file)
except:
    expenses = {}

if expenses:
    print("Welcome Back to the Personal Finance Tracker! We have your prevoius expenses saved!\n")
    time.sleep(1.5)
else:
    print("Welcome to the Personal Finance Tracker!\n")
    time.sleep(1)

while True:
    print("Please selective which option you would like by entering the corresponding number:")
    time.sleep(1)
    print("(1) Add Expense")
    time.sleep(1)
    print("(2) View All Expenses")
    time.sleep(1)
    print("(3) View Summary")
    time.sleep(1)
    print("(4) Clear Expenses")
    time.sleep(1)
    print("(5) Exit")
    
    user_option = get_menu_option()
    
    if user_option == 5:
        print("\nWe'll keep your expenses saved! Until next time")
        with open(file_path, "wb") as file:
            pickle.dump(expenses, file)
        time.sleep(1)
        break
    
    menu_action(user_option, expenses)
    
    print("")
    time.sleep(1.5)