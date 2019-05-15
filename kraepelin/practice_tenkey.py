import collections
import random

from psychopy import visual, sound, event

SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
    'into_ten', 'start_ten', 'redo_ten', 'start_demo', 'finish_demo'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

def practice_tenkey(kraepelin_window):
    inst_stim = visual.TextStim(kraepelin_window, height=80)
    ans_text = visual.TextStim(kraepelin_window, height=80, pos=(0,-100))

    kraepelin_window.display_stimuli(
        [visual.TextStim(win, text=u'テンキー入力練習', height=80)],
        sound=sound_namedtuple.into_ten,
    )
    kraepelin_window.display_stimuli(
        [visual.TextStim(win, 'Wait...', height=80)],
        sound=sound_namedtuple.start_ten,
    )
    kraepelin_window.display_stimuli(
        [visual.TextStim(win, 'Wait...', height=80)],
        sound=sound_namedtuple.start_demo,
    )

    redo_flag = True
    while redo_flag:
        #reset parameter
        stim_list = sum([random.sample(kraepelin_window.KEY_LIST, k=len(kraepelin_window.KEY_LIST)) for _ in range(2)], [])
        false_counter = 0

        kraepelin_window.display_stimuli(
            [visual.TextStim(win, 'Start!', height=80)],
            wait_time=2.,
        )
        for number in stim_list:
            inst_stim.setText(number)

            while True:
                kraepelin_window.display_stimuli(
                    [inst_stim],
                    wait_time=0.,
                )
                keys = event.waitKeys(keyList=kraepelin_window.KEY_LIST)
                answer_number = kraepelin_window.KEY_LIST.index(keys[0])
                ans_text.setText(answer_number)

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
                [visual.TextStim(win, 'Redo', height=80)],
                sound=sound_namedtuple.redo_ten,
            )

    kraepelin_window.display_stimuli(
        [visual.TextStim(win, 'Finish! Press Enter', height=80)],
        sound=sound_namedtuple.finish_demo,
    )
    event.waitKeys(keyList=['num_enter'])

if __name__ == "__main__":
    import sys
    #set global escape
    event.globalKeys.add(key='escape', func=sys.exit)

    from kraepelin_stimuli import KraepelinWindow
    win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)

    practice_tenkey(win)