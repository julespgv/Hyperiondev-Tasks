# holiday.py
"""
References:
I have read the Hyperion course materials and make use of learning
in earlier tasks, as explained below.
"""

#=====Functions=====
# User input prompt with error handling loops until user provides valid input. Some code recycled from Task 9
def get_valid_input(message=None, inp_type=None, options=None):
    while True:
        # Catch errors during the loop
        try: 
            # Request input type according to arguments passed
            if inp_type == "string":
                got_input = input(f"{message}")
            
            elif inp_type == "float": # Float used to permit input of decimal numbers
                got_input = float(input(f"{message}"))
            
            elif inp_type == "integer":
                got_input = int(input(f"{message}"))
                
                # Re-request if user enters a negative number of days
                if got_input < 0:
                    print("Value cannot be negative.")
                    continue
            
            # If user must select from multiple options
            elif inp_type == "menu":
                got_input = str(input(f"{message}")) 
                
                # User's input will be returned by function if it matches a menu option
                for element in options: 
                    if element == got_input: 
                        return got_input 

                # Display valid options in error message, then restart loop
                print(f"Error, please enter one of the following: {options}")
                continue
            
            # Return error-free input for non-menu input    
            return (got_input)
            
        except ValueError as error:
            # Advise user which type of input required, then restart loop
            print (f"{error} - Input must be {inp_type} type.")

# Function returns a destination selected by the user
def select_city(city_list):
    print ("You can choose from the below cities for your holiday:")
    # Loop through list to display all holiday options
    for city in city_list: 
        print (city)
    # User must re-enter choice if input is not an option in the list
    city_flight = get_valid_input("Enter your destination: ", "menu", city_list)
    return city_flight

# Calculate and return value of total hotel cost 
def hotel_cost(num_nights):
    return (float(num_nights * hotel_rate))

# Return flight cost dependent on destination city
def plane_cost(city_flight):
    if city_flight == "Bonn":
        return 300
    
    if city_flight == "Durban":
        return 800
    
    if city_flight == "Edinburgh":
        return 150

    if city_flight == "Salt Lake City":
        return 1000

# Calculate and return cost of car hire
def car_rental(rental_days):
    return (rental_days*car_cost)

'''Function calls subfunctions to calculate individual costs,
sums the results, then returns the total.'''
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_holiday_cost = (hotel_cost + plane_cost + car_rental)
    return total_holiday_cost

#=====Variables=====
# Define list of holiday destinations
city_list = ["Bonn", "Durban", "Edinburgh", "Salt Lake City"]

# User inputs requested for destination, nights at hotel, days of car rental:  
city_flight = select_city(city_list)
num_nights = get_valid_input("Stay for how many nights? ", "integer")
rental_days = get_valid_input("How many days of car hire? ", "integer")

# Setting *arbitrary* daily/nightly rates set for hotel and car hire:
hotel_rate = (100-(2*len(city_flight)))
car_cost = (80-(2*len(city_flight)))

# Attempt the below and catch errors
try:
    # Use above functions to calculate to nearest £1 GBP:
    total_holiday_cost = int(holiday_cost(hotel_cost(num_nights),\
                        plane_cost(city_flight), car_rental(rental_days)))
    print (f"Total cost is £{total_holiday_cost} for {num_nights} nights.")

# On error display message.
except:
    print("Error calculating total cost")
# End of program, thanks for reading.