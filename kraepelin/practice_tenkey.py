from psychopy import visual, sound, event, core
import random
import sys
import collections

#set global escape
event.globalKeys.add(key='escape', func=sys.exit)

KEY_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

redo_flag = True

win = visual.Window(units='pix', fullscr=True, allowGUI=False)

inst_stim = visual.TextStim(win, height=80)
ans_text = visual.TextStim(win, height=80, pos=(0,-100))

opening_msg = visual.TextStim(win, text=u'テンキー入力練習', height=80)
wait_msg = visual.TextStim(win, 'Wait...', height=80)
start_msg = visual.TextStim(win, 'Start!', height=80)
finish_msg = visual.TextStim(win, 'Finish!', height=80)
redo_msg = visual.TextStim(win, 'Redo', height=80)

correct_msg = visual.TextStim(win, '○', height=80, pos=(0,-200))
false_msg = visual.TextStim(win, '×', height=80, pos=(0,-200))

stim_list = random.sample(KEY_LIST, len(KEY_LIST)) + random.sample(KEY_LIST, len(KEY_LIST))


SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
	'into_ten', 'start_ten', 'redo_ten', 'start_demo', 'finish_demo'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})


#--start------------------------------------------------------------------------------
opening_msg.draw()
win.flip()
sound_namedtuple.into_ten.play()
core.wait(sound_namedtuple.into_ten.duration)

wait_msg.draw()
win.flip()
sound_namedtuple.start_ten.play()
core.wait(sound_namedtuple.start_ten.duration)

sound_namedtuple.start_demo.play()
core.wait(sound_namedtuple.start_demo.duration)

while redo_flag:

    start_msg.draw()
    win.flip()

    core.wait(2)

    false_counter = 0

    for count in stim_list:
        inst_stim.setText(count)
        
        inst_stim.draw()
        win.flip()

        while True:
            keys = event.waitKeys(keyList=KEY_LIST)
            
            answer_number = KEY_LIST.index(keys[0])

            ans_text.setText(answer_number)
            ans_text.draw()
            inst_stim.draw()
            win.flip()

            if answer_number == int(count):
                ans_text.draw()
                inst_stim.draw()
                correct_msg.draw()
                win.flip()
                core.wait(1)
                break
            else:
                ans_text.draw()
                inst_stim.draw()
                false_msg.draw()
                win.flip()
                core.wait(1)
                inst_stim.draw()
                win.flip()
                false_counter += 1

    if false_counter < 4:
        redo_flag = False
    else:
        redo_msg.draw()
        win.flip()
        sound_namedtuple.redo_ten.play()
        core.wait(sound_namedtuple.redo_ten.duration)

finish_msg.draw()
win.flip()

sound_namedtuple.finish_demo.play()
core.wait(sound_namedtuple.finish_demo.duration)

event.waitKeys(keyList=['space'])