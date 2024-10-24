# Shyla Nguyen
# COP 3502C
# Lab 6: Version Control
# 10/22/2024


# Encodes a string of all digits by shifting each digit up by 3 numbers.
def encode(password):
    encoded_pass = ""
    for digit in password:
        digit = int(digit)
        digit = (digit + 3) % 10
        encoded_pass += str(digit)
    return encoded_pass

def decode(encoded_pass):
	decoded = ""
	for digit in encoded_pass:
		decoded += str((int(digit) - 3) % 10)
	return decoded

if __name__ == '__main__':
    option = -1
    password = None
    while True:
        # Prints the menu
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option = int(input('Please enter an option: '))

        # Reads password and encodes.
        if option == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!')
            print()

        # Decodes and prints both passwords (encoded & decoded).
        elif option == 2:
		decoded = decode(password)
		print(f"The encoded password is {password}, and the original password is {decoded}")
		print()

        # Exits the program
        elif option == 3:
            break
