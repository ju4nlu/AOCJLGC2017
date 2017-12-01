import sys

# Checking the input is right
if len(sys.argv) != 2:
    print("A parameter specifying the .txt directory is required!")
    sys.exit()

# Getting that file openned
with open(sys.argv[1], 'r') as f:
    input_captcha = f.read()
f.closed

################# FIRST PART #################

# Needed variables to keep track
previous_digit = 0
counter = 0

# Main loop. Just checks if the current digit is equal to the previous one
# if this is true, then the digit is added to the counter
for digit in input_captcha:
    if digit.isdigit():
        if digit==previous_digit:
            counter += int(digit)
        previous_digit = digit

# As the list is circular, we must check the first against the last element
if input_captcha[0] == previous_digit:
    counter += int(input_captcha[0])
       
print ("The solution to the FIRST captcha is:\t{}".format(counter))

################# SECOND PART #################

# Now we also need the distance between elements
next_digit = 0
counter = 0
d = len(input_captcha)/2

# As we need to check the elements at distance d of each one, we need
# to know if we are in the lower or in the upper part of the sequence
for i, digit in enumerate(input_captcha):
    if i<d:
        next_digit = input_captcha[i+d]
    else:
        next_digit = input_captcha[i-d]
    
    if digit == next_digit:
        counter += int(digit)
        
print ("The solution to the SECOND captcha is:\t{}".format(counter))
