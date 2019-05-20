import collections
from psychopy import sound

SoundNamedTuple = collections.namedtuple('SoundNamedTuple', [
	'into_subtract_1000', 'into_subtract_1012', 'into_subtract_1007', 'into_subtract_1004', 'into_EOresting', 'into_ECresting', 'finish_resting', 'answer_of_subtraction'])
sound_namedtuple = SoundNamedTuple(**{soundname:sound.Sound('sounds/'+soundname+'.wav') for soundname in SoundNamedTuple._fields})

print(sound_namedtuple[1].duration)