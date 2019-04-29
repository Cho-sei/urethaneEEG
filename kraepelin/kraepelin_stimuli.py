import functools

import numpy
from psychopy import visual

def get_fixation_stim(win):
    return visual.ShapeStim(
        win, vertices=((-30, 0), (30, 0), (0, 0), (0, -30), (0, 30), (0, 0))
    )

def get_que_stim(win):
    return visual.Circle(
        win, radius=1, edges=64, pos=(0, -60)
    )

class MatrixStim:
    """draw a matrix using visual.TextStim as it seems.

    Attributes:
        textstim_list (list): contains position & other options of each element as visual.TextStim.
    """
    def __init__(self, win, matrix_shape, interval, center_pos, **textstim_keyargs):
        """
        Args:
            win (visual.Window):
            matrix_shape (tuple): should be tuple of ints
            interval (tuple): (interval_x, interval_y)
            center_pos (tuple): (center_x, center_y)
            textstim_keyargs (dict):
        """

        def axis_positions(count, interval, center):
            base = numpy.arange((count+1) // 2)
            if count % 2 == 0: #even
                points = interval/2 + interval*base
                return numpy.concatenate(
                    [-points[::-1]+center, points+center]
                    )
            else: #odd
                points = interval*base
                return numpy.concatenate(
                    [-points[::-1]+center, points[1:]+center]
                    )

        x_axis = axis_positions(matrix_shape[1], interval[0], center_pos[0])
        y_axis = axis_positions(matrix_shape[0], interval[1], center_pos[1])
        grid_positions = numpy.meshgrid(x_axis, y_axis)

        self.textstim_list = [
            visual.TextStim(win, pos = (x, y), **textstim_keyargs)
            for x, y in zip(numpy.nditer(grid_positions[0]), numpy.nditer(grid_positions[1]))
        ]

    def set_matrix(self, matrix):
        """set each element in matrix to corresponding ones.

        Args:
            matrix (iterable): 
        """
        for textstim, text in zip(self.textstim_list, numpy.nditer(matrix)):
            textstim.setText(text)

    def draw(self):
        """draw matrix
        """
        for textstim in self.textstim_list:
            textstim.draw()

if __name__ == "__main__":
    pass
