# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'amm-gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import matplotlib
matplotlib.use("Qt5Agg")  # claim qt5 agg.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
import yaml
import sys
import os
from amm import amm


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1046, 786)
        # Dialog.setModal(False)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(10, 760, 351, 16))
        self.label_18.setObjectName("label_18")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 590, 1021, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.result_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.result_layout.setContentsMargins(0, 0, 0, 0)
        self.result_layout.setObjectName("result_layout")
        self.res_box_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.res_box_1.setFont(font)
        self.res_box_1.setText("")
        self.res_box_1.setObjectName("res_box_1")
        self.result_layout.addWidget(self.res_box_1, 1, 2, 1, 1)
        self.cal_m0_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cal_m0_button.setFont(font)
        self.cal_m0_button.setObjectName("cal_m0_button")
        self.result_layout.addWidget(self.cal_m0_button, 5, 3, 1, 3)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.result_layout.addWidget(self.line_2, 0, 0, 1, 6)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.result_layout.addWidget(self.label_19, 1, 0, 1, 1)
        self.res_box_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.res_box_3.setFont(font)
        self.res_box_3.setText("")
        self.res_box_3.setObjectName("res_box_3")
        self.result_layout.addWidget(self.res_box_3, 5, 2, 1, 1)
        self.res_box_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.res_box_2.setFont(font)
        self.res_box_2.setText("")
        self.res_box_2.setObjectName("res_box_2")
        self.result_layout.addWidget(self.res_box_2, 3, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.result_layout.addWidget(self.label_20, 1, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.result_layout.addWidget(self.label_21, 3, 0, 1, 1)
        self.write_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.write_3.setFont(font)
        self.write_3.setObjectName("write_3")
        self.result_layout.addWidget(self.write_3, 5, 1, 1, 1)
        self.write_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.write_1.setFont(font)
        self.write_1.setObjectName("write_1")
        self.result_layout.addWidget(self.write_1, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.result_layout.addWidget(self.label_22, 3, 3, 1, 1)
        self.res_box_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.res_box_5.setFont(font)
        self.res_box_5.setText("")
        self.res_box_5.setObjectName("res_box_5")
        self.result_layout.addWidget(self.res_box_5, 3, 5, 1, 1)
        self.write_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.write_5.setFont(font)
        self.write_5.setObjectName("write_5")
        self.result_layout.addWidget(self.write_5, 3, 4, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.result_layout.addWidget(self.label_23, 5, 0, 1, 1)
        self.res_box_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.res_box_4.setFont(font)
        self.res_box_4.setText("")
        self.res_box_4.setObjectName("res_box_4")
        self.result_layout.addWidget(self.res_box_4, 1, 5, 1, 1)
        self.write_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.write_2.setFont(font)
        self.write_2.setObjectName("write_2")
        self.result_layout.addWidget(self.write_2, 3, 1, 1, 1)
        self.write_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.write_4.setFont(font)
        self.write_4.setObjectName("write_4")
        self.result_layout.addWidget(self.write_4, 1, 4, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.result_layout.addWidget(self.line_4, 6, 0, 1, 6)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(800, 10, 231, 341))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.config_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.config_layout.setContentsMargins(0, 0, 0, 0)
        self.config_layout.setObjectName("config_layout")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.config_layout.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.config_layout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.config_layout.addWidget(self.label_10, 10, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.config_layout.addWidget(self.label_4, 1, 0, 1, 1)
        self.low_lim_box = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.low_lim_box.setFont(font)
        self.low_lim_box.setObjectName("low_lim_box")
        self.config_layout.addWidget(self.low_lim_box, 9, 1, 1, 1)
        self.TIME_box = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TIME_box.setFont(font)
        self.TIME_box.setObjectName("TIME_box")
        self.config_layout.addWidget(self.TIME_box, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.config_layout.addWidget(self.label_6, 3, 0, 1, 1)
        self.RATE_box = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RATE_box.setFont(font)
        self.RATE_box.setObjectName("RATE_box")
        self.config_layout.addWidget(self.RATE_box, 0, 1, 1, 1)
        self.FFT_size_box = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FFT_size_box.setFont(font)
        self.FFT_size_box.setObjectName("FFT_size_box")
        self.config_layout.addWidget(self.FFT_size_box, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.config_layout.addWidget(self.label_5, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.config_layout.addWidget(self.label_3, 1, 2, 1, 1)
        self.high_lim_box = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.high_lim_box.setFont(font)
        self.high_lim_box.setObjectName("high_lim_box")
        self.config_layout.addWidget(self.high_lim_box, 10, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.config_layout.addWidget(self.label, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.config_layout.addWidget(self.label_9, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.config_layout.addWidget(self.label_7, 9, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.config_layout.addWidget(self.label_2, 0, 2, 1, 1)
        self.noise_gate_box = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.noise_gate_box.setFont(font)
        self.noise_gate_box.setObjectName("noise_gate_box")
        self.config_layout.addWidget(self.noise_gate_box, 6, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 781, 571))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.visualizer_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.visualizer_layout.setContentsMargins(0, 0, 0, 0)
        self.visualizer_layout.setObjectName("visualizer_layout")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.visualizer_layout.addWidget(self.label_16, 7, 0, 1, 1)
        self.figure_3 = QtWidgets.QGraphicsView(self.gridLayoutWidget_3)
        self.figure_3.setObjectName("figure_3")
        self.visualizer_layout.addWidget(self.figure_3, 7, 1, 1, 1)
        self.figure_2 = QtWidgets.QGraphicsView(self.gridLayoutWidget_3)
        self.figure_2.setObjectName("figure_2")
        self.visualizer_layout.addWidget(self.figure_2, 5, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.visualizer_layout.addWidget(self.label_15, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.visualizer_layout.addWidget(self.label_13, 6, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.visualizer_layout.addWidget(self.label_17, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.visualizer_layout.addWidget(self.label_14, 8, 1, 1, 1)
        self.figure_1 = QtWidgets.QGraphicsView(self.gridLayoutWidget_3)
        self.figure_1.setObjectName("figure_1")
        self.visualizer_layout.addWidget(self.figure_1, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.visualizer_layout.addWidget(self.label_12, 4, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.visualizer_layout.addWidget(self.line, 3, 2, 6, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(800, 360, 231, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.start_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.start_layout.setContentsMargins(0, 0, 0, 0)
        self.start_layout.setObjectName("start_layout")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.start_layout.addWidget(self.line_3)
        self.start_test_button = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_test_button.setFont(font)
        self.start_test_button.setFlat(False)
        self.start_test_button.setObjectName("start_test_button")
        self.start_layout.addWidget(self.start_test_button)
        self.output_browser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_browser.setFont(font)
        self.output_browser.setObjectName("output_browser")
        self.start_layout.addWidget(self.output_browser)
        # add a widget by hand
        self.peak_freq_browser = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.peak_freq_browser.setFont(font)
        self.peak_freq_browser.setObjectName("peak_freq_browser")
        self.start_layout.addWidget(self.peak_freq_browser)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.RATE_box, self.TIME_box)
        Dialog.setTabOrder(self.TIME_box, self.FFT_size_box)
        Dialog.setTabOrder(self.FFT_size_box, self.noise_gate_box)
        Dialog.setTabOrder(self.noise_gate_box, self.low_lim_box)
        Dialog.setTabOrder(self.low_lim_box, self.high_lim_box)
        Dialog.setTabOrder(self.high_lim_box, self.start_test_button)
        Dialog.setTabOrder(self.start_test_button, self.output_browser)
        Dialog.setTabOrder(self.output_browser, self.figure_1)
        Dialog.setTabOrder(self.figure_1, self.figure_2)
        Dialog.setTabOrder(self.figure_2, self.figure_3)
        Dialog.setTabOrder(self.figure_3, self.write_1)
        Dialog.setTabOrder(self.write_1, self.res_box_1)
        Dialog.setTabOrder(self.res_box_1, self.write_2)
        Dialog.setTabOrder(self.write_2, self.res_box_2)
        Dialog.setTabOrder(self.res_box_2, self.write_3)
        Dialog.setTabOrder(self.write_3, self.res_box_3)
        Dialog.setTabOrder(self.res_box_3, self.write_4)
        Dialog.setTabOrder(self.write_4, self.res_box_4)
        Dialog.setTabOrder(self.res_box_4, self.write_5)
        Dialog.setTabOrder(self.write_5, self.res_box_5)
        Dialog.setTabOrder(self.res_box_5, self.cal_m0_button)

        # connect working code
        self.work(Dialog)

    def retranslateUi(self, Dialog):
        # load config.yaml file
        self.config_yaml()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Geo-sonic AMM"))
        self.label_18.setText(_translate(
            "Dialog", "Geo-sonic V1.0 AMM module V1.2 Copyright Siyuan Xu"))
        self.cal_m0_button.setText(_translate("Dialog", "计算堆石体参振质量 m0"))
        self.label_19.setText(_translate("Dialog", "荷载级1"))
        self.label_20.setText(_translate("Dialog", "荷载级4"))
        self.label_21.setText(_translate("Dialog", "荷载级2"))
        self.write_3.setText(_translate("Dialog", "记录结果"))
        self.write_1.setText(_translate("Dialog", "记录结果"))
        self.label_22.setText(_translate("Dialog", "荷载级5"))
        self.write_5.setText(_translate("Dialog", "记录结果"))
        self.label_23.setText(_translate("Dialog", "荷载级3"))
        self.write_2.setText(_translate("Dialog", "记录结果"))
        self.write_4.setText(_translate("Dialog", "记录结果"))
        self.label_11.setText(_translate("Dialog", "上限频率"))
        self.label_8.setText(_translate("Dialog", "触发限"))
        self.label_10.setText(_translate("Dialog", "Hz"))
        self.label_4.setText(_translate("Dialog", "总时长"))
        self.low_lim_box.setText(_translate(
            "Dialog", "{}".format(self.low_lim)))
        self.TIME_box.setText(_translate("Dialog", "{}".format(self.TIME)))
        self.label_6.setText(_translate("Dialog", "FFT size"))
        self.RATE_box.setText(_translate("Dialog", "{}".format(self.RATE)))
        self.FFT_size_box.setText(_translate(
            "Dialog", "{}".format(self.FFT_size)))
        self.label_5.setText(_translate("Dialog", "毫秒"))
        self.label_3.setText(_translate("Dialog", "秒"))
        self.high_lim_box.setText(_translate(
            "Dialog", "{}".format(self.hight_lim)))
        self.label.setText(_translate("Dialog", "采样率"))
        self.label_9.setText(_translate("Dialog", "下限频率"))
        self.label_7.setText(_translate("Dialog", "Hz"))
        self.label_2.setText(_translate("Dialog", "Hz"))
        self.noise_gate_box.setText(_translate(
            "Dialog", "{}".format(self.Noise_gate)))
        self.label_16.setText(_translate("Dialog", "A"))
        self.label_15.setText(_translate("Dialog", "A"))
        self.label_13.setText(_translate("Dialog", "t (ms)"))
        self.label_17.setText(_translate("Dialog", "A"))
        self.label_14.setText(_translate("Dialog", "freqs (Hz)"))
        self.label_12.setText(_translate("Dialog", "t (s)"))
        self.start_test_button.setText(_translate("Dialog", "开始检测"))
        self.output_browser.setText(_translate(
            'Dialog', '欢迎使用Geo-sonic系列软件AMM振动检测模块'))

    def work(self, Dialog):
        # start amm test
        self.start_test_button.clicked.connect(self.start_test)

        # write results
        self.write_1.clicked.connect(self.write_res_1)
        self.write_2.clicked.connect(self.write_res_2)
        self.write_3.clicked.connect(self.write_res_3)
        self.write_4.clicked.connect(self.write_res_4)
        self.write_5.clicked.connect(self.write_res_5)

        # calculate m0
        self.cal_m0_button.clicked.connect(self.cal_m0)

    def config_yaml(self):
        config = yaml.load(open('config.yaml'))

        self.RATE = config['RATE']
        self.TIME = config['TIME']
        self.FFT_size = config['FFT_size']
        self.Noise_gate = config['Noise_gate']
        self.low_lim = config['low_lim']
        self.hight_lim = config['hight_lim']

    def start_test(self, Dialog):
        amm_sample = amm()

        amm_sample.RATE = int(self.RATE_box.text())
        amm_sample.RECORD_SECONDS = float(self.TIME_box.text())
        amm_sample.fft_time = int(self.FFT_size_box.text())
        amm_sample.noise_gate = int(self.noise_gate_box.text())
        amm_sample.low_lim = int(self.low_lim_box.text())
        amm_sample.hight_lim = int(self.high_lim_box.text())

        amm_sample.CHUNK = int(amm_sample.RATE / 50)
        amm_sample.fft_size = int(
            (amm_sample.fft_time / 1000) * amm_sample.RATE)

        amm_sample.run_test()

        # 创建工作绘图对象
        f1 = visualizer()
        f1.visualizer(amm_sample.sonic_x, amm_sample.sonic_y)
        # 创建gui绘图对象
        gs1 = QtWidgets.QGraphicsScene()
        gs1.addWidget(f1)
        self.figure_1.setScene(gs1)

        f2 = visualizer()
        f2.visualizer(amm_sample.x * 1000, amm_sample.y)
        gs2 = QtWidgets.QGraphicsScene()
        gs2.addWidget(f2)
        self.figure_2.setScene(gs2)

        f3 = visualizer()
        f3.visualizer(amm_sample.fft_x, amm_sample.fft_y)
        gs3 = QtWidgets.QGraphicsScene()
        gs3.addWidget(f3)
        self.figure_3.setScene(gs3)

        # print peak freq in outputbrowser
        _translate = QtCore.QCoreApplication.translate
        self.output_browser.setText(_translate(
            'Dialog', '欢迎使用Geo-sonic系列软件AMM振动检测模块\
            本次锤击测得主频为'))
        self.peak_freq_browser.setText(_translate(
            'Dialog', '{}Hz'.format(round(amm_sample.peak_freq, 2))))

    def write_res_1(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.res_box_1.insert(_translate(
            'Dialog', '{}'.format(self.peak_freq_browser.text())))

    def write_res_2(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.res_box_2.insert(_translate(
            'Dialog', '{}'.format(self.peak_freq_browser.text())))

    def write_res_3(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.res_box_3.insert(_translate(
            'Dialog', '{}'.format(self.peak_freq_browser.text())))

    def write_res_4(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.res_box_4.insert(_translate(
            'Dialog', '{}'.format(self.peak_freq_browser.text())))

    def write_res_5(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.res_box_5.insert(_translate(
            'Dialog', '{}'.format(self.peak_freq_browser.text())))

    def cal_m0(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy import optimize
        import time

        def accurate_res(a):
            # a should be a textedit.text()
            b = a.split('Hz')[:-1]
            return [float(i) for i in b]

        def one_freq(a):
            # a should be a list of freqs
            a.remove(max(a))
            a.remove(min(a))

            return float(np.mean(a))

        def linear_fit(x, k, b):
            return k * x + b

        res_1 = accurate_res(self.res_box_1.text())
        res_2 = accurate_res(self.res_box_2.text())
        res_3 = accurate_res(self.res_box_3.text())
        res_4 = accurate_res(self.res_box_4.text())
        res_5 = accurate_res(self.res_box_5.text())

        freq_1 = one_freq(res_1)
        freq_2 = one_freq(res_2)
        freq_3 = one_freq(res_3)
        freq_4 = one_freq(res_4)
        freq_5 = one_freq(res_5)

        delta_ms = np.array([150, 225, 300, 375, 450])
        freqs = np.array([freq_1, freq_2, freq_3, freq_4, freq_5])
        D = (2 * np.pi * freqs)**(-2) * (1000000)

        k, b = optimize.curve_fit(linear_fit, delta_ms, D)[0]

        m0 = b / k
        x = np.array([-m0, max(delta_ms)])
        y = linear_fit(x, k, b)

        results = np.vstack([delta_ms, freqs]).T
        np.savetxt('{}.dat'.format(time.strftime(
            "%Y-%m-%d_%H-%M-%S", time.localtime())), results)

        plt.scatter(delta_ms, D)
        plt.title('m0 = {} Kg'.format(m0))
        plt.xlabel('Additional mess delta m (Kg)')
        plt.ylabel('Para D (ms^-2)')

        plt.plot(x, y)
        plt.show()
        plt.savefig('{}.png'.format(time.strftime(
            "%Y-%m-%d_%H-%M-%S", time.localtime())), dpi=120)

# 绘图功能实现
class visualizer(FigureCanvas):
    def __init__(self, parent=None, width=7.5, height=1.3, dpi=100):
        # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_tight_layout(True)

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.axes = fig.add_subplot(111)

    def visualizer(self, x, y):
        self.axes.plot(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splashscreen = QtWidgets.QSplashScreen(QtGui.QPixmap('splash.png'))
    splashscreen.show()
    import time
    time.sleep(1)
    splashscreen.finish(splashscreen)
    MainWindow = QtWidgets.QMainWindow()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icon_small.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
    MainWindow.setWindowIcon(icon)
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
