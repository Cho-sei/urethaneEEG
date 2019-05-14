import random
import sys

from psychopy import visual, core, event

from kraepelin_stimuli import KraepelinWindow
from namedlist import namedlist
#parameter
TRIAL_MAXLENGTH = 100
BLOCK_LENGTH = 10

TrialStatus = namedlist(
    'TrialStatus',
    ['blocks', 'trials', 'cue_flag', 'response_time', 'response', 'correct_response', 'is_correct', 'stim_left', 'stim_right', 'trial_endtime']
)


def block(kraepelin_window, blocks):
    block_start = kraepelin_window.clock.getTime()

    kraepelin_window.matrixstim_left.set_random_matrix(random.randint(1, 9), random.randint(1, 9))

    for trials in range(TRIAL_MAXLENGTH):
        #make trial log
        trial_status = TrialStatus()
        trial_status.blocks = blocks + 1#add 1 for log
        trial_status.trials = trials + 1#add 1 for log
        trial_status.cue_flag = next(kraepelin_window.cueflag_cyclic_iter)

        #display count
        kraepelin_window.msg_count.setText(trials)
        kraepelin_window.msg_count.draw()
        kraepelin_window.flip()
        core.wait(1.)

        #display cue
        kraepelin_window.LRcue_dict[trial_status.cue_flag].draw()
        kraepelin_window.flip()
        core.wait(0.5)
        kraepelin_window.flip()
        core.wait(0.5)
        
        #display fixation cross & stimuli
        kraepelin_window.fixation.draw()
        kraepelin_window.matrixstim_right.set_random_matrix(random.randint(1, 9), random.randint(1, 9))
        kraepelin_window.matrixstim_left.draw()
        kraepelin_window.matrixstim_right.draw()
        win.flip()

        trial_status.response, trial_status.response_time = kraepelin_window.wait_response(block_start)
        #check the answer
        def choose_status(status_list, flags):
            return sum([status.value if flag else status.number for status, flag in zip(status_list, flags)]) % 10
        trial_status.correct_response = choose_status([kraepelin_window.matrixstim_left.matrix_status, kraepelin_window.matrixstim_right.matrix_status], trial_status.cue_flag)
        trial_status.is_correct = trial_status.response == trial_status.correct_response

        #display after answered
        kraepelin_window.msg_answer.setText(trial_status.response)
        kraepelin_window.msg_answer.draw()
        win.flip()
        core.wait(0.2)

        #output log
        trial_status.stim_left = kraepelin_window.matrixstim_left.matrix.reshape(-1,)
        trial_status.stim_right = kraepelin_window.matrixstim_right.matrix.reshape(-1,)
        trial_status.trial_endtime = kraepelin_window.clock.getTime() - block_start
        yield trial_status
        kraepelin_window.matrixstim_left.copy_status(kraepelin_window.matrixstim_right)

        #end block if no time to response next trial
        if kraepelin_window.clock.getTime()-block_start > kraepelin_window.BLOCK_DURATION - 2.:
            break

if __name__ == "__main__":
    import csv
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
        for output_list in block(win, count_blocks):
            with open('result.csv', 'a') as log:
                writer = csv.writer(log)
                writer.writerow(output_list)
        
    msg_finish.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
	