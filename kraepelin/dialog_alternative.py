from psychopy import core, visual, event

def dialog_alternative(kraepelin_window, explain_stimuli=None, display_pos=(0, 0)):
    display_text = visual.TextStim(kraepelin_window, pos=display_pos, bold=True)
    display_text.setText("")
    while True:
       #get key & append | delete
        keys = event.getKeys(keyList=kraepelin_window.NUMKEY_NAME+kraepelin_window.ENTER_NAME+kraepelin_window.DELETE_NAME)
        if keys:#for debug
            print(*keys)
        for key in keys:
            if key in kraepelin_window.NUMKEY_NAME:
                display_text.text += str(kraepelin_window.NUMKEY_NAME.index(key))
            elif key in kraepelin_window.DELETE_NAME:
                display_text.text = display_text.text[:-1]
        if set(keys) & set(kraepelin_window.ENTER_NAME):#if keys has ENTER_NAME element
            return int(display_text.text)

        kraepelin_window.display_stimuli(
            [display_text]+(explain_stimuli if explain_stimuli is not None else []),
            wait_time=0.1,
        )


if __name__ == "__main__":
    import sys
    event.globalKeys.add(key='escape', func=sys.exit)

    from kraepelin_stimuli import KraepelinWindow
    win = KraepelinWindow(fullscr=True, units='pix')
    win.setMouseVisible(False)

    print(dialog_alternative(win, explain_stimuli=[visual.TextStim(win, "Input your answer & Press enter", pos=(0, 200))]))