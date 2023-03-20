# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GTM_SDC.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(20, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Decode_Modes_CheckBox_Sci = QtWidgets.QCheckBox(self.centralwidget)
        self.Decode_Modes_CheckBox_Sci.setGeometry(QtCore.QRect(70, 190, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Decode_Modes_CheckBox_Sci.setFont(font)
        self.Decode_Modes_CheckBox_Sci.setObjectName("Decode_Modes_CheckBox_Sci")
        self.Decoder_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Decoder_Button.setGeometry(QtCore.QRect(20, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.Decoder_Button.setFont(font)
        self.Decoder_Button.setObjectName("Decoder_Button")
        self.Calibrator_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Calibrator_Button.setGeometry(QtCore.QRect(20, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.Calibrator_Button.setFont(font)
        self.Calibrator_Button.setObjectName("Calibrator_Button")
        self.InputFile_Decoder_Text = QtWidgets.QTextEdit(self.centralwidget)
        self.InputFile_Decoder_Text.setGeometry(QtCore.QRect(180, 110, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.InputFile_Decoder_Text.setFont(font)
        self.InputFile_Decoder_Text.setObjectName("InputFile_Decoder_Text")
        self.InputFile_Decoder_Button = QtWidgets.QPushButton(self.centralwidget)
        self.InputFile_Decoder_Button.setGeometry(QtCore.QRect(70, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.InputFile_Decoder_Button.setFont(font)
        self.InputFile_Decoder_Button.setObjectName("InputFile_Decoder_Button")
        self.Decode_Modes_Text = QtWidgets.QLabel(self.centralwidget)
        self.Decode_Modes_Text.setGeometry(QtCore.QRect(70, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Decode_Modes_Text.setFont(font)
        self.Decode_Modes_Text.setObjectName("Decode_Modes_Text")
        self.Decode_Modes_CheckBox_TMTC = QtWidgets.QCheckBox(self.centralwidget)
        self.Decode_Modes_CheckBox_TMTC.setGeometry(QtCore.QRect(70, 250, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Decode_Modes_CheckBox_TMTC.setFont(font)
        self.Decode_Modes_CheckBox_TMTC.setObjectName("Decode_Modes_CheckBox_TMTC")
        self.Export_Modes_CheckBox_Sci_Raw = QtWidgets.QCheckBox(self.centralwidget)
        self.Export_Modes_CheckBox_Sci_Raw.setGeometry(QtCore.QRect(350, 190, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Export_Modes_CheckBox_Sci_Raw.setFont(font)
        self.Export_Modes_CheckBox_Sci_Raw.setObjectName("Export_Modes_CheckBox_Sci_Raw")
        self.Export_Modes_CheckBox_Sci_Pipeline = QtWidgets.QCheckBox(self.centralwidget)
        self.Export_Modes_CheckBox_Sci_Pipeline.setGeometry(QtCore.QRect(350, 220, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Export_Modes_CheckBox_Sci_Pipeline.setFont(font)
        self.Export_Modes_CheckBox_Sci_Pipeline.setObjectName("Export_Modes_CheckBox_Sci_Pipeline")
        self.Export_Modes_CheckBox_Sci_Both = QtWidgets.QCheckBox(self.centralwidget)
        self.Export_Modes_CheckBox_Sci_Both.setGeometry(QtCore.QRect(350, 250, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Export_Modes_CheckBox_Sci_Both.setFont(font)
        self.Export_Modes_CheckBox_Sci_Both.setObjectName("Export_Modes_CheckBox_Sci_Both")
        self.Decoder_Button_Status = QtWidgets.QLabel(self.centralwidget)
        self.Decoder_Button_Status.setGeometry(QtCore.QRect(140, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Decoder_Button_Status.setFont(font)
        self.Decoder_Button_Status.setText("")
        self.Decoder_Button_Status.setObjectName("Decoder_Button_Status")
        self.Calibrator_Button_Status = QtWidgets.QLabel(self.centralwidget)
        self.Calibrator_Button_Status.setGeometry(QtCore.QRect(150, 330, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Calibrator_Button_Status.setFont(font)
        self.Calibrator_Button_Status.setText("")
        self.Calibrator_Button_Status.setObjectName("Calibrator_Button_Status")
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(430, 290, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.Start_Button.setFont(font)
        self.Start_Button.setObjectName("Start_Button")
        self.Start_progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.Start_progressBar.setGeometry(QtCore.QRect(530, 290, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Start_progressBar.setFont(font)
        self.Start_progressBar.setProperty("value", 24)
        self.Start_progressBar.setObjectName("Start_progressBar")
        self.Start_Status = QtWidgets.QLabel(self.centralwidget)
        self.Start_Status.setGeometry(QtCore.QRect(670, 290, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Start_Status.setFont(font)
        self.Start_Status.setObjectName("Start_Status")
        self.Hit_Selection_CheckBox_Hit = QtWidgets.QCheckBox(self.centralwidget)
        self.Hit_Selection_CheckBox_Hit.setGeometry(QtCore.QRect(520, 220, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Hit_Selection_CheckBox_Hit.setFont(font)
        self.Hit_Selection_CheckBox_Hit.setObjectName("Hit_Selection_CheckBox_Hit")
        self.Hit_Selection_Text = QtWidgets.QLabel(self.centralwidget)
        self.Hit_Selection_Text.setGeometry(QtCore.QRect(520, 190, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Hit_Selection_Text.setFont(font)
        self.Hit_Selection_Text.setObjectName("Hit_Selection_Text")
        self.Hit_Selection_CheckBox_NoHit = QtWidgets.QCheckBox(self.centralwidget)
        self.Hit_Selection_CheckBox_NoHit.setGeometry(QtCore.QRect(520, 250, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Hit_Selection_CheckBox_NoHit.setFont(font)
        self.Hit_Selection_CheckBox_NoHit.setObjectName("Hit_Selection_CheckBox_NoHit")
        self.Extract_NSPO_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Extract_NSPO_CheckBox.setGeometry(QtCore.QRect(90, 220, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Extract_NSPO_CheckBox.setFont(font)
        self.Extract_NSPO_CheckBox.setObjectName("Extract_NSPO_CheckBox")
        self.GTM_ICON = QtWidgets.QLabel(self.centralwidget)
        self.GTM_ICON.setGeometry(QtCore.QRect(660, 10, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.GTM_ICON.setFont(font)
        self.GTM_ICON.setText("")
        self.GTM_ICON.setObjectName("GTM_ICON")
        self.InputFile_Calibrator_Button = QtWidgets.QPushButton(self.centralwidget)
        self.InputFile_Calibrator_Button.setGeometry(QtCore.QRect(70, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.InputFile_Calibrator_Button.setFont(font)
        self.InputFile_Calibrator_Button.setObjectName("InputFile_Calibrator_Button")
        self.InputFile_Calibrator_Text = QtWidgets.QTextEdit(self.centralwidget)
        self.InputFile_Calibrator_Text.setGeometry(QtCore.QRect(180, 380, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.InputFile_Calibrator_Text.setFont(font)
        self.InputFile_Calibrator_Text.setObjectName("InputFile_Calibrator_Text")
        self.Calibrator_GroupBox_Visualization = QtWidgets.QGroupBox(self.centralwidget)
        self.Calibrator_GroupBox_Visualization.setGeometry(QtCore.QRect(70, 430, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Calibrator_GroupBox_Visualization.setFont(font)
        self.Calibrator_GroupBox_Visualization.setFlat(False)
        self.Calibrator_GroupBox_Visualization.setCheckable(False)
        self.Calibrator_GroupBox_Visualization.setObjectName("Calibrator_GroupBox_Visualization")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Calibrator_GroupBox_Visualization)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 213, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Visualization_VerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Visualization_VerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Visualization_VerticalLayout.setObjectName("Visualization_VerticalLayout")
        self.Visualization_RadioButton_Counts_ADC = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Visualization_RadioButton_Counts_ADC.setFont(font)
        self.Visualization_RadioButton_Counts_ADC.setObjectName("Visualization_RadioButton_Counts_ADC")
        self.Visualization_VerticalLayout.addWidget(self.Visualization_RadioButton_Counts_ADC)
        self.Visualization_RadioButton_Counts_ADC_fitting = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Visualization_RadioButton_Counts_ADC_fitting.setFont(font)
        self.Visualization_RadioButton_Counts_ADC_fitting.setObjectName("Visualization_RadioButton_Counts_ADC_fitting")
        self.Visualization_VerticalLayout.addWidget(self.Visualization_RadioButton_Counts_ADC_fitting)
        self.Calibrator_GroupBox_Module_Sensor = QtWidgets.QGroupBox(self.centralwidget)
        self.Calibrator_GroupBox_Module_Sensor.setGeometry(QtCore.QRect(310, 430, 251, 231))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Calibrator_GroupBox_Module_Sensor.setFont(font)
        self.Calibrator_GroupBox_Module_Sensor.setObjectName("Calibrator_GroupBox_Module_Sensor")
        self.Calibrator_GroupBox_Master = QtWidgets.QGroupBox(self.Calibrator_GroupBox_Module_Sensor)
        self.Calibrator_GroupBox_Master.setGeometry(QtCore.QRect(10, 30, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Calibrator_GroupBox_Master.setFont(font)
        self.Calibrator_GroupBox_Master.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Calibrator_GroupBox_Master.setFlat(False)
        self.Calibrator_GroupBox_Master.setCheckable(True)
        self.Calibrator_GroupBox_Master.setChecked(False)
        self.Calibrator_GroupBox_Master.setObjectName("Calibrator_GroupBox_Master")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Calibrator_GroupBox_Master)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 205, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Master_GridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Master_GridLayout.setContentsMargins(0, 0, 0, 0)
        self.Master_GridLayout.setObjectName("Master_GridLayout")
        self.Master_CheckBox_Sensor3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Master_CheckBox_Sensor3.setFont(font)
        self.Master_CheckBox_Sensor3.setObjectName("Master_CheckBox_Sensor3")
        self.Master_GridLayout.addWidget(self.Master_CheckBox_Sensor3, 1, 0, 1, 1)
        self.Master_CheckBox_Sensor2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Master_CheckBox_Sensor2.setFont(font)
        self.Master_CheckBox_Sensor2.setObjectName("Master_CheckBox_Sensor2")
        self.Master_GridLayout.addWidget(self.Master_CheckBox_Sensor2, 0, 1, 1, 1)
        self.Master_CheckBox_Sensor4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Master_CheckBox_Sensor4.setFont(font)
        self.Master_CheckBox_Sensor4.setObjectName("Master_CheckBox_Sensor4")
        self.Master_GridLayout.addWidget(self.Master_CheckBox_Sensor4, 1, 1, 1, 1)
        self.Master_CheckBox_Sensor1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Master_CheckBox_Sensor1.setFont(font)
        self.Master_CheckBox_Sensor1.setObjectName("Master_CheckBox_Sensor1")
        self.Master_GridLayout.addWidget(self.Master_CheckBox_Sensor1, 0, 0, 1, 1)
        self.Calibrator_GroupBox_Slave = QtWidgets.QGroupBox(self.Calibrator_GroupBox_Module_Sensor)
        self.Calibrator_GroupBox_Slave.setGeometry(QtCore.QRect(10, 130, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Calibrator_GroupBox_Slave.setFont(font)
        self.Calibrator_GroupBox_Slave.setFlat(False)
        self.Calibrator_GroupBox_Slave.setCheckable(True)
        self.Calibrator_GroupBox_Slave.setChecked(False)
        self.Calibrator_GroupBox_Slave.setObjectName("Calibrator_GroupBox_Slave")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Calibrator_GroupBox_Slave)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 205, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.Slave_GridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.Slave_GridLayout.setContentsMargins(0, 0, 0, 0)
        self.Slave_GridLayout.setObjectName("Slave_GridLayout")
        self.Slave_CheckBox_Sensor3 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Slave_CheckBox_Sensor3.setFont(font)
        self.Slave_CheckBox_Sensor3.setObjectName("Slave_CheckBox_Sensor3")
        self.Slave_GridLayout.addWidget(self.Slave_CheckBox_Sensor3, 1, 0, 1, 1)
        self.Slave_CheckBox_Sensor2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Slave_CheckBox_Sensor2.setFont(font)
        self.Slave_CheckBox_Sensor2.setObjectName("Slave_CheckBox_Sensor2")
        self.Slave_GridLayout.addWidget(self.Slave_CheckBox_Sensor2, 0, 1, 1, 1)
        self.Slave_CheckBox_Sensor4 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Slave_CheckBox_Sensor4.setFont(font)
        self.Slave_CheckBox_Sensor4.setObjectName("Slave_CheckBox_Sensor4")
        self.Slave_GridLayout.addWidget(self.Slave_CheckBox_Sensor4, 1, 1, 1, 1)
        self.Slave_CheckBox_Sensor1 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Slave_CheckBox_Sensor1.setFont(font)
        self.Slave_CheckBox_Sensor1.setObjectName("Slave_CheckBox_Sensor1")
        self.Slave_GridLayout.addWidget(self.Slave_CheckBox_Sensor1, 0, 0, 1, 1)
        self.Calibrator_GroupBox_FittingSetup = QtWidgets.QGroupBox(self.centralwidget)
        self.Calibrator_GroupBox_FittingSetup.setGeometry(QtCore.QRect(570, 430, 191, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Calibrator_GroupBox_FittingSetup.setFont(font)
        self.Calibrator_GroupBox_FittingSetup.setObjectName("Calibrator_GroupBox_FittingSetup")
        self.Peak1_GroupBox = QtWidgets.QGroupBox(self.Calibrator_GroupBox_FittingSetup)
        self.Peak1_GroupBox.setGeometry(QtCore.QRect(10, 30, 171, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak1_GroupBox.setFont(font)
        self.Peak1_GroupBox.setCheckable(True)
        self.Peak1_GroupBox.setChecked(False)
        self.Peak1_GroupBox.setObjectName("Peak1_GroupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Peak1_GroupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 151, 64))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Peak1_VerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Peak1_VerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Peak1_VerticalLayout.setObjectName("Peak1_VerticalLayout")
        self.Peak1_HorizontalLayout_Xmin = QtWidgets.QHBoxLayout()
        self.Peak1_HorizontalLayout_Xmin.setObjectName("Peak1_HorizontalLayout_Xmin")
        self.Peak1_Xmin = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak1_Xmin.setFont(font)
        self.Peak1_Xmin.setObjectName("Peak1_Xmin")
        self.Peak1_HorizontalLayout_Xmin.addWidget(self.Peak1_Xmin)
        self.Peak1_Xmin_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak1_Xmin_input.setFont(font)
        self.Peak1_Xmin_input.setObjectName("Peak1_Xmin_input")
        self.Peak1_HorizontalLayout_Xmin.addWidget(self.Peak1_Xmin_input)
        self.Peak1_VerticalLayout.addLayout(self.Peak1_HorizontalLayout_Xmin)
        self.Peak1_HorizontalLayout_Xmax = QtWidgets.QHBoxLayout()
        self.Peak1_HorizontalLayout_Xmax.setObjectName("Peak1_HorizontalLayout_Xmax")
        self.Peak1_Xmax = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak1_Xmax.setFont(font)
        self.Peak1_Xmax.setObjectName("Peak1_Xmax")
        self.Peak1_HorizontalLayout_Xmax.addWidget(self.Peak1_Xmax)
        self.Peak1_Xmax_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak1_Xmax_input.setFont(font)
        self.Peak1_Xmax_input.setObjectName("Peak1_Xmax_input")
        self.Peak1_HorizontalLayout_Xmax.addWidget(self.Peak1_Xmax_input)
        self.Peak1_VerticalLayout.addLayout(self.Peak1_HorizontalLayout_Xmax)
        self.Peak2_GroupBox = QtWidgets.QGroupBox(self.Calibrator_GroupBox_FittingSetup)
        self.Peak2_GroupBox.setGeometry(QtCore.QRect(10, 130, 171, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak2_GroupBox.setFont(font)
        self.Peak2_GroupBox.setCheckable(True)
        self.Peak2_GroupBox.setChecked(False)
        self.Peak2_GroupBox.setObjectName("Peak2_GroupBox")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.Peak2_GroupBox)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 30, 151, 64))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.Peak2_VerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.Peak2_VerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Peak2_VerticalLayout.setObjectName("Peak2_VerticalLayout")
        self.Peak2_HorizontalLayout_Xmin = QtWidgets.QHBoxLayout()
        self.Peak2_HorizontalLayout_Xmin.setObjectName("Peak2_HorizontalLayout_Xmin")
        self.Peak2_Xmin = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak2_Xmin.setFont(font)
        self.Peak2_Xmin.setObjectName("Peak2_Xmin")
        self.Peak2_HorizontalLayout_Xmin.addWidget(self.Peak2_Xmin)
        self.Peak2_Xmin_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak2_Xmin_input.setFont(font)
        self.Peak2_Xmin_input.setObjectName("Peak2_Xmin_input")
        self.Peak2_HorizontalLayout_Xmin.addWidget(self.Peak2_Xmin_input)
        self.Peak2_VerticalLayout.addLayout(self.Peak2_HorizontalLayout_Xmin)
        self.Peak2_HorizontalLayout_Xmax = QtWidgets.QHBoxLayout()
        self.Peak2_HorizontalLayout_Xmax.setObjectName("Peak2_HorizontalLayout_Xmax")
        self.Peak2_Xmax = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak2_Xmax.setFont(font)
        self.Peak2_Xmax.setObjectName("Peak2_Xmax")
        self.Peak2_HorizontalLayout_Xmax.addWidget(self.Peak2_Xmax)
        self.Peak2_Xmax_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Peak2_Xmax_input.setFont(font)
        self.Peak2_Xmax_input.setObjectName("Peak2_Xmax_input")
        self.Peak2_HorizontalLayout_Xmax.addWidget(self.Peak2_Xmax_input)
        self.Peak2_VerticalLayout.addLayout(self.Peak2_HorizontalLayout_Xmax)
        self.Calibrator_GroupBox_PlottingSetup = QtWidgets.QGroupBox(self.centralwidget)
        self.Calibrator_GroupBox_PlottingSetup.setGeometry(QtCore.QRect(70, 540, 231, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Calibrator_GroupBox_PlottingSetup.setFont(font)
        self.Calibrator_GroupBox_PlottingSetup.setObjectName("Calibrator_GroupBox_PlottingSetup")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Calibrator_GroupBox_PlottingSetup)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 211, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.PlottingSetup_VerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.PlottingSetup_VerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PlottingSetup_VerticalLayout.setObjectName("PlottingSetup_VerticalLayout")
        self.PlottingSetup_HorizontalLayout_Xmin = QtWidgets.QHBoxLayout()
        self.PlottingSetup_HorizontalLayout_Xmin.setObjectName("PlottingSetup_HorizontalLayout_Xmin")
        self.PlottingSetup_Xmin = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.PlottingSetup_Xmin.setFont(font)
        self.PlottingSetup_Xmin.setObjectName("PlottingSetup_Xmin")
        self.PlottingSetup_HorizontalLayout_Xmin.addWidget(self.PlottingSetup_Xmin)
        self.PlottingSetup_LineEdit_Xmin = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.PlottingSetup_LineEdit_Xmin.setFont(font)
        self.PlottingSetup_LineEdit_Xmin.setObjectName("PlottingSetup_LineEdit_Xmin")
        self.PlottingSetup_HorizontalLayout_Xmin.addWidget(self.PlottingSetup_LineEdit_Xmin)
        self.PlottingSetup_VerticalLayout.addLayout(self.PlottingSetup_HorizontalLayout_Xmin)
        self.PlottingSetup_HorizontalLayout_Xmax = QtWidgets.QHBoxLayout()
        self.PlottingSetup_HorizontalLayout_Xmax.setObjectName("PlottingSetup_HorizontalLayout_Xmax")
        self.PlottingSetup_Xmax = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.PlottingSetup_Xmax.setFont(font)
        self.PlottingSetup_Xmax.setObjectName("PlottingSetup_Xmax")
        self.PlottingSetup_HorizontalLayout_Xmax.addWidget(self.PlottingSetup_Xmax)
        self.PlottingSetup_LineEdit_Xmax = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.PlottingSetup_LineEdit_Xmax.setFont(font)
        self.PlottingSetup_LineEdit_Xmax.setObjectName("PlottingSetup_LineEdit_Xmax")
        self.PlottingSetup_HorizontalLayout_Xmax.addWidget(self.PlottingSetup_LineEdit_Xmax)
        self.PlottingSetup_VerticalLayout.addLayout(self.PlottingSetup_HorizontalLayout_Xmax)
        self.PlottingSetup_HorizontalLayout_Ymin = QtWidgets.QHBoxLayout()
        self.PlottingSetup_HorizontalLayout_Ymin.setObjectName("PlottingSetup_HorizontalLayout_Ymin")
        self.PlottingSetup_Ymin = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.PlottingSetup_Ymin.setFont(font)
        self.PlottingSetup_Ymin.setObjectName("PlottingSetup_Ymin")
        self.PlottingSetup_HorizontalLayout_Ymin.addWidget(self.PlottingSetup_Ymin)
        self.PlottingSetup_LineEdit_Ymin = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.PlottingSetup_LineEdit_Ymin.setFont(font)
        self.PlottingSetup_LineEdit_Ymin.setObjectName("PlottingSetup_LineEdit_Ymin")
        self.PlottingSetup_HorizontalLayout_Ymin.addWidget(self.PlottingSetup_LineEdit_Ymin)
        self.PlottingSetup_VerticalLayout.addLayout(self.PlottingSetup_HorizontalLayout_Ymin)
        self.PlottingSetup_HorizontalLayout_Ymax = QtWidgets.QHBoxLayout()
        self.PlottingSetup_HorizontalLayout_Ymax.setObjectName("PlottingSetup_HorizontalLayout_Ymax")
        self.PlottingSetup_Ymax = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.PlottingSetup_Ymax.setFont(font)
        self.PlottingSetup_Ymax.setObjectName("PlottingSetup_Ymax")
        self.PlottingSetup_HorizontalLayout_Ymax.addWidget(self.PlottingSetup_Ymax)
        self.PlottingSetup_LineEdit_Ymax = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.PlottingSetup_LineEdit_Ymax.setFont(font)
        self.PlottingSetup_LineEdit_Ymax.setObjectName("PlottingSetup_LineEdit_Ymax")
        self.PlottingSetup_HorizontalLayout_Ymax.addWidget(self.PlottingSetup_LineEdit_Ymax)
        self.PlottingSetup_VerticalLayout.addLayout(self.PlottingSetup_HorizontalLayout_Ymax)
        self.Plotting_Widget = QtWidgets.QWidget(self.centralwidget)
        self.Plotting_Widget.setGeometry(QtCore.QRect(430, 690, 331, 41))
        self.Plotting_Widget.setObjectName("Plotting_Widget")
        self.Plot_Status = QtWidgets.QLabel(self.Plotting_Widget)
        self.Plot_Status.setGeometry(QtCore.QRect(240, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Plot_Status.setFont(font)
        self.Plot_Status.setObjectName("Plot_Status")
        self.Plot_progressBar = QtWidgets.QProgressBar(self.Plotting_Widget)
        self.Plot_progressBar.setGeometry(QtCore.QRect(100, 0, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Plot_progressBar.setFont(font)
        self.Plot_progressBar.setProperty("value", 24)
        self.Plot_progressBar.setObjectName("Plot_progressBar")
        self.Plot_Button = QtWidgets.QPushButton(self.Plotting_Widget)
        self.Plot_Button.setGeometry(QtCore.QRect(0, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.Plot_Button.setFont(font)
        self.Plot_Button.setObjectName("Plot_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "GTM - SDC"))
        self.Decode_Modes_CheckBox_Sci.setText(_translate("MainWindow", "Science Data → Export Modes:"))
        self.Decoder_Button.setText(_translate("MainWindow", "Decoder"))
        self.Calibrator_Button.setText(_translate("MainWindow", "Calibrator"))
        self.InputFile_Decoder_Text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:13pt;\"><br /></p></body></html>"))
        self.InputFile_Decoder_Button.setText(_translate("MainWindow", "Input File"))
        self.Decode_Modes_Text.setText(_translate("MainWindow", "Decode Modes:"))
        self.Decode_Modes_CheckBox_TMTC.setText(_translate("MainWindow", "Telemetry Data"))
        self.Export_Modes_CheckBox_Sci_Raw.setText(_translate("MainWindow", "Raw Format"))
        self.Export_Modes_CheckBox_Sci_Pipeline.setText(_translate("MainWindow", "Pipeline Format"))
        self.Export_Modes_CheckBox_Sci_Both.setText(_translate("MainWindow", "Both"))
        self.Start_Button.setText(_translate("MainWindow", "START"))
        self.Start_Status.setText(_translate("MainWindow", "Complete!"))
        self.Hit_Selection_CheckBox_Hit.setText(_translate("MainWindow", "Hit Event"))
        self.Hit_Selection_Text.setText(_translate("MainWindow", "Hit Selection:"))
        self.Hit_Selection_CheckBox_NoHit.setText(_translate("MainWindow", "No Hit Event (for checking)"))
        self.Extract_NSPO_CheckBox.setText(_translate("MainWindow", "Extract NSPO Header"))
        self.InputFile_Calibrator_Button.setText(_translate("MainWindow", "Input File"))
        self.InputFile_Calibrator_Text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:13pt;\"><br /></p></body></html>"))
        self.Calibrator_GroupBox_Visualization.setTitle(_translate("MainWindow", "Visualization Cases:"))
        self.Visualization_RadioButton_Counts_ADC.setText(_translate("MainWindow", "Counts vs. ADC"))
        self.Visualization_RadioButton_Counts_ADC_fitting.setText(_translate("MainWindow", "Counts vs. ADC (fitting)"))
        self.Calibrator_GroupBox_Module_Sensor.setTitle(_translate("MainWindow", "Module and Sensor:"))
        self.Calibrator_GroupBox_Master.setTitle(_translate("MainWindow", "Master"))
        self.Master_CheckBox_Sensor3.setText(_translate("MainWindow", "Sensor 3"))
        self.Master_CheckBox_Sensor2.setText(_translate("MainWindow", "Sensor 2"))
        self.Master_CheckBox_Sensor4.setText(_translate("MainWindow", "Sensor 4"))
        self.Master_CheckBox_Sensor1.setText(_translate("MainWindow", "Sensor 1"))
        self.Calibrator_GroupBox_Slave.setTitle(_translate("MainWindow", "Slave"))
        self.Slave_CheckBox_Sensor3.setText(_translate("MainWindow", "Sensor 3"))
        self.Slave_CheckBox_Sensor2.setText(_translate("MainWindow", "Sensor 2"))
        self.Slave_CheckBox_Sensor4.setText(_translate("MainWindow", "Sensor 4"))
        self.Slave_CheckBox_Sensor1.setText(_translate("MainWindow", "Sensor 1"))
        self.Calibrator_GroupBox_FittingSetup.setTitle(_translate("MainWindow", "Fitting Setup:"))
        self.Peak1_GroupBox.setTitle(_translate("MainWindow", "Peak 1"))
        self.Peak1_Xmin.setText(_translate("MainWindow", "X min :"))
        self.Peak1_Xmax.setText(_translate("MainWindow", "X max:"))
        self.Peak2_GroupBox.setTitle(_translate("MainWindow", "Peak 2"))
        self.Peak2_Xmin.setText(_translate("MainWindow", "X min :"))
        self.Peak2_Xmax.setText(_translate("MainWindow", "X max:"))
        self.Calibrator_GroupBox_PlottingSetup.setTitle(_translate("MainWindow", "Plotting Setup:"))
        self.PlottingSetup_Xmin.setText(_translate("MainWindow", "X min :"))
        self.PlottingSetup_Xmax.setText(_translate("MainWindow", "X max:"))
        self.PlottingSetup_Ymin.setText(_translate("MainWindow", "Y min :"))
        self.PlottingSetup_Ymax.setText(_translate("MainWindow", "Y max:"))
        self.Plot_Status.setText(_translate("MainWindow", "Complete!"))
        self.Plot_Button.setText(_translate("MainWindow", "PLOT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
