__author__ = 'mFoxRU'

import math
from time import sleep
from itertools import count

from abstractstreamer import AbstractStreamer


class FakeStreamer(AbstractStreamer):
    def __init__(self, channels=6, lim=600, delay=.1,
                 fn=lambda x: 128 * (1 + math.sin(x * 0.1)), *args, **kwargs):
        AbstractStreamer.__init__(self, channels, lim)
        self._fn = fn
        self._delay = delay

    def _loop(self, *args, **kwargs):
        for i in count():
            self.add_data(
                [self._fn(i) for _ in xrange(self._channels)]
            )
            sleep(self._delay)