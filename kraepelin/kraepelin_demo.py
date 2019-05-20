import collections
import itertools
import math
import random

from psychopy import visual, core, sound

from kraepelin import kraepelin_experiment
from kraepelin_trigger import trigger_values
from quick20_trigger import send_trigger

#defined sounds
SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
	'introduction', 'inst_calc','post_cue', 'inst_cue_num', 'inst_progress_1', 'inst_progress_2', 'inst_progress_3', 
	'firstblock_1', 'firstblock_2', 'firstblock_3', 'firstblock_4', 'inst_cue_value_1', 'inst_cue_value_2', 'inst_cue_value_3', 'inst_cue_value_4', 
	'inst_cue_value_5', 'into_second', 'secondblock_1', 'secondblock_2', 'secondblock_3', 'secondblock_4', 'secondblock_5', 'secondblock_6', 
	'secondblock_7', 'into_demo', 'finish_instruction', 'start_demo', 'finish_demo', 'confirmation', 'inst_fixa', 'summary_cue'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

#instruction start---------------------------------------------------------------------
def instruction(win):
	send_trigger(trigger_values.Demo_Inst)

	#components settings
	emphasisrect_dict = {
		key:visual.Rect(win, pos=stim.pos, width=200, height=200, lineColor='red', lineWidth=5)
		for key, stim in dict(msg_count=win.msg_count, matrixstim_left=win.matrixstim_left, matrixstim_right=win.matrixstim_right).items()
	}
	arrow = visual.ShapeStim(
		win, vertices=((-15,0),(-15,30),(15,30),(15,0),(30,0),(0,-30),(-30,0)),
		pos=(0,-200), lineColor='white',fillColor='white')
	demo_cor_ans = visual.TextStim(win, pos=(0, -300), height=80, bold=True)

	win.display_stimuli(
		[visual.TextStim(win, text=u'課題説明', height=80, bold=True)],
		sound=sound_namedtuple.introduction,
		wait_time=2.,
	)

#1st block-----------------------------------------------------------------------------
	win.msg_count.setText("0")
	win.msg_answer.setText("7")
	#set matrix
	win.matrixstim_left.set_random_matrix(6, 4)
	win.matrixstim_right.set_random_matrix(3, 8)

	win.display_stimuli(
		[win.msg_count],
		sound=sound_namedtuple.inst_progress_1,
		wait_time=1.
	)
	win.display_stimuli(
		[emphasisrect_dict['msg_count'], win.msg_count],
		sound=sound_namedtuple.inst_progress_2,
		wait_time=1.
	)
	win.display_stimuli(
		[win.msg_count],
		sound=sound_namedtuple.inst_progress_3,
		wait_time=1.
	)
	win.display_stimuli(
		[win.LRcue_dict[(True, False)]],
		wait_time=0.5,
	)
	win.display_stimuli(
		[],
		wait_time=0.5,
	)
	win.display_stimuli(
		[],
		sound=sound_namedtuple.post_cue,
		wait_time=1.
	)
	win.display_stimuli(
		[win.LRcue_dict[(True, False)]],
		sound=sound_namedtuple.inst_cue_num,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right],
		sound=sound_namedtuple.firstblock_1,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, emphasisrect_dict['matrixstim_left']],
		sound=sound_namedtuple.firstblock_2,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, emphasisrect_dict['matrixstim_right']],
		sound=sound_namedtuple.firstblock_3,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, win.msg_answer],
		sound=sound_namedtuple.firstblock_4,
		wait_time=1.
	)
	win.display_stimuli(
		[],
		sound=sound_namedtuple.inst_cue_value_1,
		wait_time=1.
	)
	win.display_stimuli(
		[win.LRcue_dict[(True, False)]],
		sound=sound_namedtuple.inst_cue_value_2,
		wait_time=1.
	)
	win.display_stimuli(
		[win.LRcue_dict[(False, True)]],
		sound=sound_namedtuple.inst_cue_value_3,
		wait_time=1.
	)
	win.display_stimuli(
		[win.LRcue_dict[(True, True)]],
		sound=sound_namedtuple.inst_cue_value_4,
		wait_time=1.
	)
	win.display_stimuli(
		[win.LRcue_dict[(False, False)]],
		sound=sound_namedtuple.inst_cue_value_5,
		wait_time=1.
	)
#2nd block-----------------------------------------------------------------------------
	win.msg_count.setText("1")
	win.msg_answer.setText("13")
	demo_cor_ans.setText("3")
	#set matrix
	win.matrixstim_left.set_random_matrix(8, 4)
	win.matrixstim_right.set_random_matrix(5, 1)

	win.display_stimuli(
		[win.msg_count, emphasisrect_dict['msg_count']],
		sound=sound_namedtuple.into_second,
		wait_time=1.
	)
	win.display_stimuli(
		[win.LRcue_dict[(False, False)]],
		wait_time=0.5,
	)
	win.display_stimuli(
		[],
		wait_time=0.5,
	)
	win.display_stimuli(
		[],
		sound=sound_namedtuple.post_cue,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right],
		sound=sound_namedtuple.secondblock_1,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, emphasisrect_dict['matrixstim_left']],
		sound=sound_namedtuple.secondblock_2,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, emphasisrect_dict['matrixstim_right']],
		sound=sound_namedtuple.secondblock_3,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right],
		sound=sound_namedtuple.secondblock_4,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, win.msg_answer],
		sound=sound_namedtuple.secondblock_5,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, win.msg_answer, arrow],
		sound=sound_namedtuple.secondblock_6,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, win.msg_answer, arrow, demo_cor_ans],
		sound=sound_namedtuple.secondblock_7,
		wait_time=1.
	)
	win.display_stimuli(
		[win.fixation],
		sound=sound_namedtuple.inst_fixa,
		wait_time=1.
	)

#summary------------------------------------------------------------------------------
	win.display_stimuli(
		[
			visual.TextStim(win, " V :  数字", bold=True, height=80, pos=(50,100)),
			visual.TextStim(win, " N :  個数", bold=True, height=80, pos=(50,-100))
		],
		sound=sound_namedtuple.summary_cue,
		wait_time=2.
	)
	win.display_stimuli(
		[],
		sound=sound_namedtuple.finish_instruction,
		wait_time=1.,
	)


#start demo---------------------------------------------------------------------------
def demo(kraepelin_window, block_length, log_name='result_demo.csv'):
	send_trigger(trigger_values.Demo_Start)

	kraepelin_window.display_stimuli(
		[visual.TextStim(kraepelin_window, text=u'練習', height=80, bold=True)],
		sound=sound_namedtuple.into_demo,
	)
	kraepelin_window.display_stimuli(
		[],
		sound=sound_namedtuple.start_demo,
	)

	kraepelin_experiment(kraepelin_window, block_length, log_name=log_name)

	kraepelin_window.display_stimuli(
		[],
		sound=sound_namedtuple.finish_demo,
		wait_time=1.,
	)
	send_trigger(trigger_values.Demo_Fin)

#confirmation------------------------------------------------------------------------
def display_confirmation(kraepelin_window):
	kraepelin_window.display_stimuli(
		[visual.TextStim(kraepelin_window, text=text, height=80, bold=True, pos=pos) for text, pos in zip([u'説明 → 1', u'練習 → 2', u'本番 → 3'], [(0, 200), (0, 0), (0, -200)])],
		sound=sound_namedtuple.confirmation,
	)


if __name__ == "__main__":
	import sys
	from psychopy import event
	from kraepelin_stimuli import KraepelinWindow

	#set global escape
	event.globalKeys.add(key='escape', func=sys.exit)


	block_length = 2
	win = KraepelinWindow(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)
	
	instruction(win)
	demo(win, block_length)
	display_confirmation(win)

	while True:
		key = event.waitKeys(keyList=['num_1','num_2','num_3'])
		if  '1' in key:
			instruction(win)
		elif '2' in key:
			demo(win, block_length)
		else:
			break
		
		display_confirmation(win)

