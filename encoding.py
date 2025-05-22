def convListtoBin(inputList):
    return [format(ord(c), '08b') for c in inputList]

inputtext = input('input cipher text> ')
inputOneTimePad = input('input one time pad> ')

if len(inputOneTimePad) < len(inputtext):
    print("Error: One time pad must be at least as long as the input text.")
    exit()

binaryListText = convListtoBin(list(inputtext))
oneTimePadListText = convListtoBin(list(inputOneTimePad))

encodedList = []
for i in range(len(binaryListText)):
    # XOR the integer values of the characters
    xor_result = ord(inputtext[i]) ^ ord(inputOneTimePad[i])
    encodedList.append(format(xor_result, '08b'))

print("Encoded binary list:", encodedList)

# To get the encoded text (ciphertext)
ciphertext = ''.join([chr(int(b, 2)) for b in encodedList])
print("Ciphertext:", ciphertext)
