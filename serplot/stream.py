__author__ = 'mFoxRU'

import numpy as np


class Data(object):
    def __init__(self, lim, dtype=float):
        self.limit = lim
        self.counter = 0
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
