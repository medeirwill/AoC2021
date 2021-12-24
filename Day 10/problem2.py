from math import floor

pairMap = {"}": "{", ")": "(", "]" : "[", ">": "<"}
openers = set(pairMap.values())
failMap = {")": 3, "]" : 57, "}" : 1197, ">" : 25137}
completionMap = {"(" : 1, "[" : 2, "{" : 3, "<" : 4}
inputLines = list()
failScore = 0
completeScores = list()

with open("input.txt", "r") as chunkFile: 
   navLines = [rawline.strip() for rawline in chunkFile] 
        
for navString in navLines:
    openerStack = list()
    for char in navString:
        if char in openers:
            openerStack.append(char)
        else:
            if pairMap[char] == openerStack[-1]:
                openerStack.pop()
            else:
                failScore += failMap[char]
                openerStack = list()
                break
    completeScore = 0
    for charNeedsClosing in reversed(openerStack):
        completeScore = completeScore * 5 + completionMap[charNeedsClosing]
    if completeScore > 0:
        completeScores.append(completeScore)
    
completeScores.sort()

    

        
print("Syntax score is " + str(failScore) + "\n")
print("Completion score is " + str(completeScores[int(len(completeScores)/2)]))      