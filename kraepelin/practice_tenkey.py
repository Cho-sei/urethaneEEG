from psychopy import visual, sound, event, core
import random
import sys

#set global escape
event.globalKeys.add(key='escape', func=sys.exit)

KEY_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

redo_flag = True

win = visual.Window(units='pix', fullscr=True, allowGUI=False)

inst_stim = visual.TextStim(win, height=80)
ans_text = visual.TextStim(win, height=80, pos=(0,-100))

opening_msg = visual.TextStim(win, 'Practice entering tenkey', height=80)
wait_msg = visual.TextStim(win, 'Wait...', height=80)
start_msg = visual.TextStim(win, 'Start!', height=80)
finish_msg = visual.TextStim(win, 'Finish!', height=80)
redo_msg = visual.TextStim(win, 'Redo', height=80)

correct_msg = visual.TextStim(win, '○', height=80, pos=(0,-200))
false_msg = visual.TextStim(win, '×', height=80, pos=(0,-200))

stim_list = random.sample(KEY_LIST, len(KEY_LIST)) + random.sample(KEY_LIST, len(KEY_LIST))

into_ten = sound.Sound('sounds/into_ten.wav')
start_ten = sound.Sound('sounds/start_ten.wav')
redo_ten = sound.Sound('sounds/redo_ten.wav')
start_demo = sound.Sound('sounds/start_demo.wav')
finish_demo = sound.Sound('sounds/finish_demo.wav')


#--start------------------------------------------------------------------------------
opening_msg.draw()
win.flip()

into_ten.play()

core.wait(32)

wait_msg.draw()
win.flip()

start_ten.play()

core.wait(12)

start_demo.play()

core.wait(4)

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

        redo_ten.play()

        core.wait(7)

finish_msg.draw()
win.flip()

finish_demo.play()

event.waitKeys(keyList=['space'])