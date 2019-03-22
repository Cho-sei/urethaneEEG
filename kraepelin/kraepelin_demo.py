from psychopy import visual, core, event
import random
import csv
import numpy as np
import itertools

x = y = np.array([-50, 0, 50])

def arrangement(text, num, position):
	text_view.setText(text)

	matrix = list(itertools.product(x+position, y))
	
	for i in range(num):
		text_view.setPos(matrix[i])
		text_view.draw()

#parameter
trial_duration = 60
trial_length = 2
stim_length = 50

#window defined
win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

#visual text
msg_inst = visual.TextStim(win, height=80, bold=True)
balloon = visual.ShapeStim(
	win, vertices=((0,0),(10,0),(15,10),(13,0),(20,0),(20,-10),(0,-10)))
empha_rect = visual.Rect(win, width=100, height=200, lineColor='red', lineWidth=5)
demo_ans = visual.TextStim(win, pos=(0, -100), height=80, bold=True)

msg_wait = visual.TextStim(win, text='Wait...', height=80, bold=True)
msg_start = visual.TextStim(win, text='Start!', height=80, bold=True)
msg_finish = visual.TextStim(win, text='Finish!', height=80, bold=True)
answer = visual.TextStim(win, pos=(0, -100), height=80, bold=True)

text_view = visual.TextStim(win, height=50)

#progress bar
max_bar = visual.ShapeStim(
    win, vertices=((-200, -10), (-200, 10), (200, 10), (200, -10)),
    pos=(0, 200), fillColor='#a9a9a9', lineColor='black', lineWidth=0.1)
progress_bar = visual.ShapeStim(
	win, pos=(0, 200), fillColor='#696969', lineColor='black', lineWidth=0.1)
pre_progress = visual.ShapeStim(
	win, vertices=((0, 10), (0, -10)), lineColor='black')

pre_progress_number = 0
single_progress = 400/stim_length

clock = core.Clock()

#instruction start
msg_inst.setText("課題説明")
msg_inst.draw()
win.flip()

event.waitKeys(keyList=['space'])

arrangement(6, 4, -200)
arrangement(8, 3, 200)
progress_bar.vertices = ((-200, -10), (-200, 10),(-100, 10), (-100, -10))
max_bar.draw()
progress_bar.draw()
pre_progress.setPos((60, 200))
pre_progress.draw()
max_bar.setAutoDraw(True)
progress_bar.setAutoDraw(True)
pre_progress.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(6, 4, -200)
arrangement(8, 3, 200)
empha_rect.setPos((-225, 0))
empha_rect.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(6, 4, -200)
arrangement(8, 3, 200)
empha_rect.setPos((175, 0))
empha_rect.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(6, 4, -200)
arrangement(8, 3, 200)
demo_ans.setText("7")
demo_ans.draw()
win.flip()

event.waitKeys(keyList=['space'])


"""

msg_wait.draw()
win.flip()
event.waitKeys(keyList=['space'])

msg_start.draw()
win.flip()

core.wait(2)

pre_number = [random.randint(1, 9), random.randint(1, 9)]

task_start = clock.getTime()

for counter in range(stim_length):
	new_number = [random.randint(1, 9), random.randint(1, 9)]
	#display numbers
	arrangement(pre_number[0], pre_number[1], -200)
	arrangement(new_number[0], new_number[1], 200)

	#display progress bar
	progress_bar.vertices = (
		(-200, -10), (-200, 10), 
		(counter*single_progress-199, 10), (counter*single_progress-199, -10))
	max_bar.draw()
	progress_bar.draw()
		
	pre_progress.setPos((pre_progress_number*single_progress-200, 200))
	pre_progress.draw()

	win.flip()

	#enter keys and measure response time
	task_time = clock.getTime() - task_start
	keys = event.waitKeys(
		maxWait=trial_duration-task_time,
		keyList=['num_0','num_1','num_2','num_3','num_4',
			'num_5','num_6','num_7','num_8','num_9','escape'])
	if keys == None:
		break
	elif keys == 'escape' :
		win.close()
		
	#display after answered
	arrangement(pre_number[0], pre_number[1], -200)
	arrangement(new_number[0], new_number[1], 200)
	answer.setText(keys[0][4])
	answer.draw()
	max_bar.draw()
	progress_bar.draw()
	pre_progress.draw()
	win.flip()

	pre_number = new_number

	core.wait(0.2)

pre_progress_number = len(rt_list)

msg_finish.draw()
win.flip()
event.waitKeys(keyList=['space'])
"""