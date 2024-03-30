# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import bnd_gui as gui
i=0
case_number = 0
###########################################################################
## Class Bnd_Frame
###########################################################################

class Bnd_Frame ( gui.Bnd_Frame ):

	def __init__( self, parent ):
		gui.Bnd_Frame.__init__ ( self, parent, case_number)

		
	def imgs(self,img_num):
		path = "D:/gui/3D/Data/100783334/pancreas/pancreas_bnd/"
		for fn in os.listdir(path):
			if fn != '@eaDir' and fn.split('.')[1] == 'jpg':
				img_num.append(fn)
		img_num.sort()
	def next_picture(self, event,num):
		global i
		if i ==len(num)-1:
			i = -1
		image = wx.Image('D:/gui/3D/Data/100783334/pancreas/pancreas_bnd/' + str(num[i+1]))
		#更新GridBagSizer()的self.bmp2
		i = i + 1
		mypic = image.ConvertToBitmap()
		self.Bnd_bitmap.SetBitmap(wx.BitmapFromImage(mypic))
	def last_picture(self, event,num):
		global i
		if i ==0:
			i = len(num)
		image = wx.Image('D:/gui/3D/Data/100783334/pancreas/pancreas_bnd/' + str(num[i-1]))
		#更新GridBagSizer()的self.bmp2
		i = i - 1
		mypic = image.ConvertToBitmap()
		self.Bnd_bitmap.SetBitmap(wx.BitmapFromImage(mypic))
	def OnClick_pancreas(self, event):
		self.Close(True)
		import bnd_img
		app = wx.App()
		frm = bnd_img.Bnd_Frame(None)
		frm.Show()
		app.MainLoop()
	def OnClick_effusion(self, event):
		self.Close(True)
		import ctsi_img
		app = wx.App()
		frm = ctsi_img.MyFrame(None)
		frm.Show()
		app.MainLoop()

	def __del__( self ):
		pass
