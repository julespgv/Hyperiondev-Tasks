# Declare Variables:
counter = 0
num = 0
total = 0

# Loop until user enters "-1" 
while num != -1:
    num = int(input("Please enter a number: "))
    if num == -1:
        break # exit loop if the input is -1.
    else:
        # For calculating (mean) average:
        counter += 1 # count of numbers entered, excluding the -1
        total += num # sum total of entered numbers, excluding -1

# Assign mean average of numbers to string:
average = str(total/counter)

# Display average to user:
print(f"Average = {total}/{counter} = {average}")