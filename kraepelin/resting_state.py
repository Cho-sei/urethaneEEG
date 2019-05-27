import collections
import random
from psychopy import visual, sound, core, event
from dialog_alternative import dialog_alternative
from kraepelin_stimuli import get_fixation_stim
from quick20_trigger import send_trigger
SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
	'into_subtract_1007', 'into_subtract_1012', 'into_subtract_1004', 'into_subtract_1000', 'into_EOresting', 'into_ECresting', 'finish_resting', 'answer_of_subtraction'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

RECORDING_DURATION = 60#[s]

#start-----------------------------------------------------------------
def start_waitmsg(func):
	def wrapper(*args, **keyargs):#assert isinstance(args[0], visual.Window)
		visual.TextStim(args[0], 'Wait...', height=80).draw()
		args[0].flip()
		core.wait(2.)
		return func(*args, **keyargs)
	return wrapper

def restingstate_recording(win, wait_time, trigger):
	visual.TextStim(win, 'Start!', height=80).draw()
	win.flip()
	core.wait(2)

	get_fixation_stim(win).draw()
	win.flip()

	send_trigger(trigger)
	core.wait(wait_time)
	send_trigger(trigger)

	visual.TextStim(win, 'Finish!', height=80).draw()
	win.flip()

@start_waitmsg
def eyesopen_restingstate_recording(win, trigger):
	sound_namedtuple.into_EOresting.play()
	core.wait(sound_namedtuple.into_EOresting.getDuration())
	core.wait(2)

	restingstate_recording(win, RECORDING_DURATION, trigger)

	sound_namedtuple.finish_resting.play()
	core.wait(sound_namedtuple.finish_resting.getDuration())

@start_waitmsg
def eyesclose_restingstate_recording(win, trigger):
	beep = sound.Sound(value=1000, secs=1.0)
	beep.setVolume(0.5)

	sound_namedtuple.into_ECresting.play()
	core.wait(sound_namedtuple.into_ECresting.getDuration())
	core.wait(2)
	beep.play()

	restingstate_recording(win, RECORDING_DURATION, trigger)

	sound_namedtuple.finish_resting.play()
	core.wait(sound_namedtuple.finish_resting.getDuration())

@start_waitmsg
def subtractingstate_recording(win, trigger, times):
	beep = sound.Sound(value=1000, secs=1.0)
	beep.setVolume(0.5)

	sound_namedtuple[times].play()
	core.wait(sound_namedtuple[times].getDuration())
	core.wait(2)
	beep.play()

	restingstate_recording(win, RECORDING_DURATION, trigger)

	sound_namedtuple.finish_resting.play()
	core.wait(sound_namedtuple.finish_resting.getDuration())

	win.flip()
	sound_namedtuple.answer_of_subtraction.play()
	return dialog_alternative(win, explain_stimuli=[
		visual.TextStim(win, u"回答を入力してください", height=40, pos=(0, 250)),
		visual.TextStim(win, u"Enter : 決定", height=40, pos=(0, 300)),
		visual.TextStim(win, u"Delete : 1字戻る", height=40, pos=(0, 350)),
		], height=80)

if __name__ == "__main__":
	import collections
	from psychopy import event
	from kraepelin_stimuli import KraepelinWindow
	#set global escape
	event.globalKeys.add(key='escape', func=core.quit)

	win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)

	eyesopen_restingstate_recording(win, 'a')
	eyesclose_restingstate_recording(win, 'a')
	print(subtractingstate_recording(win, 'a', 1))