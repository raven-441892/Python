#Beckett Pizza Plaza cashier, Chloe The Pizza Price Calculator

def input_validation(a):
    """checks if the user input has any errors or not and runs the code till right entry is taken"""
    while True:
        try:
            user = input(a).lower()
            if user not in ['y','yes','n','no']:
                raise ValueError("Please enter 'y' or 'yes' or 'n' or 'no'") #if value error not raised then if wrong input is entered then that error raising info runs into infinite loop 
            return user
        except ValueError as e:
            print(f"Invalid input! {e}")

def customer_input():
    """Takes input from the user"""
    
    print("\n")
    print("Welcome to Beckett Pizza Plaza".rjust(50))
    print("================================".rjust(51))
    print("Dear Customer, I'm Chloe The Pizza Price Calculator\n".rjust(62))
    while True:
        try: 
            number_of_pizza = int(input("How many pizzas ordered? \n"))
            if number_of_pizza < 0:
                print("Please enter a positive number!")
            else:
                delivery = input_validation("Is delivery required? (y/yes/n/no): \n")
                day = input_validation("Is it Tuesday? (y/yes/n/no): \n")
                app = input_validation("Did the customer use the BPP app? (y/yes/n/no): \n")
                return number_of_pizza, delivery, day, app
        except:
            print("Please enter proper number!")


def pizza_price(number_of_pizza):
    """ Calculation for the pizza price only without any discount """
    pizza_price_per_piece=12
    total=pizza_price_per_piece*number_of_pizza
    return total

def tuesday_discount_offer(day,total):
    """ Calculation for the pizza price with Tuesday discount offer"""
    if day.lower()=="y" or day.lower()=="yes":
        tuesday_discount= total*0.5
        return tuesday_discount
    else:
        return 0
    
def delivery_charge(number_of_pizza,delivery):
    """ Calculation for pizza price  weather to add delivery charge or not"""
    if delivery.lower()=="y" or delivery.lower()=="yes":
        if number_of_pizza>=5:
            return 0
        else:
            delivery_amt=2.50
            return delivery_amt
                 
    else:
        return 0

def app_discount(app, total, delivery_amt, day):
    """Calculate the app discount"""
    if app.lower() == "y" or app.lower()=="yes":
        if day.lower() == "y":
            discount_price_tuesday = (total + delivery_amt) * 0.5
            app_discount_price = discount_price_tuesday * 0.25
        else:
            app_discount_price = (total + delivery_amt) * 0.25
        return app_discount_price
    return 0


def calculation(total, tuesday_discount, delivery_amt, app_discount_price):
    """Calculate the total price with above present discounts"""
    grand_total = total
    
    if tuesday_discount > 0:
        grand_total -= tuesday_discount
        
    grand_total += delivery_amt
    
    if app_discount_price > 0:
        grand_total -= app_discount_price
    
    return grand_total

def output(number_of_pizza,delivery,total,tuesday_discount,delivery_amt,app_discount_price,grand_total):
    """"Displays the grand total of the pizza in a proper format"""
    print(f"\nDear Customer, Your total charge for the order is:\n") 
    print(f"Total pizza price".ljust(30), f"£{total:.2f}".rjust(10))
    print(f"Tuesday discount".ljust(30), f"-£{tuesday_discount:.2f}".rjust(10))
    if 0<number_of_pizza<5 and (delivery.lower()=="y" or delivery.lower()=="yes"):
        print(f"Delivery Charge".ljust(30), f"+£{delivery_amt:.2f}".rjust(10))
    else:
        print(f"Delivery Charge".ljust(30), f"-£{delivery_amt:.2f}".rjust(10))
    print(f"App discount".ljust(30), f"-£{app_discount_price:.2f}".rjust(10))
    print("============================================")
    print(f"Grand Total".ljust(30), f"£{grand_total:.2f}".rjust(10))
    print("\nPlease Visit Again !!!\n")
                       
                 
num,delivery,day,app=customer_input()
price=pizza_price(num)
tuesday=tuesday_discount_offer(day,price)
delivery_stuff=delivery_charge(num,delivery)
apps=app_discount(app,price,delivery_stuff,day)
calculate=calculation(price,tuesday,delivery_stuff,apps)
display=output(num,delivery,price,tuesday,delivery_stuff,apps,calculate)

                        
# num=number_of_pizza
# delivery=delivery
# day=day
# app=app
# price=total 
# tuesday=tuesday_discount 
# delivery_stuff=delivery_amt 
# apps=app_discount_price 
# calculate=grand_total              
            
