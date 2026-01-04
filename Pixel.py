monitor = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

def activate_row(screen, row_index):
    if row_index < len(screen):      
        for i in range(len(screen[row_index])):
            screen[row_index][i] = 1
    else:
        print("Invalid row index!")

activate_row(monitor, 2)

for row in monitor:
    print(row)