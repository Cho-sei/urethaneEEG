from kraepelin import kraepelin_experiment
from kraepelin_demo import instruction, demo, display_confirmation
from resting_state import eyesopen_restingstate_recording, subtractingstate_recording

if __name__ == "__main__":
    import sys
    logfile_name = sys.argv[1]

    from psychopy import event
    event.globalKeys.add(key='escape', func=sys.exit)

    from kraepelin_stimuli import KraepelinWindow
    win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)

#questionnaire

#resting-state EEG recording

#practice 10-key

#instruction & demonstration
    block_length_demo = 2
    demo_trial = 1#for log.csv name
    instruction(win)
    demo(win, block_length_demo)
    display_confirmation(win)
    while True:
        key = event.waitKeys(keyList=['1','2','3'])
        if  '1' in key:
            instruction(win)
        elif '2' in key:
            demo_trial = demo_trial + 1
            demo_result = logfile_name+'_demo{}.csv'.format(demo_trial)
            demo(win, block_length_demo, log_name=demo_result)
        else:
            break
        display_confirmation(win)
#kraepelin experiment
    experiment_result = logfile_name+'_result.csv'
    block_length = 10
    kraepelin_experiment(win, block_length, log_name=experiment_result)
#resting-state EEG recording
    eyesopen_restingstate_recording(win)
    subtractingstate_recording(win)
#questionnaire

