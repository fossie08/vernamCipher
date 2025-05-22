inputtext = input('>')

inputlist = list(inputtext)
inputBinList = []

print(inputlist)

for character in inputlist:
    inputBinList.append(bin(ord(character)))

print(inputBinList)

