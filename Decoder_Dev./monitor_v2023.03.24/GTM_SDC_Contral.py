#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:58:23 2022

@author: jasonpbu
"""

import re
import time
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtWidgets, QtTest
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2

from GTM_SDC_UI import Ui_MainWindow
from GTM_SDC_Contral_C_Decoder import C_Decoder

# # old version using matplotlib
# from GTM_SDC_PlottingWindow import Ui_PlottingWindow
# from GTM_SDC_PlottingFunction import MplCanvas, Loader
# import matplotlib
# matplotlib.use('Qt5Agg')
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        ### GTM icon ###
        self.img_path = 'GTM_icon.png'
        self.Display_Img()
        
        ### Decoder ###
        self.ui.Decoder_Button.clicked.connect(self.ButtonClicked_Decoder)
        self.Clicked_Counter_Decoder = 0
        
        # Decoder On or Off
        self.Decoder_OnOff()
        
        # Decoder Input File
        self.ui.InputFile_Decoder_Button.clicked.connect(self.Decoder_Open_File)
        self.Input_Decoder_Filename = []
        self.Input_Decoder_Filetype = ""
        
        # Decode Modes
        self.ui.Decode_Modes_CheckBox_Sci.clicked.connect(self.Sci_CheckBoxClick)
        self.ui.Decode_Modes_CheckBox_TMTC.clicked.connect(self.TMTC_CheckBoxClick)
        self.Decode_Modes = 0
        
        # Extract Selection for Sci Export Modes
        self.ui.Extract_NSPO_CheckBox.clicked.connect(self.Extract_CheckBoxClick)
        self.Extract_Selection = 0
        
        # Sci Export Modes
        self.ui.Export_Modes_CheckBox_Sci_Raw.clicked.connect(self.Sci_Raw_CheckBoxClick)
        self.ui.Export_Modes_CheckBox_Sci_Pipeline.clicked.connect(self.Sci_Pipeline_CheckBoxClick)
        self.ui.Export_Modes_CheckBox_Sci_Both.clicked.connect(self.Sci_Both_CheckBoxClick)
        self.Export_Modes = 0

        # Monitor Modes
        self.ui.Monitor_Modes_radioButton_Plotting.clicked.connect(self.Monitor_OnOff)
        self.ui.Monitor_Modes_radioButton_Silence.clicked.connect(self.Monitor_OnOff)
        self.Monitor_Modes = 0 # 1 for TMTC, 2 foe SD

        # Module and Sensor Selection
        self.ui.Master_GroupBox.clicked.connect(self.Module_Sensor_OnOff)
        self.ui.Slave_GroupBox.clicked.connect(self.Module_Sensor_OnOff)
        self.Plotting_Module_list = []

        self.ui.Master_CheckBox_Sensor1.clicked.connect(self.Start_OnOff)
        self.ui.Master_CheckBox_Sensor2.clicked.connect(self.Start_OnOff)
        self.ui.Master_CheckBox_Sensor3.clicked.connect(self.Start_OnOff)
        self.ui.Master_CheckBox_Sensor4.clicked.connect(self.Start_OnOff)
        self.Plotting_Master_Sensor_list = []

        self.ui.Slave_CheckBox_Sensor1.clicked.connect(self.Start_OnOff)
        self.ui.Slave_CheckBox_Sensor2.clicked.connect(self.Start_OnOff)
        self.ui.Slave_CheckBox_Sensor3.clicked.connect(self.Start_OnOff)
        self.ui.Slave_CheckBox_Sensor4.clicked.connect(self.Start_OnOff)
        self.Plotting_Slave_Sensor_list = []

        # Define Plotting Variables
        self.low_gain  = 2
        self.high_gain = 20
        self.Initailize_Plotting_Variables()
        
        # Start Decoding
        self.ui.Start_groupBox.setStyleSheet("QGroupBox{border:none}")
        self.ui.Start_Button.clicked.connect(self.ButtonClicked_Start)
        
    def Display_Img(self):
        self.img = cv2.imread(self.img_path)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        self.qpixmap_height -= 210
        scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        self.ui.GTM_ICON.setPixmap(scaled_pixmap)
    
    def ButtonClicked_Decoder(self):
        self.Clicked_Counter_Decoder += 1
        if (self.Clicked_Counter_Decoder%2) != 0:
            self.ui.Decoder_Button.setStyleSheet("background-color: #2B5DD1;"
                                                 "color: #FFFFFF;"
                                                 "border-style: outset;"
                                                 "padding: 2px;"
                                                 "font: bold 20px;"
                                                 "border-width: 3px;"
                                                 "border-radius: 10px;"
                                                 "border-color: #2752B8;")
            self.ui.Decoder_Button_Status.setText("Decoder Selected!")
        else:
            self.ui.Decoder_Button.setStyleSheet("")
            self.ui.Decoder_Button_Status.setText("     ")
        self.Decoder_OnOff()
        
    def Decoder_OnOff(self):
        if (self.Clicked_Counter_Decoder%2) != 0:
            self.ui.InputFile_Decoder_Button.setEnabled(True)
            self.ui.InputFile_Decoder_Text.setEnabled(True)
            
            self.ui.Decode_Modes_Text.setEnabled(True)
            self.ui.Decode_Modes_CheckBox_Sci.setEnabled(True)
            self.ui.Extract_NSPO_CheckBox.setEnabled(True)
            self.ui.Decode_Modes_CheckBox_TMTC.setEnabled(True)
            
            self.Sci_OnOff()
        else:
            self.ui.InputFile_Decoder_Button.setEnabled(False)
            self.ui.InputFile_Decoder_Text.setEnabled(False)
            
            self.ui.Decode_Modes_Text.setEnabled(False)
            self.ui.Decode_Modes_CheckBox_Sci.setEnabled(False)
            self.ui.Extract_NSPO_CheckBox.setEnabled(False)
            self.ui.Decode_Modes_CheckBox_TMTC.setEnabled(False)
            
            self.ui.Export_Modes_CheckBox_Sci_Raw.setEnabled(False)
            self.ui.Export_Modes_CheckBox_Sci_Pipeline.setEnabled(False)
            self.ui.Export_Modes_CheckBox_Sci_Both.setEnabled(False)

            self.ui.Monitor_Modes_Group.setEnabled(False)
            self.ui.Module_Sensor_GroupBox.setEnabled(False)
            
            self.ui.Start_groupBox.setEnabled(False)
    
    def Decoder_Open_File(self):
        self.Input_Decoder_Filename, self.Input_Decoder_Filetype = QFileDialog.getOpenFileNames(self, "Open file", "./")

        if len(self.Input_Decoder_Filename) == 1:
            self.ui.InputFile_Decoder_Text.setText(self.Input_Decoder_Filename[0])
        
        if len(self.Input_Decoder_Filename) > 1:
            Input_Decoder_Filename_print = ""
            for Input_Decoder_Filename_print_temp in self.Input_Decoder_Filename:
                Input_Decoder_Filename_print += Input_Decoder_Filename_print_temp + ";"
            self.ui.InputFile_Decoder_Text.setText(Input_Decoder_Filename_print)

        self.Start_OnOff()
    
    def Sci_CheckBoxClick(self):
        if self.ui.Decode_Modes_CheckBox_Sci.isChecked():
            self.ui.Decode_Modes_CheckBox_TMTC.setChecked(False)
            self.Decode_Modes = 1
        else:
            self.Decode_Modes = 0

        self.Sci_OnOff()
        
    def TMTC_CheckBoxClick(self):
        if self.ui.Decode_Modes_CheckBox_TMTC.isChecked():
            self.ui.Decode_Modes_CheckBox_Sci.setChecked(False)
            self.Decode_Modes = 2
        else:
            self.Decode_Modes = 0

        self.Sci_OnOff()
        
    def Sci_OnOff(self):
        if self.ui.Decode_Modes_CheckBox_Sci.isChecked():
            self.ui.Extract_NSPO_CheckBox.setEnabled(True)
            
            self.ui.Export_Modes_CheckBox_Sci_Raw.setEnabled(True)
            self.ui.Export_Modes_CheckBox_Sci_Pipeline.setEnabled(True)
            self.ui.Export_Modes_CheckBox_Sci_Both.setEnabled(True)
        else:
            self.ui.Extract_NSPO_CheckBox.setEnabled(False)
            
            self.ui.Export_Modes_CheckBox_Sci_Raw.setEnabled(False)
            self.ui.Export_Modes_CheckBox_Sci_Pipeline.setEnabled(False)
            self.ui.Export_Modes_CheckBox_Sci_Both.setEnabled(False)

        self.Monitor_OnOff()
        
    def Extract_CheckBoxClick(self):
        if self.ui.Extract_NSPO_CheckBox.isChecked():
            self.Extract_Selection = 1
        else:
            self.Extract_Selection = 0

        self.Monitor_OnOff()
    
    def Sci_Raw_CheckBoxClick(self):
        if self.ui.Export_Modes_CheckBox_Sci_Raw.isChecked():
            self.ui.Export_Modes_CheckBox_Sci_Pipeline.setChecked(False)
            self.ui.Export_Modes_CheckBox_Sci_Both.setChecked(False)
            self.Export_Modes = 1
        else:
            self.Export_Modes = 0
        
        self.Monitor_OnOff()
    
    def Sci_Pipeline_CheckBoxClick(self):
        if self.ui.Export_Modes_CheckBox_Sci_Pipeline.isChecked():
            self.ui.Export_Modes_CheckBox_Sci_Raw.setChecked(False)
            self.ui.Export_Modes_CheckBox_Sci_Both.setChecked(False)
            self.Export_Modes = 2
        else:
            self.Export_Modes = 0
        
        self.Monitor_OnOff()
    
    def Sci_Both_CheckBoxClick(self):
        if self.ui.Export_Modes_CheckBox_Sci_Both.isChecked():
            self.ui.Export_Modes_CheckBox_Sci_Raw.setChecked(False)
            self.ui.Export_Modes_CheckBox_Sci_Pipeline.setChecked(False)
            self.Export_Modes = 3
        else:
            self.Export_Modes = 0
        
        self.Monitor_OnOff()
    
    def Monitor_OnOff(self):
        if self.Input_Decoder_Filename != []:
            if self.ui.Decode_Modes_CheckBox_TMTC.isChecked():
                self.ui.Monitor_Modes_Group.setEnabled(True)
            elif self.ui.Decode_Modes_CheckBox_Sci.isChecked():
                if self.ui.Export_Modes_CheckBox_Sci_Raw.isChecked():
                    self.ui.Monitor_Modes_Group.setEnabled(True)
                elif self.ui.Export_Modes_CheckBox_Sci_Pipeline.isChecked():
                    self.ui.Monitor_Modes_Group.setEnabled(True)
                elif self.ui.Export_Modes_CheckBox_Sci_Both.isChecked():
                    self.ui.Monitor_Modes_Group.setEnabled(True)
                else:
                    self.ui.Monitor_Modes_Group.setEnabled(False)
            else:
                self.ui.Monitor_Modes_Group.setEnabled(False)
        else:
            self.ui.Monitor_Modes_Group.setEnabled(False)

        self.Module_Sensor_OnOff()

    def Module_Sensor_OnOff(self):
        if self.ui.Decode_Modes_CheckBox_TMTC.isChecked(): 
            if self.ui.Monitor_Modes_radioButton_Plotting.isChecked():
                self.ui.Module_Sensor_GroupBox.setEnabled(True)
                self.ui.Master_CheckBox_Sensor1.setEnabled(False)
                self.ui.Master_CheckBox_Sensor2.setEnabled(False)
                self.ui.Master_CheckBox_Sensor3.setEnabled(False)
                self.ui.Master_CheckBox_Sensor4.setEnabled(False)
                self.ui.Slave_CheckBox_Sensor1.setEnabled(False)
                self.ui.Slave_CheckBox_Sensor2.setEnabled(False)
                self.ui.Slave_CheckBox_Sensor3.setEnabled(False)
                self.ui.Slave_CheckBox_Sensor4.setEnabled(False)
            else:
                self.ui.Module_Sensor_GroupBox.setEnabled(False)
        elif self.ui.Decode_Modes_CheckBox_Sci.isChecked():
            if self.ui.Monitor_Modes_Group.isEnabled():
                if self.ui.Monitor_Modes_radioButton_Plotting.isChecked():
                    self.ui.Module_Sensor_GroupBox.setEnabled(True)
                    self.ui.Master_CheckBox_Sensor1.setEnabled(True)
                    self.ui.Master_CheckBox_Sensor2.setEnabled(True)
                    self.ui.Master_CheckBox_Sensor3.setEnabled(True)
                    self.ui.Master_CheckBox_Sensor4.setEnabled(True)
                    self.ui.Slave_CheckBox_Sensor1.setEnabled(True)
                    self.ui.Slave_CheckBox_Sensor2.setEnabled(True)
                    self.ui.Slave_CheckBox_Sensor3.setEnabled(True)
                    self.ui.Slave_CheckBox_Sensor4.setEnabled(True)
                else:
                    self.ui.Module_Sensor_GroupBox.setEnabled(False)
            else:
                self.ui.Module_Sensor_GroupBox.setEnabled(False)
        else:
            self.ui.Module_Sensor_GroupBox.setEnabled(False)

        self.Start_OnOff()

    def Start_OnOff(self):
        if self.Input_Decoder_Filename != []:
            if self.ui.Decode_Modes_CheckBox_TMTC.isChecked():
                if self.ui.Monitor_Modes_radioButton_Silence.isChecked():
                    self.Monitor_Modes = 0
                    self.ui.Start_groupBox.setEnabled(True)
                elif self.ui.Monitor_Modes_radioButton_Plotting.isChecked():
                    if self.ui.Master_GroupBox.isChecked():
                        self.Monitor_Modes = 1
                        self.ui.Start_groupBox.setEnabled(True)
                    elif self.ui.Slave_GroupBox.isChecked():
                        self.Monitor_Modes = 1
                        self.ui.Start_groupBox.setEnabled(True)
                    else:
                        self.ui.Start_groupBox.setEnabled(False)
                else:
                    self.ui.Start_groupBox.setEnabled(False)
            elif self.ui.Decode_Modes_CheckBox_Sci.isChecked():
                if self.ui.Monitor_Modes_Group.isEnabled():
                    if self.ui.Monitor_Modes_radioButton_Silence.isChecked():
                        self.Monitor_Modes = 0
                        self.ui.Start_groupBox.setEnabled(True)
                    elif self.ui.Monitor_Modes_radioButton_Plotting.isChecked():
                        if self.ui.Master_GroupBox.isChecked():
                            if self.ui.Master_CheckBox_Sensor1.isChecked() or self.ui.Master_CheckBox_Sensor2.isChecked()\
                            or self.ui.Master_CheckBox_Sensor3.isChecked() or self.ui.Master_CheckBox_Sensor4.isChecked():
                                self.Monitor_Modes = 2
                                self.ui.Start_groupBox.setEnabled(True)
                            else:
                                self.ui.Start_groupBox.setEnabled(False)
                        elif self.ui.Slave_GroupBox.isChecked():
                            if self.ui.Slave_CheckBox_Sensor1.isChecked() or self.ui.Slave_CheckBox_Sensor2.isChecked()\
                            or self.ui.Slave_CheckBox_Sensor3.isChecked() or self.ui.Slave_CheckBox_Sensor4.isChecked():
                                self.Monitor_Modes = 2
                                self.ui.Start_groupBox.setEnabled(True)
                            else:
                                self.ui.Start_groupBox.setEnabled(False)
                        else:
                            self.ui.Start_groupBox.setEnabled(False)
                    else:
                        self.ui.Start_groupBox.setEnabled(False)
                else:
                    self.ui.Start_groupBox.setEnabled(False)
            else:
                self.ui.Start_groupBox.setEnabled(False)
        else:
            self.ui.Start_groupBox.setEnabled(False)

    def Initailize_Plotting_Variables(self):
        self.df_tmtc_master = pd.DataFrame()
        self.df_tmtc_master_skip_num = 0
        self.df_tmtc_slave = pd.DataFrame()
        self.df_tmtc_slave_skip_num = 0
        self.df_sd = pd.DataFrame()
        self.df_sd_skip_num = 0
    
    def ButtonClicked_Start(self):
        print("Decoding!")

        # silence mode
        if self.Monitor_Modes == 0:

            # for pure TMTC and SD decoding (only need one file pointer)
            if ((self.Decode_Modes == 1) and (self.Extract_Selection == 0)) or (self.Decode_Modes == 2):
                for Input_Decoder_Filename in self.Input_Decoder_Filename:
                    new_file_pointer = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=0) 
                    print(new_file_pointer)
                    new_file_pointer_cache = new_file_pointer

                    QtTest.QTest.qWait(1000)

                    continue_decode = True
                    while continue_decode:
                        new_file_pointer = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=new_file_pointer_cache) 
                        print(new_file_pointer)

                        if new_file_pointer == new_file_pointer_cache:
                            break
                        else:
                            new_file_pointer_cache = new_file_pointer
                            QtTest.QTest.qWait(10000)
            
            # for SD (with header and tail) decoding ( need two file pointers)
            if (self.Decode_Modes == 1) and (self.Extract_Selection == 1):
                for Input_Decoder_Filename in self.Input_Decoder_Filename:
                    new_file_pointer_extract = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=0) 
                    print(new_file_pointer_extract)
                    new_file_pointer_extract_cache = new_file_pointer_extract

                    Input_Decoder_Filename_extracted = Input_Decoder_Filename.replace('.bin','_extracted.bin')
                    new_file_pointer_decode = C_Decoder(Input_Decoder_Filename_extracted, self.Decode_Modes, 0, self.Export_Modes, InitailFilePointer=0) 
                    print(new_file_pointer_decode)
                    new_file_pointer_decode_cache = new_file_pointer_decode

                    QtTest.QTest.qWait(1000)

                    continue_decode = True
                    while continue_decode:
                        new_file_pointer_extract = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=new_file_pointer_extract_cache) 
                        print(new_file_pointer_extract)
                        new_file_pointer_decode = C_Decoder(Input_Decoder_Filename_extracted, self.Decode_Modes, 0, self.Export_Modes, InitailFilePointer=new_file_pointer_decode_cache) 
                        print(new_file_pointer_decode)

                        if (new_file_pointer_extract == new_file_pointer_extract_cache) and (new_file_pointer_decode == new_file_pointer_decode_cache):
                            break
                        else:
                            new_file_pointer_extract_cache = new_file_pointer_extract
                            new_file_pointer_decode_cache = new_file_pointer_decode
                            QtTest.QTest.qWait(10000)

        # TMTC plotting mode
        elif self.Monitor_Modes == 1:

            if self.ui.Master_GroupBox.isChecked():
                self.Plotting_Module_list.append('Master')
                
            if self.ui.Slave_GroupBox.isChecked():
                self.Plotting_Module_list.append('Slave')

            self.Open_PlottingWindow_TMTC()

            # for pure TMTC and SD decoding (only need one file pointer)
            if ((self.Decode_Modes == 1) and (self.Extract_Selection == 0)) or (self.Decode_Modes == 2):
                for Input_Decoder_Filename in self.Input_Decoder_Filename:
                    new_file_pointer = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=0) 
                    print(new_file_pointer)
                    new_file_pointer_cache = new_file_pointer

                    QtTest.QTest.qWait(1000)

                    Input_Decoder_Filename_TMTC_Master = Input_Decoder_Filename.replace('.bin','_tmtc_master.csv')
                    Input_Decoder_Filename_TMTC_Slave = Input_Decoder_Filename.replace('.bin','_tmtc_slave.csv')

                    if self.Plotting_Module_list == ['Master', 'Slave']:
                        self.Plotting_TMTC([Input_Decoder_Filename_TMTC_Master, Input_Decoder_Filename_TMTC_Slave])
                    elif self.Plotting_Module_list == ['Master']:
                        self.Plotting_TMTC([Input_Decoder_Filename_TMTC_Master])
                    elif self.Plotting_Module_list == ['Slave']:
                        self.Plotting_TMTC([Input_Decoder_Filename_TMTC_Slave])
                    else:
                        print(self.Plotting_Module_list)
                        print('Checking ButtonClicked_Start Plotting_TMTC!')

                    continue_decode = True
                    while continue_decode:
                        new_file_pointer = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=new_file_pointer_cache) 
                        print(new_file_pointer)
                        
                        if new_file_pointer == new_file_pointer_cache:
                            self.Plotting_Module_list = []
                            break
                        else:
                            new_file_pointer_cache = new_file_pointer
                            QtTest.QTest.qWait(5000)

                            if self.Plotting_Module_list == ['Master', 'Slave']:
                                self.Updating_Plotting_TMTC([Input_Decoder_Filename_TMTC_Master, Input_Decoder_Filename_TMTC_Slave])
                            elif self.Plotting_Module_list == ['Master']:
                                self.Updating_Plotting_TMTC([Input_Decoder_Filename_TMTC_Master])
                            elif self.Plotting_Module_list == ['Slave']:
                                self.Updating_Plotting_TMTC([Input_Decoder_Filename_TMTC_Slave])
                            else:
                                print('Checking ButtonClicked_Start Updating_Plotting_TMTC!')

        # SD plotting mode
        elif self.Monitor_Modes == 2:

            # for pure TMTC and SD decoding (only need one file pointer)
            if ((self.Decode_Modes == 1) and (self.Extract_Selection == 0)) or (self.Decode_Modes == 2):
                for Input_Decoder_Filename in self.Input_Decoder_Filename:
                    new_file_pointer = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=0) 
                    print(new_file_pointer)
                    new_file_pointer_cache = new_file_pointer

                    QtTest.QTest.qWait(1000)

                    continue_decode = True
                    while continue_decode:
                        new_file_pointer = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=new_file_pointer_cache) 
                        print(new_file_pointer)

                        if new_file_pointer == new_file_pointer_cache:
                            break
                        else:
                            new_file_pointer_cache = new_file_pointer
                            QtTest.QTest.qWait(10000)
            
            # for SD (with header and tail) decoding ( need two file pointers)
            if (self.Decode_Modes == 1) and (self.Extract_Selection == 1):
                for Input_Decoder_Filename in self.Input_Decoder_Filename:
                    new_file_pointer_extract = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=0) 
                    print(new_file_pointer_extract)
                    new_file_pointer_extract_cache = new_file_pointer_extract

                    Input_Decoder_Filename_extracted = Input_Decoder_Filename.replace('.bin','_extracted.bin')
                    new_file_pointer_decode = C_Decoder(Input_Decoder_Filename_extracted, self.Decode_Modes, 0, self.Export_Modes, InitailFilePointer=0) 
                    print(new_file_pointer_decode)
                    new_file_pointer_decode_cache = new_file_pointer_decode

                    QtTest.QTest.qWait(1000)

                    continue_decode = True
                    while continue_decode:
                        new_file_pointer_extract = C_Decoder(Input_Decoder_Filename, self.Decode_Modes, self.Extract_Selection, self.Export_Modes, InitailFilePointer=new_file_pointer_extract_cache) 
                        print(new_file_pointer_extract)
                        new_file_pointer_decode = C_Decoder(Input_Decoder_Filename_extracted, self.Decode_Modes, 0, self.Export_Modes, InitailFilePointer=new_file_pointer_decode_cache) 
                        print(new_file_pointer_decode)

                        if (new_file_pointer_extract == new_file_pointer_extract_cache) and (new_file_pointer_decode == new_file_pointer_decode_cache):
                            break
                        else:
                            new_file_pointer_extract_cache = new_file_pointer_extract
                            new_file_pointer_decode_cache = new_file_pointer_decode
                            QtTest.QTest.qWait(1000)
            
            else:
                print('Checking Monitor Modes!')

    def Open_PlottingWindow_TMTC(self):

        # Create layout to hold multiple subplots
        self.pg_layout = pg.GraphicsLayoutWidget()
        self.pg_layout.showMaximized()

    def Plotting_TMTC(self, FilenameList):
        print('Plotting TMTC!')

        self.Initailize_Plotting_Variables()

        if self.Plotting_Module_list == ['Master', 'Slave']:
            # load data
            self.df_tmtc_master, self.df_tmtc_master_skip_num = self.Loader(FilenameList[0], self.df_tmtc_master, self.df_tmtc_master_skip_num)
            self.df_tmtc_slave, self.df_tmtc_slave_skip_num = self.Loader(FilenameList[1], self.df_tmtc_slave, self.df_tmtc_slave_skip_num)
            
            # Add subplots
            self.df_tmtc_master_pg_layout = self.pg_layout.addPlot(row=0, col=0, title="Master Board Temperature#1", labels={'left': 'Temperature [°C]', 'bottom': 'Dummy Count [#]'})
            self.df_tmtc_slave_pg_layout = self.pg_layout.addPlot(row=0, col=1, title="Slave Board Temperature#1", labels={'left': 'Temperature [°C]', 'bottom': 'Dummy Count [#]'})

            # plotting
            self.df_tmtc_master_data_line = self.df_tmtc_master_pg_layout.plot(np.arange(len(self.df_tmtc_master['Board Temperature#1'])),self.df_tmtc_master['Board Temperature#1'].to_numpy(), pen=pg.mkPen(color=(255, 0, 0)))
            self.df_tmtc_slave_data_line = self.df_tmtc_slave_pg_layout.plot(np.arange(len(self.df_tmtc_slave['Board Temperature#1'])), self.df_tmtc_slave['Board Temperature#1'].to_numpy(), pen=pg.mkPen(color=(0, 0, 255)))

        elif self.Plotting_Module_list == ['Master']:
            # load data
            self.df_tmtc_master, self.df_tmtc_master_skip_num = self.Loader(FilenameList[0], self.df_tmtc_master, self.df_tmtc_master_skip_num)
            
            # Add subplots
            self.df_tmtc_master_pg_layout = self.pg_layout.addPlot(row=0, col=0, title="Master Board Temperature#1", labels={'left': 'Temperature [°C]', 'bottom': 'Dummy Count [#]'})

            # plotting
            self.df_tmtc_master_data_line = self.df_tmtc_master_pg_layout.plot(np.arange(len(self.df_tmtc_master['Board Temperature#1'])),self.df_tmtc_master['Board Temperature#1'].to_numpy(), pen=pg.mkPen(color=(255, 0, 0)))

        elif self.Plotting_Module_list == ['Slave']:
            # load data
            self.df_tmtc_slave, self.df_tmtc_slave_skip_num = self.Loader(FilenameList[0], self.df_tmtc_slave, self.df_tmtc_slave_skip_num)
            
            # Add subplots
            self.df_tmtc_slave_pg_layout = self.pg_layout.addPlot(row=0, col=0, title="Slave Board Temperature#1", labels={'left': 'Temperature [°C]', 'bottom': 'Dummy Count [#]'})

            # plotting
            self.df_tmtc_slave_data_line = self.df_tmtc_slave_pg_layout.plot(np.arange(len(self.df_tmtc_slave['Board Temperature#1'])), self.df_tmtc_slave['Board Temperature#1'].to_numpy(), pen=pg.mkPen(color=(0, 0, 255)))

        else:
            print('Checking Plotting_TMTC!')
        
        # Show our layout holding multiple subplots
        self.pg_layout.show()

    def Updating_Plotting_TMTC(self, FilenameList):

        if self.Plotting_Module_list == ['Master', 'Slave']:
            # updating data
            self.df_tmtc_master, self.df_tmtc_master_skip_num = self.Loader(FilenameList[0], self.df_tmtc_master, self.df_tmtc_master_skip_num)
            self.df_tmtc_slave, self.df_tmtc_slave_skip_num = self.Loader(FilenameList[1], self.df_tmtc_slave, self.df_tmtc_slave_skip_num)
            
            # updating plotting
            self.df_tmtc_master_data_line.setData(np.arange(len(self.df_tmtc_master['Board Temperature#1'])), self.df_tmtc_master['Board Temperature#1'].to_numpy())
            self.df_tmtc_slave_data_line.setData(np.arange(len(self.df_tmtc_slave['Board Temperature#1'])), self.df_tmtc_slave['Board Temperature#1'].to_numpy())
        
        elif self.Plotting_Module_list == ['Master']:
            # updating data
            self.df_tmtc_master, self.df_tmtc_master_skip_num = self.Loader(FilenameList[0], self.df_tmtc_master, self.df_tmtc_master_skip_num)
            
            # updating plotting
            self.df_tmtc_master_data_line.setData(np.arange(len(self.df_tmtc_master['Board Temperature#1'])), self.df_tmtc_master['Board Temperature#1'].to_numpy())
        
        elif self.Plotting_Module_list == ['Slave']:
            # updating data
            self.df_tmtc_slave, self.df_tmtc_slave_skip_num = self.Loader(FilenameList[0], self.df_tmtc_slave, self.df_tmtc_slave_skip_num)
            
            # updating plotting
            self.df_tmtc_slave_data_line.setData(np.arange(len(self.df_tmtc_slave['Board Temperature#1'])), self.df_tmtc_slave['Board Temperature#1'].to_numpy())
        
        else:
            print('Checking Updating_Plotting_TMTC!')

    def Loader(self, Filename, DataFrame, SkipNum):
        if SkipNum == 0:
            DataFrame = pd.read_csv(Filename, sep=';')
        else:
            df = pd.read_csv(Filename, sep=';', skiprows=SkipNum)
            df.columns = DataFrame.columns
            DataFrame = pd.concat([DataFrame, df], axis=0, ignore_index=True)
        SkipNum = DataFrame.shape[0]
        return DataFrame, SkipNum



    # # old version using matplotlib

    # def Open_PlottingWindow_TMTC(self):
    #     # basic window setup
    #     self.window_plotting_tmtc = QtWidgets.QMainWindow()
    #     self.ui_plotting_tmtc = Ui_PlottingWindow()
    #     self.ui_plotting_tmtc.setupUi(self.window_plotting_tmtc)

    # def Plotting_TMTC(self, FilenameList):
    #     print('Plotting TMTC!')

    #     # creat figure
    #     sc_tmtc = MplCanvas(self.window_plotting_tmtc)

    #     if self.Plotting_Module_list == ['Master', 'Slave']:
    #         # loading data
    #         self.df_tmtc_master = Loader(FilenameList[0])
    #         self.df_tmtc_slave = Loader(FilenameList[1])
    #         # plotting
    #         for i in range(1, 2+1, 1):
    #             sc_tmtc.axesList.append(sc_tmtc.fig.add_subplot(1, 2, i))
    #         sc_tmtc.axesList[0].plot(range(len(self.df_tmtc_master['Board Temperature#1'])), self.df_tmtc_master['Board Temperature#1'])
    #         sc_tmtc.axesList[1].plot(range(len(self.df_tmtc_slave['Board Temperature#1'])), self.df_tmtc_slave['Board Temperature#1'])
    #     elif self.Plotting_Module_list == ['Master']:
    #         # loading data
    #         self.df_tmtc_master = Loader(FilenameList[0])
    #         # plotting
    #         sc_tmtc.axesList.append(sc_tmtc.fig.add_subplot(1, 1, 1))
    #         sc_tmtc.axesList[0].plot(range(len(self.df_tmtc_master['Board Temperature#1'])), self.df_tmtc_master['Board Temperature#1'])
    #     elif self.Plotting_Module_list == ['Slave']:
    #         # loading data
    #         self.df_tmtc_slave = Loader(FilenameList[0])
    #         # plotting
    #         sc_tmtc.axesList.append(sc_tmtc.fig.add_subplot(1, 1, 1))
    #         sc_tmtc.axesList[0].plot(range(len(self.df_tmtc_slave['Board Temperature#1'])), self.df_tmtc_slave['Board Temperature#1'])
    #     else:
    #         print('Checking!')

    #     # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
    #     toolbar = NavigationToolbar(sc_tmtc, self.window_plotting_tmtc)

    #     layout = QtWidgets.QVBoxLayout()
    #     layout.addWidget(toolbar)
    #     layout.addWidget(sc_tmtc)

    #     # Create a placeholder widget to hold our toolbar and canvas.
    #     widget = QtWidgets.QWidget()
    #     widget.setLayout(layout)
    #     self.window_plotting_tmtc.setCentralWidget(widget)

    #     self.window_plotting_tmtc.show()
            