# References: https://realpython.com/python-enumerate/ Enumerate example used for loop counter
# instead of declaring 'count = 0' a few times, or using functions.

# Rough pseudocode used to structure:
# Create menu list (Acts as key in lists/dictionaries)
# Create populated stock_list = [(menu_item, quantity),...],
# + create stock dictionary = dict(stock_list)
# Create populated price_list = [(menu_item, cost),...]
# + create price dict = dict(price_list) 
# Loop through dictionaries' prices and stock numbers, then display calculation. 


# Define list containing menu.
menu = ["Roast beef", "Haricot beans and gruyere cheese on toast",\
        "Miscellaneous meat and vegetables burger",\
        "Tomato mozzarella jalapeno pizza",\
        "Avocado and papaya smoothie"]


# Stock dictionary
# Create list to contain menu item names and stock.
stock_list = []
quantity = 1 # arbitrary estimations for stock (and prices) used throughout.

# Loop through each menu item and create stock list:
for counter, item in enumerate(menu):
    # arbitrary stock numbers used.
    quantity += counter 
    # add each menu item and its stock value at the end of the list.
    stock_list.append((item, quantity))

# Define the stock dictionary, keys and values variables:
stock = dict(stock_list) 
stock_keys = stock.keys()
stock_values = stock.values()


# Price dictionary:
cost = 2 #Arbitrary cost of an SKU (individual stock keeping unit/item)
price_list = []

# Create list of menu items and prices:
for counter, item in enumerate(menu):
    cost += (3-counter) # arbitrary SKU prices
    # add each menu item and its SKU cost to end of the list:
    price_list.append((item, cost))

# Define the dictionary, keys and values variables
price = dict(price_list)
price_keys = price.keys()
price_values = price.values()


# Display value of all stock.
# define variable for total value of stock.
total_stock = 0

#Loop through each item (by key) and multiply the quantity of stock held by the price:
for counter, item in enumerate(price_keys): # Each 'item' is from the menu list.

    # using the key, the value of item stock / price is returned with .get()
    item_value = stock.get(item) * price.get(item) 
    # Add this to the running total of stock's value:
    total_stock += item_value


# Display stock value, which is the end of the program.
print(f"Value of stock is currently £{total_stock}.")
