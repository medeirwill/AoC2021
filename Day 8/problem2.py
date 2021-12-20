def resolveUnambiguousCode(code, codebook):
    if (len(code) == 2):
        codebook["1"] = code
    elif (len(code) == 4):
        codebook["4"] = code
    elif (len(code) == 3):
        codebook["7"] = code
    elif (len(code) == 7):
        codebook["8"] = code
    return (code in codebook.values())

def disambiguateRemaining(ambiguousCodes, codebook):
    for code in ambiguousCodes:
        if len(code) == 6: # is 9, 6 or 0
            if codebook["4"].issubset(code):
                codebook["9"] = code
            elif codebook["1"].issubset(code):
                codebook["0"] = code 
            else:
                codebook["6"] = code 
        else: # is 2, 3 or 5
            if codebook["1"].issubset(code):
                codebook["3"] = code
            elif len(codebook["4"].intersection(code)) == 3:
                codebook["5"] = code
            else:
                codebook["2"] = code
        
with open("input.txt", "r") as clockFile: 
    outputSum = 0
    for inputLine in (line.strip() for line in clockFile):
        ambiguousCodes = list()
        numeralCodebook = dict()
        input, output = inputLine.split(" | ")
        
        for numeralCode in [frozenset(codeString) for codeString in input.split()]:
            if not resolveUnambiguousCode(numeralCode, numeralCodebook):
                ambiguousCodes.append(numeralCode)
                
        disambiguateRemaining(ambiguousCodes, numeralCodebook)
        
        numeralCodebook = {code:num for (num, code) in numeralCodebook.items()}
        outputString = str()
        
        for numeralCode in [frozenset(codeString) for codeString in output.split()]:
            outputString += numeralCodebook[numeralCode]
            
        outputSum += int(outputString)

print(outputSum)