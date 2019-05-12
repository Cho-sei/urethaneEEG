from psychopy import visual

if __name__ == "__main__":
    win = visual.Window()
    rating_scale = visual.RatingScale(
        win,
        low=1, high=5,
        #choises=['not at all tired', 'extremely tired'],
        scale=None, tickHeight=1, tickMarks=[1, 5],
        markerStart=1,
        acceptPreText='set position', acceptText='press Enter', showValue=False,
        skipKeys=None, noMouse=True,
#       flipVert=True,
    )

    while rating_scale.noResponse:
        rating_scale.draw()
        win.flip()

    visual_analog_scale = visual.Slider(win, ticks=(1,1000))
    while not visual_analog_scale.getRating():
        visual_analog_scale.draw()
        win.flip()
    print(visual_analog_scale.getRating())