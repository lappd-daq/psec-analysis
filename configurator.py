import sys
import numpy as np
from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os


###############################################################################
# ACDC Parsing Functions
#
#
#
def get_ped():
    boards = [[ui.Ped_0_1.value(), ui.Ped_0_2.value(), ui.Ped_0_3.value(), ui.Ped_0_4.value(), ui.Ped_0_5.value()],
        [ui.Ped_1_1.value(), ui.Ped_1_2.value(), ui.Ped_1_3.value(), ui.Ped_1_4.value(), ui.Ped_1_5.value()],
        [ui.Ped_2_1.value(), ui.Ped_2_2.value(), ui.Ped_2_3.value(), ui.Ped_2_4.value(), ui.Ped_2_5.value()],
        [ui.Ped_3_1.value(), ui.Ped_3_2.value(), ui.Ped_3_3.value(), ui.Ped_3_4.value(), ui.Ped_3_5.value()],
        [ui.Ped_4_1.value(), ui.Ped_4_2.value(), ui.Ped_4_3.value(), ui.Ped_4_4.value(), ui.Ped_4_5.value()],
        [ui.Ped_5_1.value(), ui.Ped_5_2.value(), ui.Ped_5_3.value(), ui.Ped_5_4.value(), ui.Ped_5_5.value()],
        [ui.Ped_6_1.value(), ui.Ped_6_2.value(), ui.Ped_6_3.value(), ui.Ped_6_4.value(), ui.Ped_6_5.value()],
        [ui.Ped_7_1.value(), ui.Ped_7_2.value(), ui.Ped_7_3.value(), ui.Ped_7_4.value(), ui.Ped_7_5.value()]]

    out = ''
    for board, values in enumerate(boards):
        for chip, value in enumerate(values):
            out += 'pedestal\t{}\t{}\t{}\n'.format(board, chip, value)
        out +='\n'
    return out

def get_thresh():
    boards = [[ui.thresh_0_1.value(), ui.thresh_0_2.value(), ui.thresh_0_3.value(), ui.thresh_0_4.value(), ui.thresh_0_5.value()],
        [ui.thresh_1_1.value(), ui.thresh_1_2.value(), ui.thresh_1_3.value(), ui.thresh_1_4.value(), ui.thresh_1_5.value()],
        [ui.thresh_2_1.value(), ui.thresh_2_2.value(), ui.thresh_2_3.value(), ui.thresh_2_4.value(), ui.thresh_2_5.value()],
        [ui.thresh_3_1.value(), ui.thresh_3_2.value(), ui.thresh_3_3.value(), ui.thresh_3_4.value(), ui.thresh_3_5.value()],
        [ui.thresh_4_1.value(), ui.thresh_4_2.value(), ui.thresh_4_3.value(), ui.thresh_4_4.value(), ui.thresh_4_5.value()],
        [ui.thresh_5_1.value(), ui.thresh_5_2.value(), ui.thresh_5_3.value(), ui.thresh_5_4.value(), ui.thresh_5_5.value()],
        [ui.thresh_6_1.value(), ui.thresh_6_2.value(), ui.thresh_6_3.value(), ui.thresh_6_4.value(), ui.thresh_6_5.value()],
        [ui.thresh_7_1.value(), ui.thresh_7_2.value(), ui.thresh_7_3.value(), ui.thresh_7_4.value(), ui.thresh_7_5.value()]]

    out = ''
    for board, values in enumerate(boards):
        for chip, value in enumerate(values):
            out += 'threshold\t{}\t{}\t{}\n'.format(board, chip, value)
        out +='\n'
    return out


def parse_acdc():
    filename, _ = QFileDialog.getSaveFileName(ui.export_acdc, 'Save File', os.getcwd())
    f = open(filename, 'w')
    f.write(get_ped())
    f.write(get_thresh())
    f.close()

###############################################################################
# trig Parsing Functions
#
#
#
"""
Will return a hex mask given an array of booleans for on/off masking of channels

Parameters:
    buttons- a boolean array ordered from channel 1 to channel 30

Note that the binary string represantation of the input boolean array is actually reversed
"""
def get_mask():
    boards = [[ui.ch1button_0.isChecked(), ui.ch2button_0.isChecked(), ui.ch3button_0.isChecked(),
        ui.ch4button_0.isChecked(), ui.ch5button_0.isChecked(), ui.ch6button_0.isChecked(),
        ui.ch7button_0.isChecked(), ui.ch8button_0.isChecked(), ui.ch9button_0.isChecked(),
        ui.ch10button_0.isChecked(), ui.ch11button_0.isChecked(), ui.ch12button_0.isChecked(),
        ui.ch13button_0.isChecked(), ui.ch14button_0.isChecked(), ui.ch15button_0.isChecked(),
        ui.ch16button_0.isChecked(), ui.ch17button_0.isChecked(), ui.ch18button_0.isChecked(),
        ui.ch19button_0.isChecked(), ui.ch20button_0.isChecked(), ui.ch21button_0.isChecked(),
        ui.ch22button_0.isChecked(), ui.ch23button_0.isChecked(), ui.ch24button_0.isChecked(),
        ui.ch25button_0.isChecked(), ui.ch26button_0.isChecked(), ui.ch27button_0.isChecked(),
        ui.ch28button_0.isChecked(), ui.ch29button_0.isChecked(), ui.ch30button_0.isChecked()],

        [ui.ch1button_1.isChecked(), ui.ch2button_1.isChecked(), ui.ch3button_1.isChecked(),
        ui.ch4button_1.isChecked(), ui.ch5button_1.isChecked(), ui.ch6button_1.isChecked(),
        ui.ch7button_1.isChecked(), ui.ch8button_1.isChecked(), ui.ch9button_1.isChecked(),
        ui.ch10button_1.isChecked(), ui.ch11button_1.isChecked(), ui.ch12button_1.isChecked(),
        ui.ch13button_1.isChecked(), ui.ch14button_1.isChecked(), ui.ch15button_1.isChecked(),
        ui.ch16button_1.isChecked(), ui.ch17button_1.isChecked(), ui.ch18button_1.isChecked(),
        ui.ch19button_1.isChecked(), ui.ch20button_1.isChecked(), ui.ch21button_1.isChecked(),
        ui.ch22button_1.isChecked(), ui.ch23button_1.isChecked(), ui.ch24button_1.isChecked(),
        ui.ch25button_1.isChecked(), ui.ch26button_1.isChecked(), ui.ch27button_1.isChecked(),
        ui.ch28button_1.isChecked(), ui.ch29button_1.isChecked(), ui.ch30button_1.isChecked()],

        [ui.ch1button_2.isChecked(), ui.ch2button_2.isChecked(), ui.ch3button_2.isChecked(),
        ui.ch4button_2.isChecked(), ui.ch5button_2.isChecked(), ui.ch6button_2.isChecked(),
        ui.ch7button_2.isChecked(), ui.ch8button_2.isChecked(), ui.ch9button_2.isChecked(),
        ui.ch10button_2.isChecked(), ui.ch11button_2.isChecked(), ui.ch12button_2.isChecked(),
        ui.ch13button_2.isChecked(), ui.ch14button_2.isChecked(), ui.ch15button_2.isChecked(),
        ui.ch16button_2.isChecked(), ui.ch17button_2.isChecked(), ui.ch18button_2.isChecked(),
        ui.ch19button_2.isChecked(), ui.ch20button_2.isChecked(), ui.ch21button_2.isChecked(),
        ui.ch22button_2.isChecked(), ui.ch23button_2.isChecked(), ui.ch24button_2.isChecked(),
        ui.ch25button_2.isChecked(), ui.ch26button_2.isChecked(), ui.ch27button_2.isChecked(),
        ui.ch28button_2.isChecked(), ui.ch29button_2.isChecked(), ui.ch30button_2.isChecked()],

        [ui.ch1button_3.isChecked(), ui.ch2button_3.isChecked(), ui.ch3button_3.isChecked(),
        ui.ch4button_3.isChecked(), ui.ch5button_3.isChecked(), ui.ch6button_3.isChecked(),
        ui.ch7button_3.isChecked(), ui.ch8button_3.isChecked(), ui.ch9button_3.isChecked(),
        ui.ch10button_3.isChecked(), ui.ch11button_3.isChecked(), ui.ch12button_3.isChecked(),
        ui.ch13button_3.isChecked(), ui.ch14button_3.isChecked(), ui.ch15button_3.isChecked(),
        ui.ch16button_3.isChecked(), ui.ch17button_3.isChecked(), ui.ch18button_3.isChecked(),
        ui.ch19button_3.isChecked(), ui.ch20button_3.isChecked(), ui.ch21button_3.isChecked(),
        ui.ch22button_3.isChecked(), ui.ch23button_3.isChecked(), ui.ch24button_3.isChecked(),
        ui.ch25button_3.isChecked(), ui.ch26button_3.isChecked(), ui.ch27button_3.isChecked(),
        ui.ch28button_3.isChecked(), ui.ch29button_3.isChecked(), ui.ch30button_3.isChecked()],

        [ui.ch1button_4.isChecked(), ui.ch2button_4.isChecked(), ui.ch3button_4.isChecked(),
        ui.ch4button_4.isChecked(), ui.ch5button_4.isChecked(), ui.ch6button_4.isChecked(),
        ui.ch7button_4.isChecked(), ui.ch8button_4.isChecked(), ui.ch9button_4.isChecked(),
        ui.ch10button_4.isChecked(), ui.ch11button_4.isChecked(), ui.ch12button_4.isChecked(),
        ui.ch13button_4.isChecked(), ui.ch14button_4.isChecked(), ui.ch15button_4.isChecked(),
        ui.ch16button_4.isChecked(), ui.ch17button_4.isChecked(), ui.ch18button_4.isChecked(),
        ui.ch19button_4.isChecked(), ui.ch20button_4.isChecked(), ui.ch21button_4.isChecked(),
        ui.ch22button_4.isChecked(), ui.ch23button_4.isChecked(), ui.ch24button_4.isChecked(),
        ui.ch25button_4.isChecked(), ui.ch26button_4.isChecked(), ui.ch27button_4.isChecked(),
        ui.ch28button_4.isChecked(), ui.ch29button_4.isChecked(), ui.ch30button_4.isChecked()],

        [ui.ch1button_5.isChecked(), ui.ch2button_5.isChecked(), ui.ch3button_5.isChecked(),
        ui.ch4button_5.isChecked(), ui.ch5button_5.isChecked(), ui.ch6button_5.isChecked(),
        ui.ch7button_5.isChecked(), ui.ch8button_5.isChecked(), ui.ch9button_5.isChecked(),
        ui.ch10button_5.isChecked(), ui.ch11button_5.isChecked(), ui.ch12button_5.isChecked(),
        ui.ch13button_5.isChecked(), ui.ch14button_5.isChecked(), ui.ch15button_5.isChecked(),
        ui.ch16button_5.isChecked(), ui.ch17button_5.isChecked(), ui.ch18button_5.isChecked(),
        ui.ch19button_5.isChecked(), ui.ch20button_5.isChecked(), ui.ch21button_5.isChecked(),
        ui.ch22button_5.isChecked(), ui.ch23button_5.isChecked(), ui.ch24button_5.isChecked(),
        ui.ch25button_5.isChecked(), ui.ch26button_5.isChecked(), ui.ch27button_5.isChecked(),
        ui.ch28button_5.isChecked(), ui.ch29button_5.isChecked(), ui.ch30button_5.isChecked()],

        [ui.ch1button_6.isChecked(), ui.ch2button_6.isChecked(), ui.ch3button_6.isChecked(),
        ui.ch4button_6.isChecked(), ui.ch5button_6.isChecked(), ui.ch6button_6.isChecked(),
        ui.ch7button_6.isChecked(), ui.ch8button_6.isChecked(), ui.ch9button_6.isChecked(),
        ui.ch10button_6.isChecked(), ui.ch11button_6.isChecked(), ui.ch12button_6.isChecked(),
        ui.ch13button_6.isChecked(), ui.ch14button_6.isChecked(), ui.ch15button_6.isChecked(),
        ui.ch16button_6.isChecked(), ui.ch17button_6.isChecked(), ui.ch18button_6.isChecked(),
        ui.ch19button_6.isChecked(), ui.ch20button_6.isChecked(), ui.ch21button_6.isChecked(),
        ui.ch22button_6.isChecked(), ui.ch23button_6.isChecked(), ui.ch24button_6.isChecked(),
        ui.ch25button_6.isChecked(), ui.ch26button_6.isChecked(), ui.ch27button_6.isChecked(),
        ui.ch28button_6.isChecked(), ui.ch29button_6.isChecked(), ui.ch30button_6.isChecked()],

        [ui.ch1button_7.isChecked(), ui.ch2button_7.isChecked(), ui.ch3button_7.isChecked(),
        ui.ch4button_7.isChecked(), ui.ch5button_7.isChecked(), ui.ch6button_7.isChecked(),
        ui.ch7button_7.isChecked(), ui.ch8button_7.isChecked(), ui.ch9button_7.isChecked(),
        ui.ch10button_7.isChecked(), ui.ch11button_7.isChecked(), ui.ch12button_7.isChecked(),
        ui.ch13button_7.isChecked(), ui.ch14button_7.isChecked(), ui.ch15button_7.isChecked(),
        ui.ch16button_7.isChecked(), ui.ch17button_7.isChecked(), ui.ch18button_7.isChecked(),
        ui.ch19button_7.isChecked(), ui.ch20button_7.isChecked(), ui.ch21button_7.isChecked(),
        ui.ch22button_7.isChecked(), ui.ch23button_7.isChecked(), ui.ch24button_7.isChecked(),
        ui.ch25button_7.isChecked(), ui.ch26button_7.isChecked(), ui.ch27button_7.isChecked(),
        ui.ch28button_7.isChecked(), ui.ch29button_7.isChecked(), ui.ch30button_7.isChecked()]]


    out = ''
    for board, channels in enumerate(boards):
        bin_string = ''
        for on in channels:
            bin_string = ('1' if on else '0') + bin_string
        out += 'trig_mask\t{}\t{}\n'.format(board, hex(int(bin_string, 2)))

    return out


def get_trig_en():
    trigs = [ui.trig_en_board_0.isChecked(), ui.trig_en_board_1.isChecked(), ui.trig_en_board_2.isChecked(),
        ui.trig_en_board_3.isChecked(), ui.trig_en_board_4.isChecked(), ui.trig_en_board_5.isChecked(),
        ui.trig_en_board_6.isChecked(), ui.trig_en_board_7.isChecked()]

    out = ''
    for board, value in enumerate(trigs):
        on = '1' if value else '0'
        out += 'trig_enable\t{}\t{}\n'.format(board, on)
    return out

def get_trig_sign():
    signs = [ui.trig_sign_0.currentText(), ui.trig_sign_1.currentText(), ui.trig_sign_2.currentText(),
        ui.trig_sign_3.currentText(), ui.trig_sign_4.currentText(), ui.trig_sign_5.currentText(),
        ui.trig_sign_6.currentText(), ui.trig_sign_7.currentText()]
    out = ''
    for board, value in enumerate(signs):
        sign = '1' if value == '+' else '0'
        out += 'trig_sign\t{}\t{}\n'.format(board, sign)
    return out

def get_hwtrig_settings():
    hwtrig = ui.hardware_trig.isChecked()
    sources = [ui.hardware_src_ext.isChecked(), ui.hardware_src_0.isChecked(),
        ui.hardware_src_1.isChecked(), ui.hardware_src_2.isChecked(), ui.hardware_src_3.isChecked(),
        ui.hardware_src_4.isChecked(), ui.hardware_src_5.isChecked(), ui.hardware_src_6.isChecked(),
        ui.hardware_src_7.isChecked()]
    on = '1' if hwtrig else '0'
    src = np.argmax(sources)
    if src > 0: src = src + 2
    return 'hrdw_trig\t{}\nhrdw_src_trig\t{}\n'.format(on, src)


def parse_trig():
    filename, _ = QFileDialog.getSaveFileName(ui.export_trig, 'Save File', os.getcwd())
    f = open(filename, 'w')
    # Masks
    f.write(get_mask() + '\n')
    f.write(get_trig_en() + '\n')
    f.write(get_trig_sign() + '\n')
    f.write(get_hwtrig_settings() + '\n')

    f.write(ui.extras_text.toPlainText())
    f.close()

###############################################################################
# clicked
#
#
#
def maskall(board):
    group = eval('ui.b{}_mask'.format(board))
    for button in group.buttons():
        button.setChecked(True)

def masknone(board):
    group = eval('ui.b{}_mask'.format(board))
    for button in group.buttons():
        button.setChecked(False)

def sync_ped(board):
    group = [eval('ui.Ped_{}_{}'.format(board, chip)) for chip in range(1,6)]
    const = group[0].value()
    for text in group:
        text.setValue(const)

def sync_thresh(board):
    group = [eval('ui.thresh_{}_{}'.format(board, chip)) for chip in range(1,6)]
    const = group[0].value()
    for text in group:
        text.setValue(const)

def buttons():
    ui.export_acdc.clicked.connect(parse_acdc)
    ui.export_trig.clicked.connect(parse_trig)
    ui.mask_all_0.clicked.connect(lambda: maskall(0))
    ui.mask_all_1.clicked.connect(lambda: maskall(1))
    ui.mask_all_2.clicked.connect(lambda: maskall(2))
    ui.mask_all_3.clicked.connect(lambda: maskall(3))
    ui.mask_all_4.clicked.connect(lambda: maskall(4))
    ui.mask_all_5.clicked.connect(lambda: maskall(5))
    ui.mask_all_6.clicked.connect(lambda: maskall(6))
    ui.mask_all_7.clicked.connect(lambda: maskall(7))
    ui.mask_none_0.clicked.connect(lambda: masknone(0))
    ui.mask_none_1.clicked.connect(lambda: masknone(1))
    ui.mask_none_2.clicked.connect(lambda: masknone(2))
    ui.mask_none_3.clicked.connect(lambda: masknone(3))
    ui.mask_none_4.clicked.connect(lambda: masknone(4))
    ui.mask_none_5.clicked.connect(lambda: masknone(5))
    ui.mask_none_6.clicked.connect(lambda: masknone(6))
    ui.mask_none_7.clicked.connect(lambda: masknone(7))
    ui.sync_ped_0.clicked.connect(lambda: sync_ped(0))
    ui.sync_ped_1.clicked.connect(lambda: sync_ped(1))
    ui.sync_ped_2.clicked.connect(lambda: sync_ped(2))
    ui.sync_ped_3.clicked.connect(lambda: sync_ped(3))
    ui.sync_ped_4.clicked.connect(lambda: sync_ped(4))
    ui.sync_ped_5.clicked.connect(lambda: sync_ped(5))
    ui.sync_ped_6.clicked.connect(lambda: sync_ped(6))
    ui.sync_ped_7.clicked.connect(lambda: sync_ped(7))
    ui.sync_thresh_0.clicked.connect(lambda: sync_thresh(0))
    ui.sync_thresh_1.clicked.connect(lambda: sync_thresh(1))
    ui.sync_thresh_2.clicked.connect(lambda: sync_thresh(2))
    ui.sync_thresh_3.clicked.connect(lambda: sync_thresh(3))
    ui.sync_thresh_4.clicked.connect(lambda: sync_thresh(4))
    ui.sync_thresh_5.clicked.connect(lambda: sync_thresh(5))
    ui.sync_thresh_6.clicked.connect(lambda: sync_thresh(6))
    ui.sync_thresh_7.clicked.connect(lambda: sync_thresh(7))


###############################################################################
# Main Methods
#
#
#
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    buttons()

    MainWindow.show()
    sys.exit(app.exec_())
