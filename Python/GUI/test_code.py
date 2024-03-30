# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import sys
import wx
import wx.xrc
import os
import test

###########################################################################
## Parameter
###########################################################################
case_number = 0
i = 0
Nowpath = os.getcwd()
###########################################################################
## Class Second_Frame
###########################################################################

class Second_Frame ( test.Second_Frame ):

	def __init__( self, parent ):
		test.Second_Frame.__init__ ( self, parent, case_number)


	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def Onclick_processing( self, event):
		#這裡我不確定app.MainLoop()需不需要放最後面，它的功能是讓Application的主事件循環
		#self.Close(True)
		#frm = run_yards(None) 	#放讀條的Frame
		#frm.Show()
		#app.MainLoop()
		
		#AI
		sys.path.append(Nowpath + '\\..\\AI')
		import AI
		PATH_TO_DICOM_FILE= Nowpath + '\\..\\..\\Data\\'+ case_number
		print(PATH_TO_DICOM_FILE)
		AI.convert2jpg(PATH_TO_DICOM_FILE)
		
		AI.image_inference()
		
		print('Inference Done... ', end='\n')
		
		#Deal
		sys.path.append(Nowpath + '\\..\\Deal')
		
		import Img_processing_def
		Img_processing_def.Img_processing_def(case_number,'pancreas')
		Img_processing_def.Img_processing_def(case_number,'effusion')
		
		print('Img processing Done... \n')

		#Path
		sys.path.append(Nowpath + '\\..\\Path')

		import straightLine
		print('The Best Path Done... \n')

	def Onclick_result( self, event):
		self.Close(True)
		frm = Result_Frame(None)	#放空白的Frame 
		frm.Show()
		app.MainLoop()

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = Second_Frame(None)
    frm.Show()
    app.MainLoop()
