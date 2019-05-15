from psychopy import visual, core, event, gui

win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

FVAS = visual.ImageStim(win, image='imgs/inst_FVAS.png', units='pix')

FVAS.draw()
win.flip()

event.waitKeys(keyList=['space'])