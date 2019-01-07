from psychopy import visual, core, event
import itertools
import pandas as pd
import numpy as np
import sys

SUBJECT_ID = sys.argv[1]  # 被験者番号をコマンドライン引数で指定

# データフレーム作成

conditions = list(itertools.product(
    range(4),  # 繰り返し回数
    (0.1, 0.2, 0.8),  # SOA
    ('valid', 'invalid', 'control'),  # 有効性
    ('left', 'right'),  # ターゲットの呈示位置
))
catch_conditions = list(itertools.product(  #catch試行のためのリスト
    range(4),
    [0],
    ('valid', 'invalid', 'control'),
    ['catch'],
))

conditions.extend(catch_conditions)

df = pd.DataFrame(
    conditions, columns=('block', 'soa', 'validity', 'target_pos'))
df = df.sample(frac=1)
df.sort_values('block', inplace=True)
df.reset_index(drop=True, inplace=True)
df['resp'] = ''
df['RT'] = 0

# 刺激作成

# fullscr=Trueの場合はフルスクリーン呈示になる
# allowGUI=Falseの場合はマウスカーソルが消える
win = visual.Window(units='pix', fullscr=True, allowGUI=False)
msg_ready = visual.TextStim(win, 'Ready', height=80)
msg_finish = visual.TextStim(win, 'Finish!', height=80)
fixation = visual.ShapeStim(
    win, vertices=((-30, 0), (30, 0), (0, 0), (0, -30), (0, 30), (0, 0)))

left_cue = visual.ShapeStim(
    win, vertices=((-80, -80), (-80, 80), (80, 80), (80, -80)),
    pos=(-200, 0), lineWidth=10)
right_cue = visual.ShapeStim(
    win, vertices=((-80, -80), (-80, 80), (80, 80), (80, -80)),
    pos=(200, 0), lineWidth=10)
neutral_cue = visual.ShapeStim(
    win, vertices=((-280, -80), (-280, 80), (280, 80), (280, -80)),
    pos=(0, 0), lineWidth=10)

target = visual.ShapeStim(
    win, vertices=((-60, -60), (-60, 60), (60, 60), (60, -60)),
    fillColor='black', lineColor='black')

clock = core.Clock()

msg_ready.draw()
win.flip()
keys = event.waitKeys(keyList=['space'])

# 刺激呈示

for i, row in df.iterrows():
    if row['target_pos'] == 'left':
        target.setOpacity(1.0)
        target.setPos((-200, 0))
        if row['validity'] == 'valid':
            cue = left_cue
        elif row['validity'] == 'invalid':
            cue = right_cue
        elif row['validity'] == 'control':
            cue = neutral_cue
    elif row['target_pos'] == 'right':
        target.setOpacity(1.0)
        target.setPos((200, 0))
        if row['validity'] == 'valid':
            cue = right_cue
        elif row['validity'] == 'invalid':
            cue = left_cue
        elif row['validity'] == 'control':
            cue = neutral_cue
    else:
        target.setOpacity(0.0)
        if row['validity'] == 'valid':
            cue = right_cue
        elif row['validity'] == 'invalid':
            cue = left_cue
        elif row['validity'] == 'control':
            cue = neutral_cue

    fixation.draw()
    win.flip()

    core.wait(np.random.random() / 2 + 0.5)  # 0.5 ~ 1秒

    fixation.draw()
    cue.draw()
    win.flip()

    core.wait(0.05)
    fixation.draw()
    win.flip()

    core.wait(1 + row['soa'])

    fixation.draw()
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
#keys = event.waitKeys(keyList=['space'])

df.to_csv('output_{}.csv'.format(SUBJECT_ID), encoding='utf-8')
win.close()