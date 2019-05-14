from psychopy import visual, sound, event, core, gui
import random
import sys
import collections

from kraepelin_stimuli import get_fixation_stim

#set global escape
event.globalKeys.add(key='escape', func=sys.exit)

win = visual.Window(units='pix', fullscr=True, allowGUI=False)

wait_msg = visual.TextStim(win, 'Wait...', height=80)
start_msg = visual.TextStim(win, 'Start!', height=80)
finish_msg = visual.TextStim(win, 'Finish!', height=80)


SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
	'into_EOresting', 'into_ECresting', 'into_subtract', 'finish_resting', 'answer_of_subtraction'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

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

sound_namedtuple.into_EOresting.play()
core.wait(sound_namedtuple.into_EOresting.duration)

start_msg.draw()
win.flip()

core.wait(2)

fixation.draw()
win.flip()

core.wait(60)

finish_msg.draw()
win.flip()

sound_namedtuple.finish_resting.play()
core.wait(sound_namedtuple.finish_resting.duration)

#eyes close------------------

wait_msg.draw()
win.flip() 
sound_namedtuple.into_ECresting.play()
core.wait(sound_namedtuple.into_ECresting.duration)

Beep1.play()

start_msg.draw()
win.flip()

core.wait(2)

fixation.draw()
win.flip()

core.wait(60)

finish_msg.draw()
win.flip()

sound_namedtuple.finish_resting.play()
core.wait(sound_namedtuple.finish_resting.duration)

#subtraction------------------

wait_msg.draw()
win.flip()
sound_namedtuple.into_subtract.play()
core.wait(sound_namedtuple.into_subtract.duration)

Beep2.play()

start_msg.draw()
win.flip()

core.wait(2)

fixation.draw()
win.flip()

core.wait(60)

finish_msg.draw()
win.flip()

sound_namedtuple.finish_resting.play()
core.wait(sound_namedtuple.finish_resting.duration)

win.setMouseVisible(True)
win.flip()
sound_namedtuple.answer_of_subtraction.play()
dlg.show()

