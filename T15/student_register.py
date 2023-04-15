# Task 15 student_register.py
""" References and pseudocode
Using def (functions) referenced in later Hyperiondev material.
Previous learning of techniques from T9 and T11 tasks,
 for error-free input methods
 and checking if strings contain alpha/numeric values

Using str.isnumeric (https://docs.python.org/3/library/stdtypes.html)
 for function to account for IDs with trailing zeroes (as occurs in real life).

Pseudocode:
 Function defined to take in valid number input
  (prevents program crashing / losing all progress if invalid input entered)
 Function to check if input contained only int numbers.
 Define output file location, permissions.
 Open output file for writing
  Determine number of students
  Start loop to receive input from students (id) and write to file
   Assign input from each student to id variable 
   write string with (id variable, newline, dotted line) to output file.
 When loop ends, close file
 User informed file written. 
"""

# Function asks for input from user.
# Returns a validated number input from user, or loops to re-request.
def error_free_input(req_text, mode = None):
    # loop until user provides valid number:
    while True:
        # Errors handled to prevent inconvenient crashes
        try:
            # Unless in 'id' mode ask only for integer numbers: 
            if mode == None:
                inp_num = int((input(req_text) ))
                
                # Check and flag if less than 1 student:
                if inp_num < 1: 
                    print ("Error, number entered was less than 1. Try again.")
                    continue # Loop again.
            
            # If asking for student ID accept numbers with trailing zeroes:
            elif mode == "id":
                inp_num = str((input(req_text) ))
                # Check if the string is made up only of numbers:
                if check_is_number(inp_num) != True:    
                    
                    continue  # Loop again.
                
            # If no error, return the value.        
            return inp_num
        
        # Display error messages to guide user.
        except:
            print("Please enter integer numbers only. Trailing zeroes permitted.")

# Returns True/False whether characters are only numbers.
def check_is_number(string):
    # Loop through each character of the string passed.
    for counter in range(0, len(string)):
        # If a character is not a number display error:
        if str.isnumeric(string[counter]) == False:
            print (f"Error! Please enter a student ID number. Try again.")
            # Have found a non-number, return False.
            return False
    # return True as string contains only numbers.    
    return True


# String variables with filename, permission to open file (write only),
filename, permission, = "reg_form.txt", "w"


# Using 'with' to open file and automatically close when finished.
with open(filename, permission) as ofile:
    # Assign to variable a valid integer:
    total_students = error_free_input("How many students are registering? ")
    # Loop for each student entering their ID:
    for counter in range (total_students):
        # Empty string to include student id / dotted line to write to file:
        sign_line = ""
        stu_id = error_free_input("Please enter your ID number: ", "id")        
        # Assign student ID to string with signature line:
        sign_line += f"ID number: {stu_id}\nSigned: .............................\n" 
        # Write id and signature line to file:
        ofile.write(sign_line)

# file closes at end of 'with'. Inform user write was successful.
print(f"Register is ready, see {filename}.")
# End of file, thanks for reading