from psychopy import visual, core, event, sound
import random
import numpy as np
import itertools
import math
import sys

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
msg_inst = visual.TextStim(win, height=80, bold=True)
empha_rect = visual.Rect(win, width=200, height=200, lineColor='red', lineWidth=5)
demo_ans = visual.TextStim(win, pos=(0, -100), height=80, bold=True)
allow = visual.ShapeStim(
	win, vertices=((-15,0),(-15,30),(15,30),(15,0),(30,0),(0,-30),(-30,0)),
	pos=(0,-200), lineColor='white',fillColor='white')
demo_cor_ans = visual.TextStim(win, pos=(0, -300), height=80, bold=True)
fixation = get_fixation_stim(win)
count_fixation = visual.TextStim(win, pos=(0, 0), height=80, bold=True)

text_view = visual.TextStim(win, height=50)

summary_text1 = visual.TextStim(win, " V :  数字", bold=True, height=80, pos=(50,100))
summary_text2 = visual.TextStim(win, " N :  個数", bold=True, height=80, pos=(50,-100))


#define components for demo
msg_demo = visual.TextStim(win, text='demonstration', height=80, bold=True)
msg_wait = visual.TextStim(win, text='Wait...', height=80, bold=True)
msg_start = visual.TextStim(win, text='Start!', height=80, bold=True)
msg_finish = visual.TextStim(win, text='Finish!', height=80, bold=True)
answer = visual.TextStim(win, pos=(0, -100), height=80, bold=True)
count_fixation = visual.TextStim(win, pos=(0, 0), height=80, bold=True)
LRcue_dict = get_charcue_stim_dict(win)
matrixstim_left = KraepelinMatrixStim(win, (50, 50), (-200, 0), height=50)
matrixstim_right = KraepelinMatrixStim(win, (50, 50), (200, 0), height=50)

conf_inst = visual.TextStim(win, text='instruction → 1', height=80, bold=True, pos=(0, 200))
conf_demo = visual.TextStim(win, text='demonstration → 2', height=80, bold=True, pos=(0, 0))
conf_pro = visual.TextStim(win, text='exit → 3', height=80, bold=True, pos=(0, -200))


#defined sounds
introduction = sound.Sound('sounds/introduction.wav')
inst_calc = sound.Sound('sounds/inst_calc.wav')	#
inst_cue_num = sound.Sound('sounds/inst_cue_num.wav')
inst_progress = sound.Sound('sounds/inst_progress.wav')#
firstblock = sound.Sound('sounds/firstblock.wav')
inst_cue_value = sound.Sound('sounds/inst_cue_value.wav')
into_second =  sound.Sound('sounds/into_second.wav')
secondblock = sound.Sound('sounds/secondblock.wav')
into_demo = sound.Sound('sounds/into_demo.wav')
start_demo = sound.Sound('sounds/start_demo.wav')
finish_demo = sound.Sound('sounds/finish_demo.wav')
confirmation = sound.Sound('sounds/confirmation.wav')
inst_fixa = sound.Sound('sounds/inst_fixa.wav')
summary_cue = sound.Sound('sounds/summary_cue.wav')


clock = core.Clock()


#instruction start---------------------------------------------------------------------
def instruction():
	msg_inst.setText("task instruction")
	msg_inst.draw()
	win.flip()

	introduction.play()

	core.wait(8)

	fixation.draw()
	pos_left = random.sample(range(9), k=6)
	pos_right = random.sample(range(9), k=3)
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	win.flip()

	inst_calc.play()

	core.wait(35)

	#1st block-----------------------------------------------------------------------------

	count_fixation.setText("0")
	count_fixation.draw()
	win.flip()

	inst_progress.play()

	core.wait(5)

	empha_rect.setPos((0,0))
	empha_rect.draw()
	count_fixation.draw()
	win.flip()

	core.wait(16)

	count_fixation.draw()
	win.flip()

	core.wait(13)

	LRcue_dict[(True,False)].draw()
	win.flip()

	core.wait(0.5)

	win.flip()

	core.wait(0.5)

	inst_cue_num.play()

	core.wait(2)

	LRcue_dict[(True,False)].draw()
	win.flip()

	core.wait(41)

	fixation.draw()
	pos_left = random.sample(range(9), k=6)
	pos_right = random.sample(range(9), k=3)
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	win.flip()

	firstblock.play()

	core.wait(13) 

	fixation.draw()
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	empha_rect.setPos((-200, 0))
	empha_rect.draw()
	win.flip()

	core.wait(2)

	fixation.draw()
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	empha_rect.setPos((200, 0))
	empha_rect.draw()
	win.flip()

	core.wait(4)

	fixation.draw()
	arrangement(4, 6, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	demo_ans.setText("7")
	demo_ans.draw()
	win.flip()

	core.wait(3)

	win.flip()
	inst_cue_value.play()

	core.wait(4)

	LRcue_dict[(True,False)].draw()
	win.flip()

	core.wait(7)

	LRcue_dict[(False,True)].draw()
	win.flip()

	core.wait(5)
	
	LRcue_dict[(True,True)].draw()
	win.flip()

	core.wait(3)

	LRcue_dict[(False,False)].draw()
	win.flip()

	core.wait(13)


	#2nd block-----------------------------------------------------------------------------

	count_fixation.setText("1")
	count_fixation.draw()
	empha_rect.setAutoDraw(False)
	win.flip()

	into_second.play()

	core.wait(12)

	LRcue_dict[(False,False)].draw()
	win.flip()

	core.wait(0.5)

	win.flip()

	core.wait(0.5)

	fixation.draw()
	pos_left = random.sample(range(9), k=8)
	pos_right = random.sample(range(9), k=5)
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	win.flip()

	secondblock.play()

	core.wait(16)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	empha_rect.setPos((-200, 0))
	empha_rect.draw()
	win.flip()

	core.wait(3)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	empha_rect.setPos((200, 0))
	empha_rect.draw()
	win.flip()

	core.wait(4)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	win.flip()

	core.wait(3)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_ans.setText("13")
	demo_ans.draw()
	win.flip()

	core.wait(7)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_ans.draw()
	allow.draw()
	win.flip()

	core.wait(2)

	fixation.draw()
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_cor_ans.setText("3")
	demo_ans.draw()
	allow.draw()
	demo_cor_ans.draw()
	win.flip()

	core.wait(3)

	fixation.draw()
	win.flip()

	inst_fixa.play()

	core.wait(14)

#summary------------------------------------------------------------------------------
	summary_text1.draw()
	summary_text2.draw()

	win.flip()

	summary_cue.play()

	core.wait(17)

#start demo---------------------------------------------------------------------------
def demo():
	msg_wait.draw()
	win.flip()

	start_demo.play()

	core.wait(2)

	msg_start.draw()
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

	msg_finish.draw()
	win.flip()

	finish_demo.play()
	core.wait(4)

#confirmation------------------------------------------------------------------------
def display_confirmation():
	conf_inst.draw()
	conf_demo.draw()
	conf_pro.draw()
	win.flip()

	confirmation.play()

if __name__ == "__main__":
	
	instruction()

	win.flip()

	into_demo.play()

	core.wait(4)

	msg_demo.draw()
	win.flip()

	core.wait(15)

	demo()

	display_confirmation()

	while True:
		key = event.waitKeys(keyList=['1','2','3'])
		if  '1' in key:
			instruction()
		elif '2' in key:
			demo()
		else:
			break
		
		display_confirmation()

#--------------------------------------------------------
#
#	まとめスライド
#	Cueについて箇条書きor表にしてまとめ
#
#------------------------------------------------------