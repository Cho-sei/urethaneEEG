from psychopy import visual, core, event
from psychopy.sound import Sound
import random

class urethene201812pretest(visual.Window):
    def __init__(self, *args, **keyargs):
        """
        stim_order : should be iterable
        """
        super().__init__(**keyargs)

        # load stimuli
        landolt_up = visual.GratingStim(self, tex='landolt_up.tif')
        landolt_down = visual.GratingStim(self, tex='landolt_down.tif')
        beep_low = Sound(1000, secs=.2, loops=2)
        beep_high = Sound(1020, secs=.2, loops=2)

        self.fixation = visual.GratingStim(self, tex='fixation.tif')
        self.visual_stimulus = [landolt_up, landolt_down, landolt_up, landolt_down]
        self.audio_stimulus = [beep_high, beep_low, beep_low, beep_high]

        # display "Wait..."
        wait_msg = visual.TextStim(self, "Wait...", color=(-1, -1, -1))#black letters
        wait_msg.draw(self)
        self.flip()

    def stimulus(self, stim_type):
        self.fixation.draw(self)
        self.flip()
        core.wait(1.5)

        self.flip()# show blank
        blank_time = random.choice([.8, .9, 1., 1.1, 1.2])
        core.wait(blank_time)

        self.visual_stimulus[stim_type].draw(self)
        self.audio_stimulus[stim_type].play()
        self.flip()
        core.wait(.2)#.play(blocking=True)
        self.audio_stimulus[stim_type].stop(reset=True)
        # need more wait ?

    def end(self):
        self.flip()
        core.wait(1.)
        
        end_msg = visual.TextStim(self, "End", color=(-1, -1, -1))
        end_msg.draw(self)
        self.flip()

if __name__ == '__main__':
    import sys
    import numpy
    stim_order = numpy.loadtxt(sys.argv[1], dtype=numpy.int16, delimiter=',')

    app = urethene201812pretest(stim_order, color=(1, 1, 1), fullscr=True)#white back

    event.waitKeys(keyList=['space'])

    for stim_type in stim_order:
        app.stimulus(stim_type)

    app.end()
    event.waitKeys(keyList=['space'])
