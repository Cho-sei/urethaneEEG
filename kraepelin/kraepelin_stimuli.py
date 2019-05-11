import collections
import itertools

import numpy
from psychopy import visual

from common_stimuli import MatrixStim

MATRIX_SHAPE = (3, 3)

def get_fixation_stim(win):
    thick = 2
    length = 30
    return visual.ShapeStim(
        win, vertices=(
            (-length, thick), (-thick, thick), (-thick, length),
            (thick, length), (thick, thick), (length, thick),
            (length, -thick), (thick, -thick), (thick, -length),
            (-thick, -length), (-thick, -thick), (-length, -thick)
        ),
        fillColor='white'
    )

def get_charcue_stim_dict(win):
    """return dict of TextStim
    V & N stands for Value & Number

    Args:
        win (visual.Window): window that cues belong
    """
    def get_charcue(flag):
        return "V" if flag else "N"
    return {
        flags:visual.TextStim(
            win, text=get_charcue(flags[0])+get_charcue(flags[1]), height=80, bold=True
        )
        for flags in itertools.product([True, False], repeat=2)
    }

StimStatus = collections.namedtuple('StimStatus', ['number', 'value'])

class KraepelinMatrixStim(MatrixStim):
    def __init__(self, win, interval, center_pos, **textstim_keyargs):
        super().__init__(win, MATRIX_SHAPE, interval, center_pos, **textstim_keyargs)

    def set_random_matrix(self, number, value):
        self.matrix_status = StimStatus(number, value)
        position = numpy.random.permutation(numpy.arange(MATRIX_SHAPE[0]*MATRIX_SHAPE[1])).reshape(MATRIX_SHAPE)
        self.set_matrix(numpy.where(position < number, str(value), ""))

    def copy_status(self, other):
        assert isinstance(other, self.__class__), "copy status only from the same class"
        self.matrix_status = other.matrix_status
        self.set_matrix(other.matrix)


if __name__ == "__main__":
    pass
