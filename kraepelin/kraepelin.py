import collections
import csv
import math
import itertools
import random
import sys

import numpy
import pandas
from psychopy import visual, core, event

from kraepelin_stimuli import get_fixation_stim, get_cue_stim, MatrixStim

#parameter
TRIAL_DURATION = 60
TRIAL_LENGTH = 50
BLOCK_LENGTH = 10
MATRIX_SHAPE = (3, 3)

def generate_matrix(counts_of_number, number):
    position = numpy.random.permutation(numpy.arange(MATRIX_SHAPE[0]*MATRIX_SHAPE[1])).reshape(MATRIX_SHAPE)
    return numpy.where(position < counts_of_number, str(number), "")

StimStatus = collections.namedtuple('StimStatus', ['articles_of_number', 'number'])

class KraepelinWindow(visual.Window):

#    KEY_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    KEY_LIST = ['num_0', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9']

    def __init__(self, *args, **keyargs):
        super().__init__(*args, **keyargs)
        self.msg_answer = visual.TextStim(self, pos=(0, -100), height=80, bold=True)
        self.msg_count = visual.TextStim(self, pos=(0, 0), height=80, bold=True)

        self.fixation = get_fixation_stim(self)
        self.cue = get_cue_stim(self)

        self.matrixstim_left = MatrixStim(self, MATRIX_SHAPE, (50, 50), (-200, 0), height=50)
        self.matrixstim_right = MatrixStim(self, MATRIX_SHAPE, (50, 50), (200, 0), height=50)

    def block(self):
        pre_status = StimStatus(random.randint(1, 9), random.randint(1, 9))
        pre_stimulus = generate_matrix(*pre_status)

        clock = core.Clock()
        task_start = clock.getTime()

        self.correct = 0
        cueflag_list = [True]*(TRIAL_LENGTH//2) + [False]*(TRIAL_LENGTH-TRIAL_LENGTH//2)
        random.shuffle(cueflag_list)

        for count, cue_flag in enumerate(cueflag_list):
            #display count
            self.msg_count.setText(count)
            self.msg_count.draw()
            self.flip()
            core.wait(1.)

            #display cue
            if cue_flag:
                self.cue.draw()
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
            if cue_flag:
                cor_answer = (pre_status.number + new_status.number) % 10
            else:
                cor_answer = (pre_status.articles_of_number + new_status.articles_of_number) % 10
            if answer_number == cor_answer:
                self.correct += 1

            #display after answered
            self.msg_answer.setText(answer_number)
            self.msg_answer.draw()
            win.flip()

            #output list
            yield [count+1, answer_number, rt, cue_flag, cor_answer, pre_stimulus.reshape(-1,), new_stimulus.reshape(-1,)]

            pre_status = new_status
            pre_stimulus = new_stimulus
           
            core.wait(0.2)

if __name__ == "__main__":
    #set global escape
    event.globalKeys.add(key='escape', func=sys.exit)

    #file defined
    res_columns = ['Trials', 'answer', 'RT', 'Cue', 'cor_answer', 'stim_left', 'stim_right']

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

    #output dataframe
    Final_output = pandas.DataFrame(columns = ['Blocks'] + res_columns)
    
    for blocks in range(BLOCK_LENGTH):
        df_output = pandas.DataFrame(columns = ['Blocks'] + res_columns)
        for output_list in win.block():
            outputSeries = pandas.Series(output_list, index = res_columns)
            df_output = df_output.append(outputSeries, ignore_index=True)
        df_output['Blocks'] = blocks+1
        
        Final_output = pandas.concat([Final_output, df_output])

        Final_output.to_csv('result.csv', index=False)

    msg_finish.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
	