
def boundingBoxSquare(center, size):
    x, y = center
    return (
        x-size, # x of top-right corner
        y-size,  # y of top-right corner
        x+size, # x of top-right corner
        y+size)  # y of top-right corner