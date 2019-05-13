import csv
import math
import itertools
import random
import sys

import numpy
import pandas
from psychopy import visual, core, event

from kraepelin_stimuli import get_fixation_stim, get_charcue_stim_dict, KraepelinMatrixStim
from namedlist import namedlist
#parameter
BLOCK_DURATION = 60#[s]
TRIAL_MAXLENGTH = 100
BLOCK_LENGTH = 10

#----------------------------------------------------------------------------
#   
#   各セッション開始前にCueについてのサマリーを提示する
#
#
#-------------------------------------------------------------------------------

TrialStatus = namedlist(
    'TrialStatus',
    ['blocks', 'trials', 'cue_flag', 'response_time', 'response', 'correct_response', 'is_correct', 'stim_left', 'stim_right', 'trial_endtime']
)

class KraepelinWindow(visual.Window):

    KEY_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#    KEY_LIST = ['num_0', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9']

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

    def block(self, blocks):
        clock = core.Clock()
        block_start = clock.getTime()

        self.matrixstim_left.set_random_matrix(random.randint(1, 9), random.randint(1, 9))

        for trials in range(TRIAL_MAXLENGTH):
            #make trial log
            trial_status = TrialStatus()
            trial_status.blocks = blocks + 1#add 1 for log
            trial_status.trials = trials + 1#add 1 for log
            trial_status.cue_flag = next(self.cueflag_cyclic_iter)

            #display count
            self.msg_count.setText(trials)
            self.msg_count.draw()
            self.flip()
            core.wait(1.)

            #display cue
            self.LRcue_dict[trial_status.cue_flag].draw()
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
            block_time = key_start - block_start
            keys = event.waitKeys(
                maxWait=BLOCK_DURATION-block_time,
                keyList=self.KEY_LIST
            )
            if keys == None:
                break
            trial_status.response_time = clock.getTime() - key_start
            #check the answer
            trial_status.response = self.KEY_LIST.index(keys[0])
            def choose_status(status_list, flags):
                return sum([status.value if flag else status.number for status, flag in zip(status_list, flags)]) % 10
            trial_status.correct_response = choose_status([self.matrixstim_left.matrix_status, self.matrixstim_right.matrix_status], trial_status.cue_flag)
            trial_status.is_correct = trial_status.response == trial_status.correct_response

            #display after answered
            self.msg_answer.setText(trial_status.response)
            self.msg_answer.draw()
            win.flip()
            core.wait(0.2)

            #output log
            trial_status.stim_left = self.matrixstim_left.matrix.reshape(-1,)
            trial_status.stim_right = self.matrixstim_right.matrix.reshape(-1,)
            trial_status.trial_endtime = clock.getTime() - block_start
            yield trial_status
            self.matrixstim_left.copy_status(self.matrixstim_right)

            #end block if no time to response next trial
            if clock.getTime()-block_start > BLOCK_DURATION - 2.:
                break

if __name__ == "__main__":
    #set global escape
    event.globalKeys.add(key='escape', func=sys.exit)

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

    with open('result.csv', 'w') as log:
        writer = csv.writer(log)
        writer.writerow(TrialStatus._fields)
    
    for count_blocks in range(BLOCK_LENGTH):
        for output_list in win.block(count_blocks):
            with open('result.csv', 'a') as log:
                writer = csv.writer(log)
                writer.writerow(output_list)
        
    msg_finish.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
	