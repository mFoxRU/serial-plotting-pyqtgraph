__author__ = 'mFoxRU'

from time import sleep
from itertools import izip

import serial

from abstractstreamer import AbstractStreamer


class SerialStreamer(AbstractStreamer):
    def __init__(self, port, speed=115200, channels=6, lim=600,
                 start_bytes='ffff'):
        AbstractStreamer.__init__(self, channels, lim)
        # Prepare serial
        self._start_bytes = start_bytes
        self.serial = serial.Serial()
        self.serial.setPort(port)
        self.serial.setBaudrate(speed)
        self.serial.setTimeout(0)
        self.serial.setRtsCts(1)

    def _read_port(self, force=False):
        while 1:
            try:
                if not self.serial.isOpen():
                    self.serial.open()
                new_raw = self.serial.readall().encode('hex')
            except Exception as e:
                if force:
                    self.serial.close()
                    sleep(0.1)
                else:
                    self.serial.close()
                    exit(e)
            else:
                return new_raw

    def _loop(self):
        raw = ''
        while 1:
            raw += self._read_port()
            while len(raw) >= 4 + self._lim * 2:
                if raw.startswith(self._start_bytes):
                    info_string = raw[4:4 + self._channels * 2]
                    info_bytes = [info_string[x * 2: x * 2 + 2]
                                  for x in xrange(self._channels)]
                    info_bytes.reverse()
                    with self._locker:
                        for data, new in izip(self._data, info_bytes):
                            data.add(int(new, base=16))
                    raw = raw[4 + self._channels * 2:]
                else:
                    raw = raw[2:]