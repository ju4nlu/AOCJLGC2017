import sys

# Checking the input is right
if len(sys.argv) != 2:
    print("A parameter specifying the .txt directory is required!")
    sys.exit()

# Getting that file openned
with open(sys.argv[1], 'r') as f:
    input_captcha = f.read()
f.closed

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
       
print ("The solution to the captcha is... {}".format(counter))
