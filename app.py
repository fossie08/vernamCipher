#converts the list of charatcers to a list of ascii binary
def convListtoBin(inputList):
    binarylist = []
    for character in inputList:
        binarylist.append(bin(ord(character)))
    return binarylist

inputtext = input('input cipher text>')

print(convListtoBin(list(inputtext)))

inputOneTimePad = input('input one time pad>')

print(convListtoBin(list(inputOneTimePad)))
