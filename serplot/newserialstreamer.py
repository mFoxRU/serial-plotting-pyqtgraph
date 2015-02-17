__author__ = 'mFoxRU'

from serialstreamer import SerialStreamer


class NewSerialStreamer(SerialStreamer):
    def __init__(self, port, speed=115200, channels=6, lim=600,
                 start_bytes='ffffff'):
        SerialStreamer.__init__(self, port, speed, channels, lim, start_bytes)

    def add_data_piece(self, chan, data, state=None):
        with self._locker:
            self._data[chan].add(data)
            self._data[chan].state = state

    def _loop(self):
        raw = ''
        min_size = len(self._start_bytes) + 8
        while 1:
            raw += self._read_port()
            while len(raw) >= min_size:
                if raw.startswith(self._start_bytes):
                    channel = int(raw[6:8], base=16)
                    state = bool(int(raw[8:10], base=16))
                    value = int(raw[12:14] + raw[10:12], base=16)
                    self.add_data_piece(channel, value, state)
                    raw = raw[min_size:]
                else:
                    raw = raw[2:]