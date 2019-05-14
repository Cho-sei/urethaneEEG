from psychopy import visual, core, event, gui

win = visual.Window(size=(1920, 1080), units='pix', fullscr=True, allowGUI=False)

output_num = visual.TextStim(win, height=80, bold=True)

dlg = gui.Dlg(title=u'回答')
dlg.addField('answer:','')

core.wait(3)

win.setMouseVisible(True)
win.flip()

dlg.show()

output_num.setText(dlg.data[0])
output_num.draw()
win.flip()

core.wait(3)