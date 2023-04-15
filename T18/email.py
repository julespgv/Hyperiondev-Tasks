### --- OOP Email Simulator --- ###
# References: HyperionDev course materials / previous learning in other tasks. 


# Class for Emails, described in the triple quote string below. 
class Email(object):
    # Include information about the object for reference
    '''
    This class creates an Email object, which contains an email address, subject line and content.
    Use the 'mark_as_read' method to change 'has_been_read' from False to True. 
    '''
    
    # Set default for emails as not read. 
    has_been_read = False

    # Initialise the instance variables for emails.
    def __init__ (self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content # Body of email

    # Create the method to change 'has_been_read' emails from False to True.        
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
Inbox = []

# --- Functions --- #
# Create new emails and add to list 'Inbox' by appending. 
def populate_inbox():
    # Create 3 new sample email objects, then append into Inbox list.
    email_1 = Email("sample@first.com",\
                    "Lost in space",\
                    "Did you know that this email\nhas just two lines?")
    email_2 = Email("second_thoughts@example.com",\
                    "Spoiler alert: I found you something boring to read!",\
                    "Please can you just finish the Task and stop writing nonsense. Thanks!")
    email_3 = Email("the_last@thefirst.com",\
                    "Motorcycle Sadness: the story of an immortalised theft",\
                    "Hi,\nI didn't what to write so here's something.\nEnjoy your day,\nJules")    
    
    Inbox.append(email_1)
    Inbox.append(email_2)
    Inbox.append(email_3)
        
# Function to display index and subject line of all emails.
def list_emails():
    print("\n    Emails in inbox:")
    # Loop through each email in the inbox. Enumerate used for tracking email index.
    for list_number, emails in enumerate(Inbox):
            print(f"    {list_number}  {emails.subject_line}")
    
# Function to displays a selected email from email inbox. 
def read_email(index):
    # display email address, subject, content
    email_chosen = Inbox[index]
    print (f"\nEmail {index}:") 
    print (f"Email address: {email_chosen.email_address}")
    print (f"Subject: {email_chosen.subject_line}")
    print (f"\n{email_chosen.email_content}\n")
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email_chosen.mark_as_read()
    print (f"Email marked as read.")
    
# --- Email Program --- #
populate_inbox()

menu = True # Set to False to end program:

# Main loop:
while menu == True:

    # User enters selection from below options:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    
    # Take user input for choice of email, then call associated function / end program.
    if user_choice == 1:
        # Display the full list of emails
        list_emails()
        
        # User provides index number for email to display.
        email_index = int(input(f"    Which email would you like to read? \
\n    Please enter an integer from 0 to {(len(Inbox)-1)}: "))
        # Call function to display text from specified email object in Inbox. 
        read_email(email_index)
            
    # Display subject lines of unread emails
    # (following note in Task instructions, no function used)    
    elif user_choice == 2:
        print("\nUnread emails in inbox:")
        # Presume no emails unread, then change to True if an unread one is found in the loop. 
        unread_remaining = False
        
        # Loop through each email in the inbox. Enumerate used for tracking email index.
        for list_number, emails in enumerate(Inbox):
            # Display message if no unread emails in inbox
            
            if emails.has_been_read == False:
                # There is an unread email, change variable accordingly, and display details to user:
                unread_remaining = True
                # Make intuitive by displaying list_number + 1 ('1','2','3'.. instead of '0','1','2'..)
                print(f"    {emails.subject_line}")
    
        # If no unread emails found inform user:
        if unread_remaining == False:
            print ("All emails have been read.")
        
    # Quit application/notify user if option 3 is selected.
    elif user_choice == 3:
        print("    Program terminating...")
        menu = False # Exit loop
        
    # Other input results in error message and restart loop:
    else:
        print("Oops - incorrect input.")
# End of program