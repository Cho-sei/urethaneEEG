from psychopy import visual, core, event
import random
import csv
import numpy as np
import itertools
import sys

from kraepelin_components import MatrixStim

#set global escape
event.globalKeys.add(key='escape', func=sys.exit)

x = y = np.array([-50, 0, 50])

def arrangement(text, num, position, posList):
	text_view.setText(text)

	matrix = list(itertools.product(x+position, y))
	
	for i in range(num):
		text_view.setPos(matrix[posList[i]])
		text_view.draw()


#window defined
win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

#define components
msg_inst = visual.TextStim(win, height=80, bold=True)
empha_rect = visual.Rect(win, width=200, height=200, lineColor='red', lineWidth=5)
demo_ans = visual.TextStim(win, pos=(0, -100), height=80, bold=True)
allow = visual.ShapeStim(
	win, vertices=((-15,0),(-15,30),(15,30),(15,0),(30,0),(0,-30),(-30,0)),
	pos=(0,-200), lineColor='white',fillColor='white')
demo_cor_ans = visual.TextStim(win, pos=(0, -300), height=80, bold=True)
fixation = visual.ShapeStim(win,  vertices=((-30, 0), (30, 0), (0, 0), (0, -30), (0, 30), (0, 0)))
count_fixation = visual.TextStim(win, pos=(0, 0), height=80, bold=True)

text_view = visual.TextStim(win, height=50)



#instruction start
msg_inst.setText("課題説明")
msg_inst.draw()
win.flip()

event.waitKeys(keyList=['space'])

#1st block-----------------------------------------------------------------------------

count_fixation.setText("0")
count_fixation.draw()
win.flip()

event.waitKeys(keyList=['space'])

empha_rect.setPos((0,0))
empha_rect.draw()
count_fixation.draw()
win.flip()

event.waitKeys(keyList=['space'])

pos_left = random.sample(range(9), k=4)
pos_right = random.sample(range(9), k=3)
arrangement(6, 4, -200, pos_left)
arrangement(8, 3, 200, pos_right)
win.flip()

event.waitKeys(keyList=['space'])

fixation.draw()
win.flip()

event.waitKeys(keyList=['space'])

arrangement(6, 4, -200, pos_left)
arrangement(8, 3, 200, pos_right)
empha_rect.setPos((-200, 0))
empha_rect.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(6, 4, -200, pos_left)
arrangement(8, 3, 200, pos_right)
empha_rect.setPos((200, 0))
empha_rect.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(6, 4, -200, pos_left)
arrangement(8, 3, 200, pos_right)
demo_ans.setText("7")
demo_ans.draw()
win.flip()

event.waitKeys(keyList=['space'])


#2nd block-----------------------------------------------------------------------------

count_fixation.setText("1")
count_fixation.draw()
empha_rect.setAutoDraw(False)
win.flip()

event.waitKeys(keyList=['space'])

pos_left = random.sample(range(9), k=8)
pos_right = random.sample(range(9), k=5)
arrangement(4, 8, -200, pos_left)
arrangement(1, 5, 200, pos_right)
win.flip()

event.waitKeys(keyList=['space'])

fixation.draw()
win.flip()

event.waitKeys(keyList=['space'])

arrangement(4, 8, -200, pos_left)
arrangement(1, 5, 200, pos_right)
empha_rect.setPos((-200, 0))
empha_rect.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(4, 8, -200, pos_left)
arrangement(1, 5, 200, pos_right)
empha_rect.setPos((200, 0))
empha_rect.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(4, 8, -200, pos_left)
arrangement(1, 5, 200, pos_right)
demo_ans.setText("13")
demo_ans.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(4, 8, -200, pos_left)
arrangement(1, 5, 200, pos_right)
allow.setAutoDraw(True)
win.flip()

event.waitKeys(keyList=['space'])

arrangement(4, 8, -200, pos_left)
arrangement(1, 5, 200, pos_right)
demo_cor_ans.setText("3")
demo_cor_ans.draw()
win.flip()

event.waitKeys(keyList=['space'])


