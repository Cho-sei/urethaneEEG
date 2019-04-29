import collections
import csv
import math
import itertools
import random
import sys

import numpy
from psychopy import visual, core, event

from kraepelin_stimuli import get_fixation_stim, get_Lcue_stim, get_Rcue_stim, MatrixStim

#parameter
TRIAL_DURATION = 60
TRIAL_LENGTH = 4
BLOCK_LENGTH = 50
MATRIX_SHAPE = (3, 3)

def generate_matrix(counts_of_number, number):
    position = numpy.random.permutation(numpy.arange(MATRIX_SHAPE[0]*MATRIX_SHAPE[1])).reshape(MATRIX_SHAPE)
    return numpy.where(position < counts_of_number, str(number), "")

StimStatus = collections.namedtuple('StimStatus', ['articles_of_number', 'number'])

class KraepelinWindow(visual.Window):

    KEY_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self, *args, **keyargs):
        super().__init__(*args, **keyargs)
        self.msg_answer = visual.TextStim(self, pos=(0, -100), height=80, bold=True)
        self.msg_count = visual.TextStim(self, pos=(0, 0), height=80, bold=True)

        self.fixation = get_fixation_stim(self)
        self.LRcue = [get_Lcue_stim(self), get_Rcue_stim(self)]

        self.matrixstim_left = MatrixStim(self, MATRIX_SHAPE, (50, 50), (-200, 0), height=50)
        self.matrixstim_right = MatrixStim(self, MATRIX_SHAPE, (50, 50), (200, 0), height=50)

    def block(self):
        pre_status = StimStatus(random.randint(1, 9), random.randint(1, 9))
        pre_stimulus = generate_matrix(*pre_status)

        clock = core.Clock()
        task_start = clock.getTime()

        self.correct = 0

        assert TRIAL_LENGTH%4 == 0, "TRIAL_LENGTH should be multiple of 4"
        cueflag_list = [(False, False)]*(TRIAL_LENGTH//4) + [(False, True)]*(TRIAL_LENGTH//4) + [(True, False)]*(TRIAL_LENGTH//4) + [(True, True)]*(TRIAL_LENGTH//4)
        random.shuffle(cueflag_list)

        for count, cue_flag in enumerate(cueflag_list):
            #display count
            self.msg_count.setText(count)
            self.msg_count.draw()
            self.flip()
            core.wait(1.)

            #display cue
            for cue, flag in zip(self.LRcue, cue_flag):
                if flag:
                    cue.draw()
            self.flip()
            core.wait(0.5)
            self.flip()
            core.wait(0.5)
            
            #display fixation cross & stimuli
            self.fixation.draw()
            new_status = StimStatus(random.randint(1, 9), random.randint(1, 9))
            new_stimulus = generate_matrix(*new_status)
            self.matrixstim_left.set_matrix(pre_stimulus)
            self.matrixstim_right.set_matrix(new_stimulus)
            self.matrixstim_left.draw()
            self.matrixstim_right.draw()
            win.flip()

            #enter keys and measure response time
            key_start = clock.getTime()
            task_time = key_start - task_start
            keys = event.waitKeys(
                maxWait=TRIAL_DURATION-task_time,
                keyList=self.KEY_LIST
            )
            if keys == None:
                break
            
            key_end = clock.getTime()
            rt = key_end - key_start
            #check the answer
            answer_number = self.KEY_LIST.index(keys[0])

            cor_answer = (pre_number[1 if cue_flag[0] else 0] + new_number[1 if cue_flag[1] else 0]) % 10
            if answer_number == cor_answer:
                self.correct += 1

            pre_status = new_status
            pre_stimulus = new_stimulus

            #display after answered
            self.msg_answer.setText(answer_number)
            self.msg_answer.draw()
            win.flip()

            core.wait(0.2)
            yield rt

if __name__ == "__main__":
    #set global escape
    event.globalKeys.add(key='escape', func=sys.exit)

    #file defined
    res_columns = ['trials', 'all', 'accuracy', 'RT']

    with open('result.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(res_columns)

    #window defined
    win = KraepelinWindow(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

    #visual text
    msg_wait = visual.TextStim(win, text='Wait...', height=80, bold=True)
    msg_start = visual.TextStim(win, text='Start!', height=80, bold=True)
    msg_finish = visual.TextStim(win, text='Finish!', height=80, bold=True)

    msg_wait.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    msg_start.draw()
    win.flip()

    core.wait(2)

    for blocks in range(BLOCK_LENGTH):
        rt_list = [i for i in win.block()]
      
        with open('result.csv', 'a') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(
                [blocks+1, len(rt_list), win.correct/len(rt_list) if len(rt_list)>0 else 0] + rt_list
            )

    msg_finish.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
	