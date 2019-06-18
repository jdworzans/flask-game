import matplotlib.pyplot as plt


def substract(iterable, number=0.5):
    """Substract a number from every coordinate in iterable.

    Args:
        iterable (iterable): Iterable with pair of coordinates.
        number (float, optional): Number to substract. Defaults to 0.5.

    Returns:
        iterable (iterable): Iterable with substracted coordinates.
    """
    result = []
    for i in iterable:
        result.append([iterable[0]-number, i[1]-number])
    return result

def draw(progress, col1, col2):
    """Draw a gameboard.

    Args:
        progress (list): List of moves where.
            move (tuple): Coordinates of move.
        col1 (str): Hexadecimal value of 1st color.
        col2 (str): Hexadecimal value of 2nd color.

    Returns:
        fig (Figure): Scatterplot of progress coordinates.
    """
    coords = substract(progress)
    x, y = [], []
    for xy in coords:
        x.append(xy[0])
        y.append(xy[1])

    # Prepare figure and axis
    fig, axis = plt.subplots(1,1)
    axis.set_xlim(0,3)
    axis.set_ylim(0,3)
    axis.vlines([1,2],0,3)
    axis.hlines([1,2],0,3)
    axis.set_xticks([0.5, 1.5, 2.5])
    axis.set_xticklabels(["A", "B", "C"])
    axis.set_yticks([0.5, 1.5, 2.5])
    axis.set_yticklabels(["1", "2", "3"])
    axis.tick_params(left = False, bottom = False)

    # Plot points
    axis.scatter(x[0::2], y[0::2], s = 7000, c=col1)
    axis.scatter(x[1::2], y[1::2], s = 7000, c=col2)
    return fig
