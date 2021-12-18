from problem_1 import crunchDepths

with open("input.txt", "r") as depths_file:
    depths_list = [int(line) for line in depths_file.read().splitlines()]
windowCount = len(depths_list) - 2

windowFilename = "windows.txt"
with open(windowFilename, "w") as windows_file:
    for i in range(windowCount):
        windows_file.write(
            str(depths_list[i] + depths_list[i+1] + depths_list[i+2])
            )
        windows_file.write("\n")
crunchDepths(windowFilename)
