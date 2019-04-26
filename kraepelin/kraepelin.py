from psychopy import visual, core, event
import random
import csv
import numpy as np
import itertools
import math
import numpy

from kraepelin_components import MatrixStim

#parameter
trial_duration = 60
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
count_fixation = visual.TextStim(win, pos=(0, 0), height=80, bold=True)


#matrix-like stimulus
matrix_shape = (3, 3)
matrixstim_left = MatrixStim(win, matrix_shape, (50, 50), (-200, 0), height=50)
matrixstim_right = MatrixStim(win, matrix_shape, (50, 50), (200, 0), height=50)
def generate_matrix(counts_of_number, number):
	position = numpy.random.permutation(numpy.arange(matrix_shape[0]*matrix_shape[1])).reshape(matrix_shape)
	return numpy.where(position < counts_of_number, str(number), "")

clock = core.Clock()

msg_wait.draw()
win.flip()
event.waitKeys(keyList=['space'])

msg_start.draw()
win.flip()

core.wait(2)

key_list=['0','1','2','3','4','5','6','7','8','9','escape']

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
		win.flip()

		#enter keys and measure response time
		key_start = clock.getTime()
		task_time = clock.getTime() - task_start
		keys = event.waitKeys(
			maxWait=trial_duration-task_time,
			keyList=key_list
		)

		if keys == None:
			break
		elif keys == 'escape' :
			win.close()
		
		key_end = clock.getTime()

		rt = key_end - key_start
		rt_list.append(rt)

		answer_number = key_list.index(keys[0])

		#display after answered

		answer.setText(answer_number)
		answer.draw()
		win.flip()

		#check the answer
		cor_answer = (pre_number[0] + new_number[0]) % 10
		if answer_number == cor_answer:
			correct += 1

		pre_number = new_number
		pre_stimulus = new_stimulus

		core.wait(0.2)

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