__author__ = 'mFoxRU'

import sys
import _winreg as reg
import itertools as it

from PyQt4 import QtGui, QtCore
import serial
import pyqtgraph as pg
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

from mainwindow import Ui_MainWindow
from fakestreamer import FakeStreamer
from serialstreamer import SerialStreamer
from newserialstreamer import NewSerialStreamer


class GuiApp(QtGui.QMainWindow):
    title_template = '<font color="{}">Channel {}</font>'
    protocols = {'Serial Protocol 1': SerialStreamer,
                 'Serial Protocol 2': NewSerialStreamer}
    title_colors = {None:   '#000000',
                    0:      '#FF0000',
                    1:      '#00FF00'}


    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = None
        self.stream = None
        self.filtering = False
        self.ui.w_box_plotting_control.setEnabled(False)
        # Add sources
        self.ui.w_port.addItem('Emulate')
        for port in self._serial_ports():
            self.ui.w_port.addItem(port)
        # Connects
        self.ui.w_connect.clicked.connect(self._try_to_connect)
        self.ui.w_filter_none.toggled.connect(self._no_filter)
        self.ui.w_button_autozoom.toggled.connect(
            self._autozoom_button_pressed)
        self.ui.w_button_pause.toggled.connect(self._pause_button_pressed)
        # Mix
        self.plots = []

    def hide_release(self):
        # For special release
        self.ui.w_channels.setValue(6)
        self.ui.w_channels.setVisible(False)
        self.ui.w_protocol.setVisible(False)

    def _try_to_connect(self):
        port = str(self.ui.w_port.currentText())
        # # Disable interface
        self.ui.w_box_source.setEnabled(False)
        # Using fake source?
        if port == 'Emulate':
            self._start(None)
            return
        # Check port availability
        try:
            ser = serial.Serial(port)
        except serial.SerialException as e:
            QtGui.QMessageBox.critical(self, 'Error', e.message,
                                       QtGui.QMessageBox.Ok)
            # Re-enable interface
            self.ui.w_box_source.setEnabled(True)
        else:
            ser.close()
            self._start(port)

    @QtCore.pyqtSlot(bool)
    def _no_filter(self, state):
        self.filtering = not state
        self.ui.w_filter_window.setEnabled(not state)

    @QtCore.pyqtSlot(bool)
    def _pause_button_pressed(self, state):
        if state:
            self.ui.w_button_pause.setText('Resume')
            if self.timer is not None:
                self.timer.stop()
        else:
            self.ui.w_button_pause.setText('Pause')
            if self.timer is not None:
                self.timer.start()

    @QtCore.pyqtSlot(bool)
    def _autozoom_button_pressed(self, state):
        for plot in self.plots:
            plot.enableAutoRange(axis=pg.ViewBox.YAxis, enable=state)

    def _start(self, port):
        self.ui.w_box_plotting_control.setEnabled(True)
        # Prepare for plots placing
        channels = self.ui.w_channels.value()
        matrix = (1, 3) if channels <= 3 else (2, 3)
        coordinates = it.izip(
            xrange(channels),
            it.product(xrange(matrix[0]), xrange(matrix[1]))
        )
        # Create grid
        grid = QtGui.QGridLayout()
        self.ui.w_box_plot.setLayout(grid)
        # Initialize streamer
        if port is None:
            cls = FakeStreamer
        else:
            cls = self.protocols[str(self.ui.w_protocol.currentText())]
        self.stream = cls(channels=channels, lim=600, port=port)
        self.stream.start()
        # Create plots
        for ch, (y, x) in coordinates:
            widget = pg.PlotWidget(self, title=self.title_template.format(
                '#000000', ch + 1),)
            grid.addWidget(widget, x, y)
            plot = widget.getPlotItem()
            self.plots.append(plot)
            plot.enableAutoRange(axis=pg.ViewBox.YAxis, enable=True)
            plot.enableAutoRange(axis=pg.ViewBox.XAxis, enable=False)
            view = plot.getViewBox()
            view.setXRange(0, 600, padding=0.01)
            view.setMouseEnabled(x=False, y=True)
            plot.plot()
        # Setup update
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self._update_plots)
        self.timer.start()

    @QtCore.pyqtSlot()
    def _update_plots(self):
        n = int(self.ui.w_filter_window.value())
        if self.filtering:
            stream = self.stream.sma(n)
        else:
            stream = self.stream.data

        # Update data
        for plot, data in it.izip(self.plots, stream):
            dataitem = plot.listDataItems()[0]
            dataitem.setData(data)

        # Update plot titles
        for ch, (pl, st) in enumerate(it.izip(self.plots, self.stream.state)):
            pl.setTitle(
                self.title_template.format(self.title_colors[st], ch + 1))

    @staticmethod
    def _serial_ports():
        try:
            key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,
                              r'HARDWARE\DEVICEMAP\SERIALCOMM')
        except WindowsError as e:
            print e
        else:
            for n in it.count():
                try:
                    port = reg.EnumValue(key, n)
                    yield str(port[1])
                except EnvironmentError:
                    break


def main(argv=None):
    if argv is None:
        argv = sys.argv
    app = QtGui.QApplication(argv)
    gui = GuiApp()
    if not 'godmode' in argv:
        gui.hide_release()
    gui.show()
    app.exec_()


if __name__ == '__main__':
    main()
