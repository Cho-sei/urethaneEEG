from psychopy import visual
import numpy

class MatrixStim:
    def __init__(self, win, matrix_shape, interval, center_pos, **textstim_keyargs):

        def axis_positions(count, interval, center):
            base = numpy.arange((count+1) // 2)
            if count % 2 == 0: #even
                points = interval/2 + interval*base + center
                return numpy.concatenate([points[::-1], points])
            else: #odd
                points = interval*base + center
                return numpy.concatenate([points[::-1], points[1:]])

        x_axis = axis_positions(matrix_shape[1], interval[0], center_pos[0])
        y_axis = axis_positions(matrix_shape[0], interval[1], center_pos[1])
        grid_positions = numpy.meshgrid(x_axis, y_axis)

        self.textstim_list = [
            visual.TextStim(win, pos = (x, y), **textstim_keyargs)
            for x, y in zip(numpy.nditer(grid_positions[0]), numpy.nditer(grid_positions[1]))
        ]

    def set_matrix(self, matrix):
        print(len(self.textstim_list), matrix.shape)
        for textstim, text in zip(self.textstim_list, numpy.nditer(matrix)):
            textstim.setText(text)
            textstim.draw()