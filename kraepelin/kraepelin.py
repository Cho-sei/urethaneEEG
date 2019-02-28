from psychopy import visual, core, event
import random
import csv
import numpy as np
import itertools

x = y = np.array([-50, 0, 50])

def arrangement(text, num, position):
	text_view = visual.TextStim(win, height=50)
	text_view.setText(text)

	matrix = list(itertools.product(x+position, y))
	
	for i in range(num):
		text_view.setPos(matrix[i])
		text_view.draw()

#parameter
trial_duration = 5
trial_length = 2
stim_length = 50

#file defined
res_columns = ['trials', 'all', 'accuracy', 'RT']

with open('result.csv', 'w') as file:
	writer = csv.writer(file, lineterminator='\n')
	writer.writerow(res_columns)

#window defined
win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

#visual text
msg_wait = visual.TextStim(win, text='Wait...', height=80, bold=True)
msg_start = visual.TextStim(win, text='Start!', height=80, bold=True)
msg_finish = visual.TextStim(win, text='Finish!', height=80, bold=True)
answer = visual.TextStim(win, pos=(0, -100), height=80, bold=True)

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

msg_wait.draw()
win.flip()
event.waitKeys(keyList=['space'])

msg_start.draw()
win.flip()

core.wait(2)

for trials in range(trial_length):
	pre_number = [random.randint(1, 9), random.randint(1, 9)]

	rt_list = []
	correct = 0
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
		arrangement(pre_number[0], pre_number[1], -200)
		arrangement(new_number[0], new_number[1], 200)
		answer.setText(keys[0][4])
		answer.draw()
		max_bar.draw()
		progress_bar.draw()
		pre_progress.draw()
		win.flip()

		#check the answer
		cor_answer = (pre_number[1] + new_number[1]) % 10
		if keys[0][4] == str(cor_answer):
			correct += 1

		pre_number = new_number

		core.wait(0.2)

	pre_progress_number = len(rt_list)

	if len(rt_list) == 0:
		result = [trials+1, 0, 0]
	else:
		result = [trials+1, len(rt_list), correct/len(rt_list)]
		result.extend(rt_list)
	
	with open('result.csv','a') as file:
		writer = csv.writer(file, lineterminator='\n')
		writer.writerow(result)

msg_finish.draw()
win.flip()
event.waitKeys(keyList=['space'])