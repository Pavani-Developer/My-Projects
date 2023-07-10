#Write a python program to manage a fruits shop inventory and transactions like mentioned below
#Should have inventory with fruits information like name,quantity and price
#Transaction are like :
""" 1. It has to check the availability of fruits
    2. And bill has to generated for the fruits he/she bought , a customer can buy multiple types of fruits in one transaction
    3.And the list of remainig items along with their quantities
"""

fruits = ["apple",'orange','mango','guava','banana','grape','pineapple']
quantity = [150,60,70,100,75,65,90]
prices = [100,50,150,60,70,50,90]
bill = []

#if 'who' is yes that means user is a customer 
#Below program gonna excute

who = input("Are you a customer or Owner if you are a Customer enter 'Yes': ")
if who == 'yes':
    while True:
        fruit_name = input("Which fruit do you want to buy Enter fruit name in lowercase : ")
        if fruit_name in fruits:
            user_quan = float(input("How much quantity do you want(in kgs): "))
            fruit_idx = fruits.index(fruit_name)
            if user_quan > quantity[fruit_idx]:

                print("We don't have that much quantity")

            else:
                price = prices[fruit_idx] * user_quan
                bill.append(price)
                quantity[fruit_idx] = quantity[fruit_idx] - user_quan
                    

        else:
            print("We don't have that fruit! Sorry!")
        
        shopping = input("Do you want continue Shopping (yes/no):")

        if shopping == 'no':
            for i in zip(fruits,quantity):
                print(i)
            print("We're closing this shopping for you , before you exit pay bill !")
            print("Total amount is : ",sum(bill))
            print("Have a nice Day!")
            break
#Creating Owners Page which is used to add items and quantity 
#If 'who' is 'no' user is owner to excute below program it asks owner password 


else:
    password = input("Enter Password: ")
    if password == 'Password1234':
        print("***************BEFORE ADDING FRUITS 'REPORT'***************")
        for i in zip(fruits,quantity):
            print(i)
        #Above for loop prints report before adding any items to previous list
        while True:
            #Program asks for owner opinion if he/she wanted to add items to the inventory program asks for that
            owner_choice = input("Do you want to add any items to your Inventory(yes/no): ")
            if owner_choice == 'yes':
                add_item = input("Enter fruit name if you want to add it to this inventory: ")
                #We check if user wants to add an existing item we only add the quantity to existing quantity
                if add_item in fruits:
                    add_quan = int(input("Enter quantity of fruits you added : "))
                    fruit_index = fruits.index(add_item)
                    quantity[fruit_index] = add_quan + quantity[fruit_index]
                #If it's not in there we add fruits name ,quantity and prices to the lists respectivily
                else:
                    fruits.append(add_item)
                    add_quan = int(input("Enter quantity of fruits you added : "))
                    quantity.append(add_quan)
                    price_add = float(input('Enter price per kg: '))
                    prices.append(price_add)
            else:

                print("*" * 15, "AFTER ADDING FRUITS 'REPORT'","*"*15)
                for i in zip(fruits,quantity):
                    print(i)
                break
    else:
        print("Password incorrect! Try Again")
