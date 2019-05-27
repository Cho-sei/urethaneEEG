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

from psychopy import event, core, sound, visual

SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
    'start_2nd_session', 'ending', 'start_experiment', 'otsukaresama'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

if __name__ == "__main__":
    import sys
    logfile_name = sys.argv[1]

    event.globalKeys.add(key='escape', func=core.quit)

    from kraepelin_stimuli import KraepelinWindow
    win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)
    mouse = event.Mouse(win)
    mouse.setExclusive(True)#disable mouse

    #wait start
    visual.TextStim(win, text="Start!", height=80).draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    send_trigger(trigger_values.Experiment_Start)
#start 2nd session
    sound_namedtuple.start_2nd_session.play()
    core.wait(sound_namedtuple.start_2nd_session.getDuration())
    core.wait(2)
#questionnaire
    mouse.setExclusive(False)
    with open(logfile_name+"_questionnaire3.csv", 'x') as f:
        writer = csv.DictWriter(f, fieldnames=ratingscale_keynames)
        writer.writeheader()
        writer.writerow(fatigue_visualanalogscale(win))
        writer.writerow(karolinska_sleepinessscale(win))
        writer.writerows(odorant_questionaire(win))
    mouse.setExclusive(True)
#resting-state EEG recording
    eyesopen_restingstate_recording(win, trigger_values.Pre_Resting_EO)
    eyesclose_restingstate_recording(win, trigger_values.Pre_Resting_EC)
    subtract_result = subtractingstate_recording(win, trigger_values.Pre_Resting_Sub, SubtractThird)
    with open(logfile_name+"_subtract3.csv", 'x') as f:
        f.write(str(subtract_result))
#kraepelin experiment
    experiment_result = logfile_name+'_kraepelin_session2.csv'
    block_length = 10
    sound_namedtuple.start_experiment.play()
    core.wait(sound_namedtuple.start_experiment.getDuration())
    kraepelin_experiment(win, block_length, log_name=experiment_result)
    sound_namedtuple.otsukaresama.play()
    core.wait(sound_namedtuple.otsukaresama.getDuration())
#resting-state EEG recording
    eyesopen_restingstate_recording(win, trigger_values.Post_Resting_EO)
    eyesclose_restingstate_recording(win, trigger_values.Post_Resting_EC)
    subtract_result = subtractingstate_recording(win, trigger_values.Pre_Resting_Sub, SubtractFourth)
    with open(logfile_name+"_subtract4.csv", 'x') as f:
        f.write(str(subtract_result))
#questionnaire
    mouse.setExclusive(False)
    with open(logfile_name+"_questionnaire4.csv", 'x') as f:
        writer = csv.DictWriter(f, fieldnames=ratingscale_keynames)
        writer.writeheader()
        writer.writerow(fatigue_visualanalogscale(win))
        writer.writerow(karolinska_sleepinessscale(win))
        writer.writerows(odorant_questionaire(win))
    mouse.setExclusive(True)
#ending
    win.flip()
    sound_namedtuple.ending.play()
    core.wait(sound_namedtuple.ending.getDuration())
    core.wait(2)

#wait end
    visual.TextStim(win, text="Finish!", height=80).draw()
    win.flip()
    event.waitKeys(keyList=['space'])
