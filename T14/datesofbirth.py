""" Pseudocode
set up variables with headers "Name" and "Birthdate",
open file,
 read every line,
  assign names (first, last) / birthdates (day, month, year) to strings
  assign strings with names / birthdates to lists

 loop through printing names and dates from lists.
close file at program end. 
"""

# Declare list variables to store the lists of isolated names / birthdates    
names, dates = ["Name"], ["Birthdate"]

# Attempt to open file for reading (then close when finished)
with open('DOB.txt', 'r+') as file:

    # Loop through reading and processing each line in open file:
    for full_line in file:
        # split the words and assign these to a list 
        list_words_line = full_line.split()
        # Assign to string first 2 words as the name
        name_line = f"{list_words_line[0]} {list_words_line[1]}"
        # Assign to string last 3 words as birthdate.
        date_line = f"{list_words_line[2]} {list_words_line[3]} {list_words_line[4]}"

        # Add name string to list of all names: 
        names.append(name_line) 
        # Add date string to list of dates names:
        dates.append(date_line)

    # Loop through displaying header / all names 
    for name in names:
        print (name)
    print ("") # Empty newline between names/birthdates

    # Loop through displaying header and all birthdates 
    for date in dates:
        print (date)
# End of with: file will be closed.
