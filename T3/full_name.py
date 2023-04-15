#  Ask user to provide their full name
full_name = input("Please type in your full name: ")

#  Display error if nothing was entered:
if len (full_name) == False:
    print ("You haven’t entered anything. Please enter your full name.")

#  Display error message if fewer than 4 characters:
elif len(full_name) < 4:
    print ("You have entered less than 4 characters. \
          Please make sure that you have entered your name and surname.")

#  Display error message if more than 25 characters:
elif len(full_name) > 25:
    print ("You have entered more than 25 characters. \
          Please make sure that you have only entered \
          your full name.")

#  If no error the input has been validated, display thanks:
else:
    print ("Thank you for entering your name.")