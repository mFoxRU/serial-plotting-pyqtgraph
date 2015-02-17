__author__ = 'mFoxRU'

import abc
import thread

import numpy as np


class LimData(object):
    def __init__(self, lim, dtype=float):
        self.limit = lim
        self.counter = 0
        self.state = None
        self._data = np.zeros(self.limit, dtype=dtype)

    def add(self, new_data):
        if self.counter < self.limit:
            self._data[self.counter] = new_data
            self.counter += 1
        else:
            self._data = np.roll(self._data, -1)
            self._data[-1] = new_data

    @property
    def data(self):
        if self.counter >= self.limit:
            return self._data
        else:
            return self._data[:self.counter]

    def sma(self, n):
        if n > self.counter:
            return []
        w = np.repeat(1., n) / n
        sma = np.convolve(self._data[:self.counter], w, mode='valid')
        return sma


class AbstractStreamer(object):
    def __init__(self, channels=6, lim=600, *args, **kwargs):
        self._lim = lim
        self._channels = channels
        self._data = [LimData(lim, dtype=int) for _ in xrange(channels)]
        self._locker = thread.allocate_lock()

    @property
    def data(self):
        with self._locker:
            return (d.data for d in self._data)

    def sma(self, n):
        with self._locker:
            return (d.sma(n) for d in self._data)

    @property
    def state(self):
        with self._locker:
            return (d.state for d in self._data)

    def add_data(self, data):
        with self._locker:
            for n, d in enumerate(data):
                self._data[n].add(d)

    def start(self):
        thread.start_new_thread(self._loop, ())

    @abc.abstractmethod
    def _loop(self, *args, **kwargs):
        pass