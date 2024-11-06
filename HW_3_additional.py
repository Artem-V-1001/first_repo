'''
Об'єднати реалізовані системи входу та систему керуванням товарами
(створення читання оновлення видалення)
'''
# користувач {"login":str,password:str}

users = []
products = []
number_of_try = 3 
# Реалізувати функціонал регістрації і входу до системи із users

def login():
    user_login = input("Login user:")
    user_password = input("Password :")
    for user in users:
        if user_login == user["login"] and user_password == user["password"]:
            print(f"You entered as {user_login}")
            return user

def registration():
    user_login = input("Login user:")
    user_password = input("Password:")
    if user_login not in [user["login"] for user in users]:
        user = {"login":user_login,"password":user_password}
        users.append(user)
        print("Registration successful")

def check_try(user):
   global number_of_try
   if user is None:
       number_of_try -= 1
       print(f"Number of attemps {number_of_try}")
   if number_of_try < 1:
       print("All attemps wasted, restart application")

def create_product():
    products.append({"title":input("Enter the name of the product: "),
                     "description":input("Enter the description of the product: "),
                     "price":float(input("Enter the price of the product: "))})

def view_products():
    print("-"*25)
    for number,product in dict(enumerate(products,1)).items():
            print(f"{number}) {product['title']}")
            print("-"*25)

def product_working():
    print("-"*25)
    for number,product in dict(enumerate(products,1)).items():
        print(f"{number}) {product['title']}")
        print("-"*25)
        number = input("Choose the number of product: ")
        if number.isdigit() and 0 < int(number) <= len(products):
            number = int(number) - 1

            while True:
                new_choice = input("""1 read
2 edit
3 delete
4 previous step: """)
                if new_choice == "1":
                    print(products[number])
                if new_choice == "2":
                    product = products[number]
                    product.update({"title":input("Enter new name: "),
                                     "description":input("Enter new description: "),
                                     "price":float(input("Enter new price: "))})
                if new_choice == "3":
                    products.pop(number)
                if new_choice == "4":
                    break

def main_menu(user):
    print(f"Welcome, {user['login']}")
    while True:
        choice = input("""1 Create product
2 Read all products
3 Work with one product 
q Exit
Your choise: """)
        if choice == "1":
            create_product()
        if choice == "2":
            view_products()
        if choice == "3":
            product_working()
        if choice == "q":
            break


while True:
    choice = input("""1 Registration
2 Login
q Exit: """)
    if choice == "1":
        registration()
    if choice == "2":
        if number_of_try > 0:
            user = login()
            check_try(user)
            if user:
                main_menu(user)
                
    if choice == "q":
        break

