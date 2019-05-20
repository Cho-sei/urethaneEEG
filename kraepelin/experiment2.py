import csv

from kraepelin import kraepelin_experiment
from kraepelin_demo import instruction, demo, display_confirmation
from resting_state import eyesopen_restingstate_recording, eyesclose_restingstate_recording, subtractingstate_recording
from questionnaire import ratingscale_keynames, fatigue_visualanalogscale, karolinska_sleepinessscale
from practice_tenkey import practice_tenkey
from kraepelin_trigger import trigger_values
from quick20_trigger import send_trigger

from psychopy import event, sound, core

SubtractFirst = 0
SubtractSecond = 1
SubtractThird = 2
SubtractFourth = 3

start_2nd_session = sound.Sound('sounds/start_2nd_session.wav')
ending = sound.Sound('sounds/ending.wav')

if __name__ == "__main__":
    import sys
    logfile_name = sys.argv[1]

    event.globalKeys.add(key='escape', func=sys.exit)

    from kraepelin_stimuli import KraepelinWindow
    win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)

    send_trigger(trigger_values.Experiment_Start)
#start 2nd session
    start_2nd_session.play()
    core.wait(start_2nd_session.getDuration())
    core.wait(2)
#questionnaire
    win.setMouseVisible(True)
    with open(logfile_name+"_questionnaire3.csv", 'w') as f:
        writer = csv.DictWriter(f, fieldnames=ratingscale_keynames)
        writer.writeheader()
        writer.writerow(fatigue_visualanalogscale(win))
        writer.writerow(karolinska_sleepinessscale(win))
    win.setMouseVisible(False)
#resting-state EEG recording
    eyesopen_restingstate_recording(win, trigger_values.Pre_Resting_EO)
    eyesclose_restingstate_recording(win, trigger_values.Pre_Resting_EC)
    subtractingstate_recording(win, trigger_values.Pre_Resting_Sub, SubtractThird)
#practice 10-key
    #practice_tenkey(win)
#instruction & demonstration
#    block_length_demo = 2
#    demo_trial = 1#for log.csv name
#    instruction(win)
#    demo_result = logfile_name+'_kraepelindemo{}.csv'.format(demo_trial)
#    demo(win, block_length_demo, log_name=demo_result)
#    display_confirmation(win)
#    while True:
#        key = event.waitKeys(keyList=['num_1','num_2','num_3'])
#        if  '1' in key:
#            instruction(win)
#        elif '2' in key:
#            demo_trial = demo_trial + 1
#            demo_result = logfile_name+'_kraepelindemo{}.csv'.format(demo_trial)
#            demo(win, block_length_demo, log_name=demo_result)
#        else:
#            break
#        display_confirmation(win)
#kraepelin experiment
    experiment_result = logfile_name+'_kraepelin_session2.csv'
    block_length = 10
    kraepelin_experiment(win, block_length, log_name=experiment_result)
#resting-state EEG recording
    eyesopen_restingstate_recording(win, trigger_values.Post_Resting_EO)
    eyesclose_restingstate_recording(win, trigger_values.Post_Resting_EC)
    subtractingstate_recording(win, trigger_values.Post_Resting_Sub, SubtractFourth)
#questionnaire
    win.setMouseVisible(True)
    with open(logfile_name+"_questionnaire4.csv", 'w') as f:
        writer = csv.DictWriter(f, fieldnames=ratingscale_keynames)
        writer.writeheader()
        writer.writerow(fatigue_visualanalogscale(win))
        writer.writerow(karolinska_sleepinessscale(win))
    win.setMouseVisible(False)
#ending
    win.flip()
    ending.play()
    core.wait(ending.getDuration())