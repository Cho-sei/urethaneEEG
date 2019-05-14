from psychopy import visual, sound, event, core, gui
import random
import sys

from kraepelin_stimuli import get_fixation_stim

#set global escape
event.globalKeys.add(key='escape', func=sys.exit)

win = visual.Window(units='pix', fullscr=True, allowGUI=False)

wait_msg = visual.TextStim(win, 'Wait...', height=80)
start_msg = visual.TextStim(win, 'Start!', height=80)
finish_msg = visual.TextStim(win, 'Finish!', height=80)

into_EOresting = sound.Sound('sounds/into_EOresting.wav')
into_ECresting = sound.Sound('sounds/into_ECresting.wav')
into_subtract = sound.Sound('sounds/into_subtract.wav')
finish_resting = sound.Sound('sounds/finish_resting.wav')
answer_msg = sound.Sound('sounds/answer_of_subtraction.wav')

Beep1 = sound.Sound(value=1000, secs=1.0)
Beep2 = sound.Sound(value=1000, secs=1.0)
Beep1.setVolume(0.5)
Beep2.setVolume(0.5)

fixation = get_fixation_stim(win)

dlg = gui.Dlg(title=u'回答')
dlg.addField(u'答え:','')

#start-----------------------------------------------------------------

#eyes open------------------
wait_msg.draw()
win.flip()

into_EOresting.play()

core.wait(14)

start_msg.draw()
win.flip()

core.wait(2)

fixation.draw()
win.flip()

core.wait(60)

finish_msg.draw()
win.flip()

finish_resting.play()

core.wait(5)

#eyes close------------------

into_ECresting.play()

wait_msg.draw()
win.flip() 

core.wait(17)

Beep1.play()

start_msg.draw()
win.flip()

core.wait(2)

fixation.draw()
win.flip()

core.wait(60)

finish_msg.draw()
win.flip()

finish_resting.play()

core.wait(5)

#subtraction------------------

into_subtract.play()

wait_msg.draw()
win.flip()

core.wait(25)

Beep2.play()

start_msg.draw()
win.flip()

core.wait(2)

fixation.draw()
win.flip()

core.wait(60)

finish_msg.draw()
win.flip()

finish_resting.play()

core.wait(2)

win.setMouseVisible(True)
win.flip()
answer_msg.play()
dlg.show()

