from psychopy import core, visual

def control_ratingscale(ratingscale, question_explainstim, last_showtime=0.5):
    while ratingscale.noResponse:
        question_explainstim.draw()
        ratingscale.draw()
        win.flip()
    #show the question is over
    question_explainstim.draw()
    ratingscale.draw()
    win.flip()
    core.wait(last_showtime)

    return dict(
        rating=ratingscale.getRating(),
        response_time=ratingscale.getRT(),
        histories=ratingscale.getHistory()
    )

if __name__ == "__main__":
    import sys
    from psychopy import event
    #set global escape
    event.globalKeys.add(key='escape', func=sys.exit)

    #window defined
    win = visual.Window(units='pix', fullscr=True, allowGUI=False)

    fatigue_ratingscale = visual.RatingScale(
        win,
        low=0, high=1, precision=100,#return value from 0 to 1 in 0.01 ticks
        labels=[None, None],#no tick labels
        showValue=False,#do not show the value selected now on the button
        skipKeys=None,#do not allow to skip answering
        tickHeight=2,
        pos=(0,-350),
    )

    sleepiness_ratingscale = visual.RatingScale(
        win,
        low=1, high=9,#return value from 1 to 9 in 1 ticks
        showValue=False,#do not show the value selected now on the button
        skipKeys=None,#do not allow to skip answering
        pos=(0,-350),
    )

#    test_textstim = visual.TextBox(window=win, text="test", size=(100,100))#, text="lorem ipsum", pos=(0, 100))#, height=80)
    test_textstim = visual.TextBox(win,
                            text="This is your text",
                            font_size=21,
                            font_color=[-1,-1,1], 
                            size=(1,.3),
                            pos=(0.0,0.25), 
                            grid_horz_justification='center',
                            units='norm',)
    test_textstim2 = visual.TextBox(win,
                            text="This is not your text",
                            font_size=21,
                            font_color=[-1,-1,1], 
                            size=(1,.3),
                            pos=(0.0,0.25), 
                            grid_horz_justification='center',
                            units='norm',)
    kss_textstim = visual.TextBox(
        win,
        pos=(0., .25), size=(1., .3),
        font_size=21, font_color=[-1, -1, 1],
        grid_horz_justification='left', grid_vert_justification='left',
        align_horz='left', align_vert='left',
        units='norm',
        text="1   Extremely alert\r\n2   Very alart\r\n3   Alert\r\n4   Fairly alert\r\n5   Neither alert nor sleepy\r\n6   Some signs of sleepiness\r\n7   Sleepy, but no effort to keep alert\r\n8   Sleepy, some effort to keep alert\r\n9   Very sleepy, great effort to keep alert, fighting sleep"
    )

    print(control_ratingscale(fatigue_ratingscale, test_textstim))
    print(control_ratingscale(sleepiness_ratingscale, kss_textstim))