from psychopy import visual, core, event, sound
import random
import numpy as np
import itertools
import math
import sys
import collections

from kraepelin_stimuli import get_fixation_stim, get_charcue_stim_dict, KraepelinMatrixStim

#set global escape
event.globalKeys.add(key='escape', func=sys.exit)

x = y = np.array([-50, 0, 50])

def arrangement(text, num, position, posList):
	text_view.setText(text)

	matrix = list(itertools.product(x+position, y))
	
	for i in range(num):
		text_view.setPos(matrix[posList[i]])
		text_view.draw()


#parameter
trial_duration = 60
block_length = 2
TRIAL_LENGTH = 52


#window defined
win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

#define components for instruction
empha_rect = visual.Rect(win, width=200, height=200, lineColor='red', lineWidth=5)
demo_ans = visual.TextStim(win, pos=(0, -100), height=80, bold=True)
allow = visual.ShapeStim(
	win, vertices=((-15,0),(-15,30),(15,30),(15,0),(30,0),(0,-30),(-30,0)),
	pos=(0,-200), lineColor='white',fillColor='white')
demo_cor_ans = visual.TextStim(win, pos=(0, -300), height=80, bold=True)
fixation = get_fixation_stim(win)
count_fixation = visual.TextStim(win, pos=(0, 0), height=80, bold=True)

text_view = visual.TextStim(win, height=50)

summary_text1 = visual.TextStim(win, u" V :  数字", bold=True, height=80, pos=(0,100))
summary_text2 = visual.TextStim(win, u" N :  個数", bold=True, height=80, pos=(0,-100))


#defined sounds
SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
	'introduction', 'inst_calc','post_cue', 'inst_cue_num', 'inst_progress_1', 'inst_progress_2', 'inst_progress_3', 
	'firstblock_1', 'firstblock_2', 'firstblock_3', 'firstblock_4', 'inst_cue_value_1', 'inst_cue_value_2', 'inst_cue_value_3', 'inst_cue_value_4', 
	'inst_cue_value_5', 'into_second', 'secondblock_1', 'secondblock_2', 'secondblock_3', 'secondblock_4', 'secondblock_5', 'secondblock_6', 
	'secondblock_7', 'into_demo', 'finish_instruction', 'start_demo', 'finish_demo', 'confirmation', 'inst_fixa', 'summary_cue'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

#instruction start---------------------------------------------------------------------
def instruction(win):
	visual.TextStim(win, text=u'課題説明', height=80, bold=True).draw()
	win.flip()
	sound_namedtuple.introduction.play()
	core.wait(sound_namedtuple.introduction.duration)

	fixation.draw()
	pos_left = random.sample(range(9), k=6)
	pos_right = random.sample(range(9), k=3)
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	win.flip()
	sound_namedtuple.inst_calc.play()
	core.wait(sound_namedtuple.inst_calc.duration)

	#1st block-----------------------------------------------------------------------------

	count_fixation.setText("0")
	count_fixation.draw()
	win.flip()
	sound_namedtuple.inst_progress_1.play()
	core.wait(sound_namedtuple.inst_progress_1.duration)

	empha_rect.setPos((0,0))
	empha_rect.draw()
	count_fixation.draw()
	win.flip()
	sound_namedtuple.inst_progress_2.play()
	core.wait(sound_namedtuple.inst_progress_2.duration)

	count_fixation.draw()
	win.flip()
	sound_namedtuple.inst_progress_3.play()
	core.wait(sound_namedtuple.inst_progress_3.duration)

	LRcue_dict[(True,False)].draw()
	win.flip()

	core.wait(0.5)

	win.flip()

	core.wait(0.5)

	sound_namedtuple.post_cue.play()
	core.wait(sound_namedtuple.post_cue.duration)

	LRcue_dict[(True,False)].draw()
	win.flip()
	sound_namedtuple.inst_cue_num.play()
	core.wait(sound_namedtuple.inst_cue_num.duration)

	fixation.draw()
	pos_left = random.sample(range(9), k=6)
	pos_right = random.sample(range(9), k=3)
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	win.flip()
	sound_namedtuple.firstblock_1.play()
	core.wait(sound_namedtuple.firstblock_1.duration) 

	fixation.draw()
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	empha_rect.setPos((-200, 0))
	empha_rect.draw()
	win.flip()
	sound_namedtuple.firstblock_2.play()
	core.wait(sound_namedtuple.firstblock_2.duration)

	fixation.draw()
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	empha_rect.setPos((200, 0))
	empha_rect.draw()
	win.flip()
	sound_namedtuple.firstblock_3.play()
	core.wait(sound_namedtuple.firstblock_3.duration)

	fixation.draw()
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	demo_ans.setText("7")
	demo_ans.draw()
	win.flip()
	sound_namedtuple.firstblock_4.play()
	core.wait(sound_namedtuple.firstblock_4.duration)

	win.flip()
	sound_namedtuple.inst_cue_value_1.play()
	core.wait(sound_namedtuple.inst_cue_value_1.duration)

	LRcue_dict[(True,False)].draw()
	win.flip()
	sound_namedtuple.inst_cue_value_2.play()
	core.wait(sound_namedtuple.inst_cue_value_2.duration)

	LRcue_dict[(False,True)].draw()
	win.flip()
	sound_namedtuple.inst_cue_value_3.play()
	core.wait(sound_namedtuple.inst_cue_value_3.duration)
	
	LRcue_dict[(True,True)].draw()
	win.flip()
	sound_namedtuple.inst_cue_value_4.play()
	core.wait(sound_namedtuple.inst_cue_value_4.duration)

	LRcue_dict[(False,False)].draw()
	win.flip()
	sound_namedtuple.inst_cue_value_5.play()
	core.wait(sound_namedtuple.inst_cue_value_5.duration)


	#2nd block-----------------------------------------------------------------------------

	count_fixation.setText("1")
	count_fixation.draw()
	empha_rect.setAutoDraw(False)
	win.flip()
	sound_namedtuple.into_second.play()
	core.wait(sound_namedtuple.into_second.duration)

	LRcue_dict[(False,False)].draw()
	win.flip()

	core.wait(0.5)

	win.flip()

	core.wait(0.5)

	sound_namedtuple.post_cue.play()
	core.wait(sound_namedtuple.post_cue.duration)

	fixation.draw()
	pos_left = random.sample(range(9), k=8)
	pos_right = random.sample(range(9), k=5)
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	win.flip()
	sound_namedtuple.secondblock_1.play()
	core.wait(sound_namedtuple.secondblock_1.duration)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	empha_rect.setPos((-200, 0))
	empha_rect.draw()
	win.flip()
	sound_namedtuple.secondblock_2.play()
	core.wait(sound_namedtuple.secondblock_2.duration)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	empha_rect.setPos((200, 0))
	empha_rect.draw()
	win.flip()
	sound_namedtuple.secondblock_3.play()
	core.wait(sound_namedtuple.secondblock_3.duration)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	win.flip()
	sound_namedtuple.secondblock_4.play()
	core.wait(sound_namedtuple.secondblock_4.duration)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_ans.setText("13")
	demo_ans.draw()
	win.flip()
	sound_namedtuple.secondblock_5.play()
	core.wait(sound_namedtuple.secondblock_5.duration)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_ans.draw()
	allow.draw()
	win.flip()
	sound_namedtuple.secondblock_6.play()
	core.wait(sound_namedtuple.secondblock_6.duration)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_cor_ans.setText("3")
	demo_ans.draw()
	allow.draw()
	demo_cor_ans.draw()
	win.flip()
	sound_namedtuple.secondblock_7.play()
	core.wait(sound_namedtuple.secondblock_7.duration)

	fixation.draw()
	win.flip()
	sound_namedtuple.inst_fixa.play()
	core.wait(sound_namedtuple.inst_fixa.duration)

#summary------------------------------------------------------------------------------
	summary_text1.draw()
	summary_text2.draw()
	win.flip()
	sound_namedtuple.summary_cue.play()
	core.wait(sound_namedtuple.summary_cue.duration)

#start demo---------------------------------------------------------------------------
def demo(win):
	visual.TextStim(win, text='Wait...', height=80, bold=True).draw()
	win.flip()
	sound_namedtuple.start_demo.play()
	core.wait(sound_namedtuple.start_demo.duration)

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
	core.wait(sound_namedtuple.finish_demo.duration)

#confirmation------------------------------------------------------------------------
def display_confirmation(win):
	visual.TextStim(win, text=u'説明 → 1', height=80, bold=True, pos=(0, 200)).draw()
	visual.TextStim(win, text=u'練習 → 2', height=80, bold=True, pos=(0, 0)).draw()
	visual.TextStim(win, text=u'本番 → 3', height=80, bold=True, pos=(0, -200)).draw()
	win.flip()

	sound_namedtuple.confirmation.play()

if __name__ == "__main__":
	
	instruction(win)
	win.flip()
	sound_namedtuple.finish_instruction.play()
	core.wait(sound_namedtuple.finish_instruction.duration)

	visual.TextStim(win, text=u'練習', height=80, bold=True).draw()
	win.flip()
	sound_namedtuple.into_demo.play()
	core.wait(sound_namedtuple.into_demo.duration)

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