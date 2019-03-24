from psychopy import visual
import numpy

def draw_matrix(win, array2d, interval, center_pos, **textstim_keyargs):
    """
    draw a 2d-array as it seems.

    Args:
        array2d (numpy.ndarray): 
        interval (???): (x,y)
        center_pos (???): (x,y)
        textstim_keyargs (dict):
    Returns:
        None
    """

    assert array2d.ndim == 2, "Matrix should be 2d."
    #assert numpy.issubdtype(array2d.dtype, np.integer), "Matrix should be composed of integers."

    #calculate grid positions
    def axis_positions(count, interval, center):
        if count % 2 == 0: #even
            pass
        else: #odd
            pass
    x_axis = axis_positions(array2d.shape[1], interval[0], center_pos[0])
    y_axis = axis_positions(array2d.shape[0], interval[1], center_pos[1])
    grid_positions = numpy.meshgrid(x_axis, y_axis)

    #draw numbers
    for number, x, y in zip(numpy.nditer(array2d), numpy.nditer(grid_positions[0]), numpy.nditer(grid_positions[1])):
        number_stim = visual.TextStim(win, text=str(number), pos=(x, y), **textstim_keyargs)
        number_stim.draw()

