from psychopy import visual,core,event
import pandas as pd
import itertools
import numpy as np
import sys

SUBJECT_ID = sys.argv[1]  # 被験者番号をコマンドライン引数で指定

#データフレーム作成

conditions = list(itertools.product(
	range(1),
	(60, 120, 180, 240, 300),
	('b', 'd', '〇'),
))

df = pd.DataFrame(
	conditions, columns=('block', 'rotation', 'character'))
df = df.sample(frac=1)
df.sort_values('block', inplace=True)
df.reset_index(drop=True, inplace=True)
df['resp'] = ''
df['RT'] = 0

#刺激作成

win = visual.Window(units='pix', fullscr=True, allowGUI=False)
msg_ready = visual.TextStim(win, 'Ready', height=80)
msg_finish = visual.TextStim(win, 'Finish!', height=80)
fixation = visual.ShapeStim(
	win, vertices=((-30, 0), (30, 0), (0, 0), (0, -30), (0, 30), (0, 0)))
target = visual.TextStim(win, height=80, bold=True)

clock = core.Clock()

msg_ready.draw()
win.flip()
keys = event.waitKeys(keyList=['space'])

#刺激呈示

for i, row in df.iterrows():
	target.setText(row['character'])
	target.setOri(row['rotation'])

	fixation.setOpacity(1.0)
	fixation.draw()
	win.flip()

	core.wait(1.5)

	fixation.setOpacity(0.0)
	win.flip()

	core.wait(np.random.random() / 2 + 0.5)  # 0.5 ~ 1秒

	target.draw()
	win.flip()

	t_start = clock.getTime()
	keys = event.waitKeys(maxWait=3, keyList=['left', 'right', 'escape'])
	if keys == None:
		continue
	elif 'escape' in keys:
		break
	t_end = clock.getTime()

	resp = keys[0]
	rt = t_end - t_start

	df.loc[i, ['resp', 'RT']] = (resp, rt)

msg_finish.draw()
win.flip()
core.wait(2)

df.to_csv('output_{}.csv'.format(SUBJECT_ID), encoding='shift-jis')
win.close()