'''References
This is my own work, I have read the Hyperiondev course pdfs,
so make use of functions, lists, exit(), eval(), use of 'os' library.

I have followed feedback from a mentoring session looking at this code
and separated my pseudocode into a different file, and reduced the comments.

Extra guidance for eval():
https://docs.python.org/3/library/functions.html#eval

File operations guidance:
https://docs.python.org/3/library/functions.html#open
https://docs.python.org/3/tutorial/inputoutput.html#tut-files
'''
#=====import os library=====
import os

#=====Global variables=====
# User can select one of these program modes
modes = ("calc", "read", "exit")
# User can select one of these operators
operators = ("+","-","*", "**","/", "//","%")
# string used to display operators for user guidance
operators_legible = " or ".join(operators)
# Program mode and got_input start undefined.
program_mode, got_input = None, None 

#=====Functions=====
def calc_mode():
    ''' Take user input and form expression / calculate result
Display resulting expression / result to user.
Then write equation to file
    '''
    # Handle errors
    try:
        first_num = get_valid_input("Please enter the first number", "float")
        second_num = get_valid_input("Please enter the second number", "float")
        # User must enter operator from limited selection
        operator = get_valid_input(f"Enter either {operators_legible}", "menu", operators)
        # Expression formed from above variables        
        expression = str(first_num)+operator+str(second_num)
        # Check expression yields a valid result:
        result = get_equation_result(expression)

        if result != "Error":
            # Concatenate expression and result to write to file
            equation = f"{expression}={result}"
            # Display result and full equation to user
            print (f"Expression {expression} gives the following result: {result}")
            
            # Write equation to file
            file_operation("write", "output.txt", equation)

        # Display error message if unable to calculate result
        elif result == "Error":
            print(f"Error: Expression '{expression}' did not give a valid result.")
    
    # Display error message
    except:
        print ("Error encountered in calculator mode! Exiting program.")


def get_equation_result(expression):
    '''Returns result of evaluating expression, or returns "Error"'''
    try:
        # If the expression is valid (e.g. no divide by zero) will return the result.
        return eval(expression)
    except:
        return "Error"

def get_valid_input(message=None, inp_type=None, options=None):
    '''This function handles all requests for validated user input.
validation is according to the input type passed as an argument.
    '''
    got_input = None
    while True: #Will loop user input request until user gives a suitable answer.
        try:
            if inp_type == "string":
                got_input = input(f"{message}: ")
            elif inp_type == "float": # Float used to permit input of decimal numbers.
                got_input = float(input(f"{message}: "))
            elif inp_type == "menu":
                got_input = str(input(f"{message}: ")) 
                
                # Users input is valid if it matches a value found cycling through the menu tuple:
                for element in options: # Loop through each 'menu' option in a list/tuple/set.
                    if element == got_input: # compare each element to user input.
                        return got_input # Exit loop, function will return input value. 

                #Error if no match found; offer advice and request again
                print(f"Error, please enter one of the following: {options}")
                continue #restart 'while' loop. 
                                     
            return (got_input) # If no exception for non-menu variables, return the validated input
            
        except ValueError as error: #User should be notified of exception and offered advice, then will restart loop.
            print (f"{error} - Input must be {inp_type} type.")
        except:
            print ("Error!")

def file_operation(permission="read", filename="output.txt", equation=None):
    '''Attempt to open a file with specified arguments.
This is used both to write calc_mode,
and to perform read/display in read_mode
    
    '''
    if permission == "write":
        permission = 'a' # Append to file when writing
    
    if permission == "read":
        permission = 'r' # Open read-only when reading.

    # As the above was successful, now read/write file:
    try:
        file = open(filename, permission)
        
        # If reading from file:
        if permission == "r":
            
            for line in file:
                print(line)
            print("End of file.")
            
        if permission == "a":
            # write the equation, plus newline, to the end of the file.
            file.write(equation+f"\n")
            print(f"Wrote equation to {filename}")        
    
    except FileNotFoundError as error:
        print(error)
    except:
        print ("Error writing/reading file.")
    # Close file if it is open.
    finally:
        
        if file is not None:
            file.close()

def read_mode():
    '''Read from user-specified filename'''
    # Loop until the user enters a name of a file that exists
    while True:
        try:
            filename = input("Enter the filename, or type '-1' to go back: ")
            
            if filename == '-1':
                print ("Returning to menu")
                break
            
            # Check if file exists using 'os' library (Task 17)
            elif not os.path.exists(filename):
                print("Error: File does not exist. Please try again.")            
            
            else:
            # Call function to open file, read each line and print to screen:
                file_operation("read", filename)
                # Exit loop once read and displayed to user.
                break 

        except:
            print ("Error in attempting file read.")
            continue


def run_time():
    '''Defines main function of program'''
    # Check which mode to run:
    program_mode = get_valid_input("Enter 'calc' to calculate the result of two numbers and an operator.\
\nEnter 'read' to view all contents of a file \
\nOr enter 'exit' to exit the program", "menu", modes)

    # Program will run function dependent on user input, with error handling
    if program_mode == "read":
        try:
            read_mode()
        except:
            print ("Read mode error.")

    elif program_mode == "calc":
        try:
            calc_mode()
        except:
            print ("Calculation mode error.")    

    elif program_mode == "exit":
        print ("Exiting program.")
        exit()

# Run the program until user intentionally exits
while True:
    run_time()
    # Display message each time when returning to menu 
    print("Returning to menu") 