# Save original sentence in variable:
fox_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# Replace "!" with spaces, then replace " ." with ".", then assign to variable
fox_replace = (fox_string.replace("!", " ")).replace(" .", ".")
# Reprint sentence: 
print(fox_replace)

# Display fox_replace in uppercase: 
print(fox_replace.upper())

# Print original sentence in reverse:
print(fox_string[::-1])