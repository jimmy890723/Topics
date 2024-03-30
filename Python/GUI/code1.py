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
import APP1

###########################################################################
## Class Start_Frame
###########################################################################
case_number = "100783334"
i = 0

###########################################################################
## Class Cases_score_Frame
###########################################################################

class Cases_score_Frame ( APP1.Cases_score_Frame ):

	def __init__( self, parent ):
		APP1.Cases_score_Frame.__init__ ( self, parent, case_number)


	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def Onclick_Segmentation( self, event): 
		frm = Segmentation_Analysis(None)
		frm.Show()
		app.MainLoop()
	def Onclick_CTSI_Result( self, event):
		frm = CTSI_Analysis(None)
		frm.Show()
		app.MainLoop()

###########################################################################
## Class Segmentation_Analysis
###########################################################################
choose_type = "effusion"
class Segmentation_Analysis ( APP1.Segmentation_Analysis ):

	def __init__( self, parent ):
		APP1.Segmentation_Analysis.__init__ ( self, parent, case_number, choose_type)


	def __del__( self ):
		pass

###########################################################################
## Class CTSI_Analysis
###########################################################################

class CTSI_Analysis ( APP1.CTSI_Analysis ):

	def __init__( self, parent ):
		APP1.CTSI_Analysis.__init__ ( self, parent, case_number)


	def __del__( self ):
		pass


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = Cases_score_Frame(None)
    frm.Show()
    app.MainLoop()

