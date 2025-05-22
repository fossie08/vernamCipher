def convListtoBin(inputList):
    return [format(ord(c), '08b') for c in inputList]

ciphertext = input('input ciphertext> ')
inputOneTimePad = input('input one time pad> ')

if len(inputOneTimePad) < len(ciphertext):
    print("Error: One time pad must be at least as long as the ciphertext.")
    exit()

decoded_chars = []
for i in range(len(ciphertext)):
    xor_result = ord(ciphertext[i]) ^ ord(inputOneTimePad[i])
    decoded_chars.append(chr(xor_result))

decoded_text = ''.join(decoded_chars)
print("Decoded text:", decoded_text)
