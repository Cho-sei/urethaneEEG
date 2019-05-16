from psychopy import core, visual

ratingscale_keynames = ['name', 'rating', 'response_time', 'history']

def control_ratingscale(win, ratingscale, stimuli_list, test_name, last_showtime=0.5):
    while ratingscale.noResponse:
        for stimulus in stimuli_list + [ratingscale]:
            stimulus.draw()
        win.flip()
    #show the question is over
    for stimulus in stimuli_list + [ratingscale]:
        stimulus.draw()
    win.flip()
    core.wait(last_showtime)

    return dict(zip(
        ratingscale_fieldnames,
        [test_name, ratingscale.getRating(), ratingscale.getRT(), ratingscale.getHistory()]
    ))

def fatigue_visualanalogscale(win):
    return control_ratingscale(
        win,
        visual.RatingScale(
            win,
            low=0, high=1, precision=1000,#return value from 0 to 1 in 0.01 ticks
            labels=[None, None],#no tick labels
            showValue=False,#do not show the value selected now on the button
            skipKeys=None,#do not allow to skip answering
            tickMarks=[None, None],
            tickHeight=2,
            pos=(0,-250),
        ),
        [
            visual.ImageStim(win, 'imgs/inst_FVAS.png'),
            visual.ImageStim(win, 'imgs/VAS_left.png', pos=(-500, -250)),
            visual.ImageStim(win, 'imgs/VAS_right.png', pos=(500, -250)),
        ],
        'fatigue visual analog scale'
    )

def karolinska_sleepinessscale(win):
    return control_ratingscale(
        win,
        visual.RatingScale(
            win,
            low=1, high=9,#return value from 1 to 9 in 1 ticks
            showValue=False,#do not show the value selected now on the button
            skipKeys=None,#do not allow to skip answering
            tickMarks=list(range(1,10)),
            pos=(0,-350),
        ),
        [
            visual.ImageStim(win, 'imgs/inst_KASS.png')
        ],
        'karolinska sleepiness scale'
    )

if __name__ == "__main__":
    import sys
    from psychopy import event

    from kraepelin_stimuli import KraepelinWindow
    #set global escape
    event.globalKeys.add(key='escape', func=sys.exit)

    #window defined
    win = KraepelinWindow(units='pix', fullscr=True, allowGUI=False)

    print(fatigue_visualanalogscale(win))
    print(karolinska_sleepinessscale(win))