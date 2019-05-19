from psychopy import core, visual, event

def dialog_alternative(kraepelin_window):
    display_text = visual.TextStim(win, pos=(0, 0), bold=True)
    display_text.setText("")
    cursor_rect = visual.Rect(win, width=20, height=80)
    while True:
        #set cursor
        t = core.getTime()


        kraepelin_window.display_stimuli(
            [display_text],
            wait_time=0.1,
        )
       #get key & append | delete
        keys = event.getKeys(keyList=kraepelin_window.NUMKEY_NAME+kraepelin_window.ENTER_NAME+kraepelin_window.DELETE_NAME)
        if keys:#for debug
            print(*keys)
        for key in keys:
            if key in kraepelin_window.NUMKEY_NAME:
                display_text.text += str(kraepelin_window.NUMKEY_NAME.index(key))
            elif key in kraepelin_window.DELETE_NAME:
                display_text.text = display_text.text[:-1]
            elif key in kraepelin_window.ENTER_NAME:
                return int(display_text.text)


if __name__ == "__main__":
    import sys
    event.globalKeys.add(key='escape', func=sys.exit)

    from kraepelin_stimuli import KraepelinWindow
    win = KraepelinWindow(fullscr=True, units='pix')
    win.setMouseVisible(False)

    print(dialog_alternative(win))