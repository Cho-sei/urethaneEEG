from psychopy import visual, sound, event, core
import random

KEY_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

win = visual.Window(units='pix', fullscr=True, allowGUI=False)

inst_stim = visual.TextStim(win, height=80)
ans_text = visual.TextStim(win, height=80, pos=(0,-100))

correct_msg = visual.TextStim(win, 'Correct!', height=80, pos=(0,-200))
false_msg = visual.TextStim(win, 'False!', height=80, pos=(0,-200))

for count in range(5):
    inst_number = random.randint(0,9)
    inst_stim.setText(inst_number)
    
    inst_stim.draw()
    win.flip()

    while True:
        keys = event.waitKeys(keyList=KEY_LIST)
        if 'escape' in keys:
            break
        
        answer_number = KEY_LIST.index(keys[0])

        ans_text.setText(answer_number)
        ans_text.draw()
        inst_stim.draw()
        win.flip()

        if answer_number == inst_number:
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

