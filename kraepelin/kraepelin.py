import csv
import math
import itertools
import random
import sys

import numpy
import pandas
from psychopy import visual, core, event

from kraepelin_stimuli import get_fixation_stim, get_charcue_stim_dict, KraepelinMatrixStim

#parameter
TRIAL_DURATION = 60
TRIAL_LENGTH = 52
BLOCK_LENGTH = 10

#----------------------------------------------------------------------------
#   
#   各セッション開始前にCueについてのサマリーを提示する
#
#
#-------------------------------------------------------------------------------



class KraepelinWindow(visual.Window):

    KEY_LIST = ['num_0', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9']

    def __init__(self, *args, **keyargs):
        super().__init__(*args, **keyargs)
        self.msg_answer = visual.TextStim(self, pos=(0, -100), height=80, bold=True)
        self.msg_count = visual.TextStim(self, pos=(0, 0), height=80, bold=True)

        self.fixation = get_fixation_stim(self)
        self.LRcue_dict = get_charcue_stim_dict(self)

        self.matrixstim_left = KraepelinMatrixStim(self, (50, 50), (-200, 0), height=50)
        self.matrixstim_right = KraepelinMatrixStim(self, (50, 50), (200, 0), height=50)

    def block(self):
        clock = core.Clock()
        task_start = clock.getTime()

        self.matrixstim_left.set_random_matrix(random.randint(1, 9), random.randint(1, 9))

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
            cues = self.LRcue_dict[cue_flag]
            cues.draw()
            self.flip()
            core.wait(0.5)
            self.flip()
            core.wait(0.5)
            
            #display fixation cross & stimuli
            self.fixation.draw()
            self.matrixstim_right.set_random_matrix(random.randint(1, 9), random.randint(1, 9))
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

            def choose_status(status, flag):
                return status.value if flag else status.number
            cor_answer = (
                choose_status(self.matrixstim_left.matrix_status, cue_flag[0]) + choose_status(self.matrixstim_right.matrix_status, cue_flag[1])
                ) % 10

            #display after answered
            self.msg_answer.setText(answer_number)
            self.msg_answer.draw()
            win.flip()
            core.wait(0.2)

            #output log
            yield [count+1, cue_flag, rt, answer_number, cor_answer, answer_number==cor_answer, self.matrixstim_left.matrix.reshape(-1,), self.matrixstim_right.matrix.reshape(-1,)]
            self.matrixstim_left.copy_status(self.matrixstim_right)

            if clock.getTime()-task_start < 2.:
                break

if __name__ == "__main__":
    #set global escape
    event.globalKeys.add(key='escape', func=sys.exit)

    #file defined
    res_columns = ['Trials', 'Cue', 'RT', 'answer', 'cor_answer', 'is_correct', 'stim_left', 'stim_right']

    #window defined
    win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)

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
    Final_output = pandas.DataFrame(columns=['Blocks']+res_columns)
    
    for blocks in range(BLOCK_LENGTH):
        df_output = pandas.DataFrame(columns=['Blocks']+res_columns)
        for output_list in win.block():
            outputSeries = pandas.Series(output_list, index = res_columns)
            df_output = df_output.append(outputSeries, ignore_index=True)
        df_output['Blocks'] = blocks+1
        
        Final_output = pandas.concat([Final_output, df_output])

        Final_output.to_csv('result.csv', index=False)

    msg_finish.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
	