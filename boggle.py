def make_grid(width, height):
    """
    Make a grid that holds the correct number of boggle tiles for a boggle game
    """
    return {(row, col): ' ' for row in range(height)
        for col in range(width)}