import collections
import random

from psychopy import visual, sound, event

from kraepelin_trigger import trigger_values
from quick20_trigger import send_trigger

SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
    'into_ten', 'start_ten', 'redo_ten', 'start_demo', 'otsukaresama'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

def practice_tenkey(kraepelin_window):
    send_trigger(trigger_values.Prac_ten_Inst)

    inst_stim = visual.TextStim(kraepelin_window, height=80)
    ans_text = visual.TextStim(kraepelin_window, height=80, pos=(0,-100))

    kraepelin_window.display_stimuli(
        [visual.TextStim(kraepelin_window, text=u'テンキー入力練習', height=80)],
        sound=sound_namedtuple.into_ten,
        wait_time=1.,
    )
    kraepelin_window.display_stimuli(
        [visual.TextStim(kraepelin_window, 'Wait...', height=80)],
        sound=sound_namedtuple.start_ten,
        wait_time=1.,
    )
    kraepelin_window.display_stimuli(
        [visual.TextStim(kraepelin_window, 'Press Enter', height=80)],
        sound=sound_namedtuple.start_demo,
        wait_time=1.,
    )
    event.waitKeys(keyList=kraepelin_window.ENTER_NAME)

    redo_flag = True
    while redo_flag:
        send_trigger(trigger_values.Prac_ten_Start)
        #reset parameter
        stim_list = sum([random.sample(range(len(kraepelin_window.NUMKEY_NAME)), k=len(kraepelin_window.NUMKEY_NAME)) for _ in range(2)], [])
        false_counter = 0

        kraepelin_window.display_stimuli(
            [visual.TextStim(kraepelin_window, 'Start!', height=80)],
            wait_time=2.,
        )
        for number in stim_list:
            inst_stim.setText(number)

            while True:
                send_trigger(trigger_values.Prac_ten_Stim)
                kraepelin_window.display_stimuli(
                    [inst_stim],
                    wait_time=0.,
                )
                keys = event.waitKeys(keyList=kraepelin_window.NUMKEY_NAME)
                answer_number = kraepelin_window.NUMKEY_NAME.index(keys[0])
                ans_text.setText(answer_number)
                send_trigger(trigger_values.Prac_ten_Resp)

                if answer_number == int(number):
                    kraepelin_window.display_stimuli(
                        [ans_text, inst_stim, visual.TextStim(kraepelin_window, '○', height=80, pos=(0,-200))],
                        wait_time=1.,
                    )
                    break
                else:
                    #try the same key
                    kraepelin_window.display_stimuli(
                        [ans_text, inst_stim, visual.TextStim(kraepelin_window, '×', height=80, pos=(0,-200))],
                        wait_time=1.,
                    )
                    false_counter += 1

        if false_counter < 4:
            redo_flag = False
        else:
            kraepelin_window.display_stimuli(
                [visual.TextStim(kraepelin_window, 'Redo', height=80)],
                sound=sound_namedtuple.redo_ten,
            )

    kraepelin_window.display_stimuli(
        [visual.TextStim(kraepelin_window, 'Finish! Press Enter', height=80)],
        sound=sound_namedtuple.otsukaresama,
    )
    event.waitKeys(keyList=kraepelin_window.ENTER_NAME)

if __name__ == "__main__":
    #set global escape
    from psychopy import core
    event.globalKeys.add(key='escape', func=core.quit)

    from kraepelin_stimuli import KraepelinWindow
    win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)

    practice_tenkey(win)