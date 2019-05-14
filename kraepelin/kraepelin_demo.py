import collections
import itertools
import math
import random
import sys

from psychopy import visual, core, event, sound

#set global escape
event.globalKeys.add(key='escape', func=sys.exit)

#parameter
trial_duration = 60
block_length = 2
TRIAL_LENGTH = 52

#defined sounds
SoundNamedTuple = collections.namedtuple('SoundNamedTuple', ['introduction', 'inst_calc', 'inst_cue_num', 'inst_progress', 'firstblock', 'inst_cue_value', 'into_second', 'secondblock', 'into_demo', 'start_demo', 'finish_demo', 'confirmation', 'inst_fixa', 'summary_cue'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

#instruction start---------------------------------------------------------------------
def instruction(win):
	#components settings
	emphasisrect_dict = {
		key:visual.Rect(win, pos=stim.pos, width=200, height=200, lineColor='red', lineWidth=5)
		for key, stim in dict(msg_count=win.msg_count, matrixstim_left=win.matrixstim_left, matrixstim_right=win.matrixstim_right).items()
	}
	arrow = visual.ShapeStim(
		win, vertices=((-15,0),(-15,30),(15,30),(15,0),(30,0),(0,-30),(-30,0)),
		pos=(0,-200), lineColor='white',fillColor='white')
	demo_cor_ans = visual.TextStim(win, pos=(0, -300), height=80, bold=True)

	#set matrix
	win.matrixstim_left.set_random_matrix(4, 6)
	win.matrixstim_right.set_random_matrix(8, 3)


	sound_namedtuple.introduction.play()
	visual.TextStim(win, text='task instruction', height=80, bold=True).draw()
	win.flip()
	core.wait(8)

	sound_namedtuple.inst_calc.play()
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right],
		wait_time=35,
	)

	#1st block-----------------------------------------------------------------------------
	sound_namedtuple.inst_progress.play()
	win.msg_count.setText("0")
	win.display_stimuli(
		[win.msg_count],
		wait_time=5,
	)
	win.display_stimuli(
		[emphasisrect_dict['msg_count'], win.msg_count],
		wait_time=16,
	)
	win.display_stimuli(
		[win.msg_count],
		wait_time=13
	)
	win.display_stimuli(
		[win.LRcue_dict[(True, False)]],
		wait_time=0.5,
	)
	win.display_stimuli(
		[], wait_time=0.5,
	)

	sound_namedtuple.inst_cue_num.play()
	core.wait(2)
	win.display_stimuli(
		[win.LRcue_dict[(True, False)]],
		wait_time=41,
	)

	sound_namedtuple.firstblock.play()
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right],
		wait_time=13,
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, emphasisrect_dict['matrixstim_left']],
		wait_time=2,
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, emphasisrect_dict['matrixstim_right']],
		wait_time=4,
	)
	win.msg_answer.setText("7")
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, win.msg_answer],
		wait_time=3,
	)

	sound_namedtuple.inst_cue_value.play()
	win.display_stimuli(
		[], wait_time=4,
	)
	win.display_stimuli(
		[win.LRcue_dict[(True,False)]],
		wait_time=7,
	)
	win.display_stimuli(
		[win.LRcue_dict[(False,True)]],
		wait_time=5,
	)
	win.display_stimuli(
		[win.LRcue_dict[(True,True)]],
		wait_time=3,
	)	
	win.display_stimuli(
		[win.LRcue_dict[(False,False)]],
		wait_time=13,
	)

	#2nd block-----------------------------------------------------------------------------
	#set matrix
	win.matrixstim_left.set_random_matrix(4, 8)
	win.matrixstim_right.set_random_matrix(1, 5)

	sound_namedtuple.into_second.play()
	win.msg_count.setText("1")
	win.display_stimuli(
		[win.msg_count],
		wait_time=12,
	)
#	empha_rect.setAutoDraw(False)#???
	win.display_stimuli(
		[win.LRcue_dict[(False,False)]],
		wait_time=0.5,
	)
	win.display_stimuli(
		[], wait_time=0.5,
	)

	sound_namedtuple.secondblock.play()
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right],
		wait_time=16,
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, emphasisrect_dict['matrixstim_left']],
		wait_time=3,
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, emphasisrect_dict['matrixstim_right']],
		wait_time=4,
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right],
		wait_time=3,
	)
	win.msg_answer.setText('13')
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, win.msg_answer],
		wait_time=7,
	)
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, win.msg_answer, arrow],
		wait_time=2,
	)
	demo_cor_ans.setText('3')
	win.display_stimuli(
		[win.fixation, win.matrixstim_left, win.matrixstim_right, win.msg_answer, arrow, demo_cor_ans],
		wait_time=3,
	)

	sound_namedtuple.inst_fixa.play()
	win.display_stimuli(
		[], wait_time=14,
	)

#summary------------------------------------------------------------------------------
	sound_namedtuple.summary_cue.play()
	win.display_stimuli(
		[
			visual.TextStim(win, " V :  数字", bold=True, height=80, pos=(50,100)),
			visual.TextStim(win, " N :  個数", bold=True, height=80, pos=(50,-100))
		],
		wait_time=17,
	)

#start demo---------------------------------------------------------------------------
def demo(win):
	visual.TextStim(win, text='demonstration', height=80, bold=True).draw()
	win.flip()

	sound_namedtuple.start_demo.play()

	core.wait(2)

	visual.TextStim(win, text='Start!', height=80, bold=True).draw()
	win.flip()

	core.wait(2)

	for blocks in range(block_length):
		matrixstim_left.set_random_matrix(random.randint(1, 9), random.randint(1, 9))

		rt_list = []
		correct = 0
		task_start = clock.getTime()

		KEYLIST = ['0','1','2','3','4','5','6','7','8','9']

		cueflag_list = [(False, False)]*(TRIAL_LENGTH//4) + [(False, True)]*(TRIAL_LENGTH//4) + [(True, False)]*(TRIAL_LENGTH//4) + [(True, True)]*(TRIAL_LENGTH//4)
		random.shuffle(cueflag_list)
		
		for trials, cue_flag in enumerate(cueflag_list):
			# display fixation
			count_fixation.setText(trials)
			count_fixation.draw()
			win.flip()
			core.wait(1)

			#display cues
			LRcue_dict[cue_flag].draw()			
			win.flip()
			core.wait(0.5)

			win.flip()
			core.wait(0.5)

			#display numbers
			fixation.draw()
			matrixstim_right.set_random_matrix(random.randint(1, 9),random.randint(1, 9))
			matrixstim_left.draw()
			matrixstim_right.draw()
			win.flip()

			#enter keys and measure response time
			key_start = clock.getTime()
			task_time = clock.getTime() - task_start
			keys = event.waitKeys(
				maxWait=trial_duration-task_time,
				keyList=KEYLIST)
			if keys == None:
				break
			
			key_end = clock.getTime()

			rt = key_end - key_start
			rt_list.append(rt)

			#display after answered
			answer_number = KEYLIST.index(keys[0])
			answer.setText(answer_number)
			answer.draw()
			win.flip()

			matrixstim_left.copy_status(matrixstim_right)

			core.wait(0.2)

	visual.TextStim(win, text='Finish!', height=80, bold=True).draw()
	win.flip()

	sound_namedtuple.finish_demo.play()
	core.wait(4)

#confirmation------------------------------------------------------------------------
def display_confirmation(win):
	sound_namedtuple.confirmation.play()
	for text, pos in zip(['instruction → 1', 'demonstration → 2', 'exit → 3'], [(0, 200), (0, 0), (0, -200)]):
		visual.TextStim(win, text=text, height=80, bold=True, pos=pos).draw()
	win.flip()


if __name__ == "__main__":
	from kraepelin_stimuli import KraepelinWindow
	win = KraepelinWindow(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)
	
	instruction(win)

	win.flip()

	sound_namedtuple.into_demo.play()
	core.wait(4)

	visual.TextStim(win, text='demonstration', height=80, bold=True).draw()
	win.flip()

	core.wait(15)

	demo(win)

	display_confirmation(win)

	while True:
		key = event.waitKeys(keyList=['1','2','3'])
		if  '1' in key:
			instruction(win)
		elif '2' in key:
			demo(win)
		else:
			break
		
		display_confirmation(win)

#--------------------------------------------------------
#
#	まとめスライド
#	Cueについて箇条書きor表にしてまとめ
#
#------------------------------------------------------