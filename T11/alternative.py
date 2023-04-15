"""Reference materials from Hyperiondev, including materials for def / functions,
To check if something is a word (not blank string / non-letter characters):
https://stackoverflow.com/questions/15558392/how-can-i-check-if-character-in-a-string-is-a-letter-python
https://docs.python.org/3.8/library/stdtypes.html#str.isalpha

Alternating explanation:
I have limited previous experience using booleans (or mod 2) methods
for simple alternating.

Re. the second part of the task:
 Only letter characters can actually be capitalised.
 A function checks if a series of characters is a word
 (after/before which there are spaces - use of split)
 It is a word only if it contains letters.
 
 If no letters, the flip bit won't change in this loop iteration,
 so the case won't be changed from how it was for the previous real word.
 The flip bit will only change (hence the case too) when it next sees a 'word'.

 This prevents changing case in non-word sections e.g.
 "pIE 3 tHEN" => "pIE" is a word, "3" not a word (no letters), "tHEN" is a word.
 So we correctly print "PIE 3 then" instead of "PIE 3 THEN".
 
Rough pseudocode:
Part 1:
Read in string input from user.

Loop through input string,
 assign to new string:
 characters from input str, one at a time, alternately put into lower/upper case

Part 2:
Split input string, using space " " as delimiter: creates a list of elements.
Define function to check whether each element is a word/non-word.

Loop through each element of the list
 Call function to check if it has letters in it, so is a 'word'
  If it is a word, flip the bit so the case is opposite to previous 'word'.
  If not a word, don't flip.
 Depending on flip bit, assign element to new list in either upper/lower case.

Join modified word list (alternating caps) into string
Print modified strings with alternate characters, alternate words.

"""

orig_string = input("Please enter a string.\n")

# Part 1 solution
# create new string to contain alternating characters in lowercase/uppercase:
string_alt_characters = ""

# Loop counter, and a flipbit for alternating:
counter, flip = 0, True

# count through orig_string from first to last character:
for counter in range (0,len(orig_string)): 

    # Alternate between True/False for each iteration of the loop below.
    flip = not flip
     
     # Add current letter to new string as lower/uppercase:
    if flip==False: 
        string_alt_characters += orig_string[counter].upper()
    else:
        string_alt_characters += orig_string[counter].lower()

# Part 2 solution: put into upper/lowercase alternate words

# Create a list splitting the potential words of the original string:
string_split_up = orig_string.split(" ")
# List to hold modified words:
string_in_list = []
# String for printing to user, with alternate upper/lowercase words:
string_alt_words = ""

'''Function to check if a part of the string is a word with letters to lowercase/capitalise.
   It will return True if it has letters, or False if it has none.'''
def contains_characters(string_list, element):
    # variables for function
    contains_non_alpha = False
    contains_alpha = False
    counter = 0

    # String without characters returns False as it contains no letters.
    if element == "": return False
    
    # Iterate through every character in the element (where the function was called)
    # Update variables when alpha/non-alpha characters found.
    for counter in range(0, len(element)): 
        if str.isalpha(element[counter]) == True: contains_alpha = True
        if str.isalpha(element[counter]) == False: contains_non_alpha = True
    if (contains_alpha == False) and (contains_non_alpha == True):
        return False # No letters in series of characters. Include in output as-is.
    else:
        return True  # element in list has letters, so will invert 'flip' boolean.


''' with variables and function defined, will now 
words and alternate them in lowercase/uppercase using the 'flip' boolean'''
for element in string_split_up:
# First call a function to check whether this element has characters to capitalise/lowercase
# This prevents flipping for space/punctuation.
    if contains_characters(string_split_up, element) == True:
        flip = not flip

    if flip == False:
        string_in_list.append(element.upper())
    else:
        string_in_list.append(element.lower())
        # If flip is True should be False in next iteration, and vice versa, to alternate:
        
# join the modified list elements in a new string: 
string_alt_words = " ".join(string_in_list)

# display part-capitalised strings:
print(f"{string_alt_characters}")
print(f"{string_alt_words}")
# End of program - thanks for reading! 