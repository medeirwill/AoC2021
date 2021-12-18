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

for call in bingoCalls:
    everyCardWon = False
    for boardNumber, board in enumerate(bingoCards):
        if len(bingoWinners) == len(bingoCards):
            everyCardWon = True
        try:
            if not board.isWinner:
                board.marker(call)
        except Exception:
            bingoWinners.append(board)
    if everyCardWon:
        break

print("Hit on " + call + " and unmarked total is " +
      str(bingoWinners[-1].unmarkedTotal))
