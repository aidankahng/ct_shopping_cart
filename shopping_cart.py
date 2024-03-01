#Upon starting the program, initialize an empty list or dictionary to represent the shopping cart. Present a user-friendly menu that includes the following options:
#Allow users to add items to the shopping cart. For each item, prompt the user to input a name, quantity, and price. Store these details and add it to the shopping cart.
#Provide the ability to remove items from the shopping cart. Prompt the user to input the name of the item they wish to remove. Ensure to handle cases where the item is not found in the cart.
#Display the current contents of the shopping cart. Include the name, quantity, and price of each item, as well as a running total of the cost.
#Allow the user to exit the program. Upon quitting, print a summary of all items in the cart, including their details and the total cost.
#Implement a loop that continuously prompts the user for their choice until they decide to quit.
# Include appropriate error handling to deal with scenarios such as invalid input when adding or removing items.
# Ensure that the program provides a clear and user-friendly experience. Include informative messages and prompts to guide the user through each step.
# After the user quits, display a friendly closing message along with the final list of items in the cart and the total cost.
import csv
import random
import time

def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    dict_data = {}
    for i in range(len(data)):
        dict_data[data[i]['Item Name']] = data[i]
        dict_data[data[i]['Item Name']]['quantity'] = random.randint(1,15)
    
    return dict_data

def remove_from_cart(cart:dict, key:str):
    removed = cart.pop(key, 'failed')
    if removed == 'failed':
        print(f"Failed to remove {key} from the cart")
    else:
        print(f"Successfully removed all {key} from the cart")

def display_cart(cart):
    total_cost = 0
    print("-"*40)
    print("\tYOUR CART")
    print("-"*40)
    if cart == {}:
        print("There is nothing in your cart!")
    else:
        for item_key in cart:
            total_cost += int(cart[item_key]['quantity']) * float(cart[item_key]['value'])
            print(f"{cart[item_key]['quantity']} x {item_key} at ${float(cart[item_key]['value']):.2f} ea")
    print("-"*40)
    print(f"\tTOTAL COST: ${total_cost:.2f}")
    print("="*40)

def add_to_cart(cart, items):
    for i in items:
        cart[i] = items[i]

def shop():
    # Initialize dictionary shopping cart
    cart = {}
    shopping = True
    print("\n\tWelcome to VeggieMart. \nWe sell veggies and things that eat veggies")
    print("If you were looking for VeganMart, they closed due to lack of sales.\n")
    while shopping:
        action = input("Add/Remove/Cart/Clear/Mystery/Quit? ").lower()
        if action == 'quit':
            break
        elif action == 'add':
            item_value, item_quantity = "notFloat", "notDigit"
            item_name = input("What item would you like? ").title()
            while not all(x.isdigit() or x == "." for x in item_value):
                item_value = input("How much does that cost? ")
            while not all(x.isdigit() for x in item_quantity):
                item_quantity = input("How many would you like? ")
            item = {item_name:{"value":float(item_value), "quantity":int(item_quantity)}}
            add_to_cart(cart, item)
        elif action == 'remove':
            remove_key = input("What item would you like to remove? ").title()
            remove_from_cart(cart, remove_key)
        elif action == 'cart':
            display_cart(cart)
        elif action == 'clear':
            is_full = False
            if len(cart) > 10:
                is_full = True
                print(f"You have a lot of items in your cart\nIt seems as though someone had lovingly chosen them with you\nAre you sure you want to empty your whole cart?")
            confirm_clear = input("Type clear again to confirm (this is not reversible): ").lower()
            if confirm_clear == 'clear':
                cart = {}    
                print(f"Cart has been emptied.")
                if is_full:
                    print(f"An elderly woman scowls as you return dozens of frozen items to their shelves")
                    time.sleep(0.5)
                    print(f"Your fingerprints cover the produce aile")
                    time.sleep(0.5)
        elif action == 'mystery':
            print('A staff member shops for you!')
            time.sleep(0.1)
            print('Filling up produce...')
            time.sleep(0.1)
            print('Filling up proteins...')
            time.sleep(0.1)
            print('Stockpiling for your bunker...')
            time.sleep(0.1)
            print('Feeding your neighbors...')
            time.sleep(0.5)
            mystery_items = read_csv("./store.csv")
            add_to_cart(cart, mystery_items)
            print('The staff member smiles as they return with your cart')
            time.sleep(0.5)
            print('Your cart is now overflowing with items')
            input("Press enter to see your new cart")
            display_cart(cart)
    display_cart(cart)
    if len(cart) > 0:
        print(f"Thank you for shopping at VeggieMart. \nPlease come again.")
    else:
        print(f"The security guard stares you as you leave empty handed")

if __name__ == "__main__":
    shop()