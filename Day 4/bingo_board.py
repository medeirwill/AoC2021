class BingoBoard:
    def __init__(self, rowsArray):
        self.boardRows = list()
        self.hitDict = dict()
        self.rowHits = [0]*5
        self.columnHits = [0]*5
        self.unmarkedTotal = 0
        self.isWinner = False
        for string in rowsArray:
            self.boardRows.append(string.split())
        for rowIndex, row in enumerate(self.boardRows):
            # Could improve this by iterating over the characters in the string
            # as it's added rather than like this
            for columnIndex, number in enumerate(row):
                self.hitDict[self.boardRows[rowIndex][columnIndex]] = (
                    rowIndex,
                    columnIndex
                )
                self.unmarkedTotal += int(number)
                self.originalTotal = self.unmarkedTotal

    def marker(self, calledNumber: str):
        if hitCoordinates := self.hitDict.get(calledNumber, False):
            row = hitCoordinates[0]
            column = hitCoordinates[1]
            self.unmarkedTotal -= int(calledNumber)
            self.rowHits[row] += 1
            self.columnHits[column] += 1
            if self.rowHits[row] == 5 or self.columnHits[column] == 5:
                self.isWinner = True
                raise Exception("Unmarked total: "
                                + str(self.unmarkedTotal)
                                + "\nHit on: " + calledNumber)
