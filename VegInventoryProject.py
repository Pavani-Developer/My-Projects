veg = ["tomato",'onions','chillies','potatos']
quantity = [30,50,25,40]
price = [20,25,15,30]
#we store amount of each item that customer  buy's and sum up last when customer wants to stops shopping
total_amount = [] 

while True:

    item = input("Enter what do you want : ")
    if item in veg:
        item_index = veg.index(item)
        
        customer_asked_quantity = float(input("Enter quatity :"))
        if customer_asked_quantity <= quantity[item_index]:
            amount = customer_asked_quantity * price[item_index]
            quantity[item_index] = quantity[item_index] - customer_asked_quantity
            #appends each items bill to the list called total_amount 
            total_amount.append(amount) 
        else:
            print("We don't have that much quatity")


    else:
        print(item,'Not available right now!')
    
    continue_or_not = input("Do you want continue buying vegetables (yes/no) : ")
    if continue_or_not == 'no':
        print("The total amount of your vegetable shopping is:",sum(total_amount)) # using sum function we calculate total sum of customer bill
        print("We're closing shop ")
        print("*" * 10 ,"Final Report", "*" * 10)
        for i in zip(veg,quantity):
            print(i)
        break
    
        
