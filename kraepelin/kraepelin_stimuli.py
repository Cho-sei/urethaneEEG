import collections
import itertools
import random

import numpy
from psychopy import core, visual, event

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

class KraepelinWindow(visual.Window):

    KEY_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#    KEY_LIST = ['num_0', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9']
    BLOCK_DURATION = 60#[s]

    def __init__(self, *args, **keyargs):
        super().__init__(*args, **keyargs)
        self.msg_answer = visual.TextStim(self, pos=(0, -100), height=80, bold=True)
        self.msg_count = visual.TextStim(self, pos=(0, 0), height=80, bold=True)

        self.fixation = get_fixation_stim(self)
        self.LRcue_dict = get_charcue_stim_dict(self)

        self.matrixstim_left = KraepelinMatrixStim(self, (50, 50), (-200, 0), height=50)
        self.matrixstim_right = KraepelinMatrixStim(self, (50, 50), (200, 0), height=50)

        cue_list = list(itertools.product((True, False), repeat=2))
        self.cueflag_cyclic_iter = itertools.cycle(sum([random.sample(cue_list, k=len(cue_list)) for _ in range(100)],[]))

        self.clock = core.Clock()

    def display_stimuli(self, stimulus_list, sound=None, wait_time=0.):
        if sound:
            sound.play()
            sound_wait = sound.duration
        else:
            sound_wait = 0

        for stimulus in stimulus_list:
            stimulus.draw()
        self.flip()
        core.wait(wait_time + sound_wait)

    def wait_response(self, block_start):
        """wait keys & measure the response time
        """
        key_start = self.clock.getTime()
        block_time = key_start - block_start
        keys = event.waitKeys(
            maxWait=self.BLOCK_DURATION-block_time,
            keyList=self.KEY_LIST
        )
        if keys == None:
            return None
        return self.KEY_LIST.index(keys[0]), self.clock.getTime() - key_start

if __name__ == "__main__":
    pass
