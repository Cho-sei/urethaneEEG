from psychopy import visual, core, event

win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

allow = visual.ShapeStim(
	win, vertices=((-15,0),(-15,30),(15,30),(15,0),(30,0),(0,-30),(-30,0)),
	pos=(0,-100), lineColor='red', lineWidth=5)

allow.draw()
win.flip()

event.waitKeys(keyList=['space'])