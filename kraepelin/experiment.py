import csv
import collections

from kraepelin import kraepelin_experiment
from kraepelin_demo import instruction, demo, display_confirmation
from resting_state import eyesopen_restingstate_recording, eyesclose_restingstate_recording, subtractingstate_recording
from questionnaire import ratingscale_keynames, fatigue_visualanalogscale, karolinska_sleepinessscale, odorant_questionaire
from practice_tenkey import practice_tenkey
from kraepelin_trigger import trigger_values
from quick20_trigger import send_trigger

SubtractFirst = 0
SubtractSecond = 1
SubtractThird = 2
SubtractFourth = 3

from psychopy import event, core, sound

SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
    'opening', 'end_1st_session', 'alert_mouse', 'start_experiment', 'otsukaresama'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

if __name__ == "__main__":
    import sys
    logfile_name = sys.argv[1]

    event.globalKeys.add(key='escape', func=sys.exit)

    from kraepelin_stimuli import KraepelinWindow
    win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)

    send_trigger(trigger_values.Experiment_Start)
#opening
    sound_namedtuple.opening.play()
    core.wait(sound_namedtuple.opening.getDuration())
    core.wait(1)
    sound_namedtuple.alert_mouse.play()
    core.wait(sound_namedtuple.alert_mouse.getDuration())
    core.wait(2)
#questionnaire
    win.setMouseVisible(True)
    with open(logfile_name+"_questionnaire1.csv", 'x') as f:
        writer = csv.DictWriter(f, fieldnames=ratingscale_keynames)
        writer.writeheader()
        writer.writerow(fatigue_visualanalogscale(win))
        writer.writerow(karolinska_sleepinessscale(win))
        writer.writerows(odorant_questionaire(win))
    win.setMouseVisible(False)
#resting-state EEG recording
    eyesopen_restingstate_recording(win, trigger_values.Pre_Resting_EO)
    eyesclose_restingstate_recording(win, trigger_values.Pre_Resting_EC)
    subtract_result = subtractingstate_recording(win, trigger_values.Pre_Resting_Sub, SubtractFirst)
    with open(logfile_name+"_subtract1.csv", 'x') as f:
        f.write(str(subtract_result))
#practice 10-key
    practice_tenkey(win)
#instruction & demonstration
    block_length_demo = 2
    demo_trial = 1#for log.csv name
    instruction(win)
    demo_result = logfile_name+'_kraepelindemo{}.csv'.format(demo_trial)
    demo(win, block_length_demo, log_name=demo_result)
    while True:
        selection = display_confirmation(win)
        if selection == 0:
            instruction(win)
        elif selection == 1:
            demo_trial = demo_trial + 1
            demo_result = logfile_name+'_kraepelindemo{}.csv'.format(demo_trial)
            demo(win, block_length_demo, log_name=demo_result)
        else:
            break
#kraepelin experiment
    experiment_result = logfile_name+'_kraepelin_session1.csv'
    block_length = 10
    sound_namedtuple.start_experiment.play()
    core.wait(sound_namedtuple.start_experiment.getDuration())
    kraepelin_experiment(win, block_length, log_name=experiment_result)
    sound_namedtuple.otsukaresama.play()
    core.wait(sound_namedtuple.otsukaresama.getDuration())
#resting-state EEG recording
    eyesopen_restingstate_recording(win, trigger_values.Post_Resting_EO)
    eyesclose_restingstate_recording(win, trigger_values.Post_Resting_EC)
    subtract_result = subtractingstate_recording(win, trigger_values.Pre_Resting_Sub, SubtractFirst)
    with open(logfile_name+"_subtract2.csv", 'x') as f:
        f.write(str(subtract_result))
#questionnaire
    win.setMouseVisible(True)
    with open(logfile_name+"_questionnaire2.csv", 'x') as f:
        writer = csv.DictWriter(f, fieldnames=ratingscale_keynames)
        writer.writeheader()
        writer.writerow(fatigue_visualanalogscale(win))
        writer.writerow(karolinska_sleepinessscale(win))
        writer.writerows(odorant_questionaire(win))
    win.setMouseVisible(False)
#ending of 1st session
    win.flip()
    end_1st_session.play()
    core.wait(end_1st_session.getDuration())