
import sys

if len(sys.argv) != 2:
    print("A parameter specifying the .txt directory is required!")
    sys.exit()

with open(sys.argv[1], 'r') as f:
    input_captcha = f.read()
f.closed

#input_captcha = "123341"

previous_digit = 0
counter = 0

for digit in input_captcha:
    if digit.isdigit():
        if digit==previous_digit:
            counter += int(digit)
        previous_digit = digit

if input_captcha[0] == previous_digit:
    counter += int(input_captcha[0])
    
        
print ("The solution to the captcha is... {}".format(counter))