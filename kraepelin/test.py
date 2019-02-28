from psychopy import visual, core, event

win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

text = visual.TextStim(win, height=50)

for i in range(5):
	keys = event.waitKeys()
	text.setText(keys[0][4])

	text.draw()
	win.flip()