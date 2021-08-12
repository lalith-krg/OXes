def win(player,grid):            
    for row in range(3):
        if(grid[row][0] == grid[row][1] == grid[row][2] == player):
            return player
    
    for column in range(3):
        if(grid[0][column] == grid[1][column] == grid[2][column] == player):
            return player

    if (grid[0][0] == grid[1][1] == grid[2][2] == player):
        return player
    if (grid[2][0] == grid[1][1] == grid[0][2] == player):
        return player

    return None
