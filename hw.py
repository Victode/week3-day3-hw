cart = {}

def show():
    print("=~" * 15)
    print("SHOPPING CART:")

    for key, val in cart.items():
        total = val['quantity'] *  val['price']
        print(f"{key.title()} x {val['quantity']}: ${'{:.2f}'.format(total)}")
        
    print("=~" * 15)

def add_list(item, quantity, price):
    cart[item] = {
        'quantity': quantity,
        'price': price
    }

def delete(item):
    del cart[item]

def main():
    while True:
        try:
            nav = input("Would you like to (show/add/delete/quit)?")
            if nav == "show": 
                show()

            elif nav == "add":
                name = input("What would you like to add to your cart?")

                if len(name) < 2:
                    raise ValueError("Name input not valid, input cannot be one character.")

                quantity = input("How many are you buying?")

                if quantity != int(quantity):
                    raise Exception("Quantity input not valid, input needs to be a number.")

                price = float(input("product price?"))
                add_list(name, quantity, price)

                if price == float(price):
                    raise ValueError("Price input not valid.")

            elif nav == "delete":
                name = input('What would you like to take out? ')
                delete(name)

                if name != cart.items(): 
                    pass

            elif nav == "quit":
                show()
                print("Thank you! Have a nice day!")
                break
        except ValueError as error:
            print("There was an error.")
            print(error)
   
        except Exception as error:
            print("There was an error. Your input was invalid.")
main()