from psychopy import visual, core, event

win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

Lcue = visual.Circle(win, radius=30, edges=64, pos=(-200, 0), fillColor='white')
summary_text1 = visual.TextStim(win, " :  数字", bold=True, height=100, pos=(50,100))
summary_text2 = visual.TextStim(win, " :  個数", bold=True, height=100, pos=(50,-100))

Lcue.setPos((-150, 85))
Lcue.draw()
summary_text1.draw()
summary_text2.draw()

win.flip()

core.wait(5)


