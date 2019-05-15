import random
from psychopy import visual, sound, core, gui
from kraepelin_stimuli import get_fixation_stim

#start-----------------------------------------------------------------
def start_waitmsg(func):
	def wrapper(*args, **keyargs):#assert isinstance(args[0], visual.Window)
		visual.TextStim(args[0], 'Wait...', height=80).draw()
		args[0].flip()
		core.wait(2.)
		return func(*args, **keyargs)
	return wrapper

def restingstate_recording(win, wait_time):
	visual.TextStim(win, 'Start!', height=80).draw()
	win.flip()
	core.wait(2)

	get_fixation_stim(win).draw()
	win.flip()
	core.wait(wait_time)

	visual.TextStim(win, 'Finish!', height=80).draw()
	win.flip()

@start_waitmsg
def eyesopen_restingstate_recording(win, sounds):
	sounds.into_EOresting.play()
	core.wait(sounds.into_EOresting.duration)

	restingstate_recording(win, 60)

	sounds.finish_resting.play()
	core.wait(sounds.finish_resting.duration)

@start_waitmsg
def eyesclose_restingstate_recording(win, sounds):
	beep = sound.Sound(value=1000, secs=1.0)
	beep.setVolume(0.5)

	sounds.into_ECresting.play()
	core.wait(sounds.into_ECresting.duration)
	beep.play()

	restingstate_recording(win, 60)

	sounds.finish_resting.play()
	core.wait(sounds.finish_resting.duration)

@start_waitmsg
def subtractingstate_recording(win, sounds):
	beep = sound.Sound(value=1000, secs=1.0)
	beep.setVolume(0.5)
	dlg = gui.Dlg(title=u'回答')
	dlg.addField(u'答え:','')

	sounds.into_subtract.play()
	core.wait(sounds.into_subtract.duration)
	beep.play()

	restingstate_recording(win, 60)

	sounds.finish_resting.play()
	core.wait(sounds.finish_resting.duration)

	win.setMouseVisible(True)
	win.flip()
	sound_namedtuple.answer_of_subtraction.play()
	return dlg.show()

if __name__ == "__main__":
	import collections
	import sys
	from psychopy import event
	from kraepelin_stimuli import KraepelinWindow
	#set global escape
	event.globalKeys.add(key='escape', func=sys.exit)

	win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)
	SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
		'into_EOresting', 'into_ECresting', 'into_subtract', 'finish_resting', 'answer_of_subtraction'])
	sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

	eyesopen_restingstate_recording(win, sound_namedtuple)
	eyesclose_restingstate_recording(win, sound_namedtuple)
	print(subtractingstate_recording(win, sound_namedtuple))