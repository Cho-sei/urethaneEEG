import collections
import functools

import numpy
from psychopy import visual

MATRIX_SHAPE = (3, 3)

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
            textstim.setText(str(text))

    def draw(self):
        """draw matrix
        """
        for textstim in self.textstim_list:
            textstim.draw()

class KraepelinWindow(visual.Window):
    def __init__(self, *args, **keyargs):
        super().__init__(*args, **keyargs)

        self.msg_answer = visual.TextStim(self, pos=(0, -100), height=80, bold=True)
        self.msg_count = visual.TextStim(self, pos=(0, 0), height=80, bold=True)

        self.fixation = visual.ShapeStim(
            win, vertices=((-30, 0), (30, 0), (0, 0), (0, -30), (0, 30), (0, 0))
        )

        self.matrixstim_left = MatrixStim(self, MATRIX_SHAPE, (50, 50), (-200, 0), height=50)
        self.matrixstim_right = MatrixStim(self, MATRIX_SHAPE, (50, 50), (200, 0), height=50)

    def draw_count(self, count):
        self.msg_count.setText(count)
        self.msg_count.draw()
    
    def draw_answer(self, answer):
        self.msg_answer.setText(answer)
        self.msg_answer.draw()

    def draw_fixation(self):
        self.fixation.draw()

    def draw_matrices(self, matrix_left, matrix_right):
        self.matrixstim_left.set_matrix(matrix_left)
        self.matrixstim_right.set_matrix(matrix_right)
        self.matrix_left.draw()
        self.matrix_right.draw()

if __name__ == "__main__":
    pass
