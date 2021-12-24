pairMap = {"}": "{", ")": "(", "]" : "[", ">": "<"}
openers = set(pairMap.values())
failMap = {")": 3, "]" : 57, "}" : 1197, ">" : 25137}

inputLines = list()
score = 0

with open("input.txt", "r") as chunkFile: 
   navLines = [rawline.strip() for rawline in chunkFile] 
        
for navString in navLines: #Need to implement the hot seat as a stack: if valid closer, pop, else fail and increment score
    openerStack = list()
    for char in navString:
        if char in openers:
            openerStack.append(char)
        else:
            if pairMap[char] == openerStack[-1]:
                openerStack.pop()
            else:
                score += failMap[char]
                break
        
print(score)      