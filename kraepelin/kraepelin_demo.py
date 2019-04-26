from psychopy import visual, core, event, sound
import random
import numpy as np
import itertools
import math
from kraepelin_components import MatrixStim

x = y = np.array([-50, 0, 50])

def arrangement(text, num, position, posList):
	text_view.setText(text)

	matrix = list(itertools.product(x+position, y))
	
	for i in range(num):
		text_view.setPos(matrix[posList[i]])
		text_view.draw()


#parameter
trial_duration = 5
trial_length = 2
stim_length = 50


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
fixation = visual.ShapeStim(
    win, vertices=((-30, 0), (30, 0), (0, 0), (0, -30), (0, 30), (0, 0)))
count_fixation = visual.TextStim(win, pos=(0, 0), height=80, bold=True)

text_view = visual.TextStim(win, height=50)


#define components for demo
msg_wait = visual.TextStim(win, text='Wait...', height=80, bold=True)
msg_start = visual.TextStim(win, text='Start!', height=80, bold=True)
msg_finish = visual.TextStim(win, text='Finish!', height=80, bold=True)
answer = visual.TextStim(win, pos=(0, -100), height=80, bold=True)
count_fixation = visual.TextStim(win, pos=(0, 0), height=80, bold=True)
matrix_shape = (3, 3)
matrixstim_left = MatrixStim(win, matrix_shape, (50, 50), (-200, 0), height=50)
matrixstim_right = MatrixStim(win, matrix_shape, (50, 50), (200, 0), height=50)
def generate_matrix(counts_of_number, number):
	position = np.random.permutation(np.arange(matrix_shape[0]*matrix_shape[1])).reshape(matrix_shape)
	return np.where(position < counts_of_number, str(number), "")

conf_inst = visual.TextStim(win, text='instruction → １', height=80, bold=True, pos=(0, 200))
conf_demo = visual.TextStim(win, text='demonstration → ２', height=80, bold=True, pos=(0, 0))
conf_pro = visual.TextStim(win, text='exit → ３', height=80, bold=True, pos=(0, -200))


#defined sounds
introduction = sound.Sound('sounds/introduction.wav')
inst_progress = sound.Sound('sounds/inst_progress.wav')
firstblock = sound.Sound('sounds/firstblock.wav')
secondblock = sound.Sound('sounds/secondblock.wav')
into_demo = sound.Sound('sounds/into_demo.wav')
start_demo = sound.Sound('sounds/start_demo.wav')
finish_demo = sound.Sound('sounds/finish_demo.wav')
confirmation = sound.Sound('sounds/confirmation.wav')
inst_fixa = sound.Sound('sounds/inst_fixa.wav')


clock = core.Clock()


#instruction start---------------------------------------------------------------------
def instruction():
	msg_inst.setText("task instruction")
	msg_inst.draw()
	win.flip()

	introduction.play()

	core.wait(8)

	#1st block-----------------------------------------------------------------------------

	count_fixation.setText("0")
	count_fixation.draw()
	win.flip()

	inst_progress.play()

	core.wait(4)

	empha_rect.setPos((0,0))
	empha_rect.draw()
	count_fixation.draw()
	win.flip()

	core.wait(15)

	count_fixation.draw()
	win.flip()

	core.wait(4)

	count_fixation.draw()
	empha_rect.setPos((-200,0))
	empha_rect.draw()
	empha_rect.setPos((200,0))
	empha_rect.draw()
	win.flip()

	core.wait(8)

	pos_left = random.sample(range(9), k=4)
	pos_right = random.sample(range(9), k=3)
	arrangement(6, 4, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	win.flip()

	core.wait(0.2)

	fixation.draw()
	win.flip()

	core.wait(1)

	firstblock.play()

	core.wait(4)

	arrangement(6, 4, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	empha_rect.setPos((-200, 0))
	empha_rect.draw()
	win.flip()

	core.wait(4)

	arrangement(6, 4, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	empha_rect.setPos((200, 0))
	empha_rect.draw()
	win.flip()

	core.wait(4)

	arrangement(6, 4, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	win.flip()

	core.wait(12)

	arrangement(6, 4, -200, pos_left)
	arrangement(8, 3, 200, pos_right)
	demo_ans.setText("7")
	demo_ans.draw()
	win.flip()

	core.wait(8)


	#2nd block-----------------------------------------------------------------------------

	count_fixation.setText("1")
	count_fixation.draw()
	empha_rect.setAutoDraw(False)
	win.flip()

	core.wait(8)

	pos_left = random.sample(range(9), k=8)
	pos_right = random.sample(range(9), k=5)
	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	win.flip()

	core.wait(0.2)

	fixation.draw()
	win.flip()

	core.wait(1)

	secondblock.play()

	core.wait(2)

	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	empha_rect.setPos((-200, 0))
	empha_rect.draw()
	win.flip()

	core.wait(4)

	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	empha_rect.setPos((200, 0))
	empha_rect.draw()
	win.flip()

	core.wait(4)

	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	win.flip()

	core.wait(9)

	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_ans.setText("13")
	demo_ans.draw()
	win.flip()

	core.wait(6)

	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_ans.draw()
	allow.draw()
	win.flip()

	core.wait(2)

	arrangement(4, 8, -200, pos_left)
	arrangement(1, 5, 200, pos_right)
	demo_cor_ans.setText("3")
	demo_ans.draw()
	allow.draw()
	demo_cor_ans.draw()
	win.flip()

	core.wait(3)

	inst_fixa.play()

	fixation.draw()
	win.flip()

	core.wait(11)


#start demo---------------------------------------------------------------------------
def demo():
	msg_wait.draw()
	win.flip()

	start_demo.play()

	core.wait(2)

	msg_start.draw()
	win.flip()

	core.wait(2)

	for trials in range(trial_length):
		pre_number = [random.randint(1, 9), random.randint(1, 9)]
		pre_stimulus = generate_matrix(pre_number[0], pre_number[1])

		rt_list = []
		correct = 0
		task_start = clock.getTime()

		for counter in range(stim_length):
			# display fixation
			count_fixation.setText(counter)
			count_fixation.draw()
			win.flip()
			core.wait(1)

			#display numbers
			new_number = [random.randint(1, 9), random.randint(1, 9)]
			new_stimulus = generate_matrix(new_number[0], new_number[1])
			matrixstim_left.set_matrix(pre_stimulus)
			matrixstim_right.set_matrix(new_stimulus)
			win.flip()
			core.wait(0.2)

			fixation.draw()
			win.flip()

			#enter keys and measure response time
			key_start = clock.getTime()
			task_time = clock.getTime() - task_start
			keys = event.waitKeys(
				maxWait=trial_duration-task_time,
				keyList=['num_0','num_1','num_2','num_3','num_4',
					'num_5','num_6','num_7','num_8','num_9','escape'])
			if keys == None:
				break
			elif keys == 'escape' :
				win.close()
			
			key_end = clock.getTime()

			rt = key_end - key_start
			rt_list.append(rt)

			#display after answered
			answer.setText(keys[0][4])
			answer.draw()
			win.flip()

			pre_number = new_number
			pre_stimulus = new_stimulus

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

#main--------------------------------------------------------------------------------
instruction()

win.flip()

into_demo.play()

core.wait(7)

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