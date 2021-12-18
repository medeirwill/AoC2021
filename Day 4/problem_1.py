from bingo_board import BingoBoard

bingoCalls = list()
bingoCards = list()

with open("input.txt", "r") as bingo_file:
    while line := bingo_file.readline().strip():
        bingoCalls += line.split(",")

    cardArray = []
    for line in bingo_file:
        if line.strip():
            cardArray.append(line.strip())
        else:
            bingoCards.append(BingoBoard(cardArray))
            cardArray = []
    bingoCards.append(BingoBoard(cardArray))  # Get the last board
    bingoWinners = []
try:
    for call in bingoCalls:
        for boardNumber, board in enumerate(bingoCards):
            board.marker(call)
except Exception as winnerExcept:
    print(str(winnerExcept))
