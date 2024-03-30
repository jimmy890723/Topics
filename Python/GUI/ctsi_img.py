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
import ctsi_gui as gui
case_number = "100783334"

i = 0
###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( gui.MyFrame ):

	def __init__( self, parent ):
		
		gui.MyFrame.__init__ ( self, parent, case_number)

		
	def imgs(self,img_num):
		path = "../../Data/" + case_number + "/pancreas/pancreas_ove/"
		for fn in os.listdir(path):
			if fn != '@eaDir' and fn.split('.')[1] == 'jpg':
				img_num.append(fn)
		img_num.sort()
	def next_picture(self, event,num):
		global i
		if i ==len(num)-1:
			i = -1
		image1 = wx.Image("../../Data/" + case_number + "/pancreas/2016_3_21____09_26_12_pancreas_jpg/" + str(num[i+1]))
		image2 = wx.Image("../../Data/" + case_number + "/pancreas/pancreas_ove/" + str(num[i+1]))
		#更新GridBagSizer()的self.bmp2
		i = i + 1
		mypic1 = image1.ConvertToBitmap()
		self.bitmap_no.SetBitmap(wx.BitmapFromImage(mypic1))
		mypic2 = image2.ConvertToBitmap()
		self.bitmap_yes.SetBitmap(wx.BitmapFromImage(mypic2))
	def last_picture(self, event,num):
		global i
		if i ==0:
			i = len(num)
		image = wx.Image("../../Data/" + case_number + "/pancreas/2016_3_21____09_26_12_pancreas_jpg/" + str(num[i-1]))
		image2 = wx.Image("../../Data/" + case_number + "/pancreas/2016_3_21____09_26_12_pancreas_jpg/" + str(num[i-1]))
		#更新GridBagSizer()的self.bmp2
		i = i - 1
		mypic1 = image.ConvertToBitmap()
		self.bitmap_no.SetBitmap(wx.BitmapFromImage(mypic1))
		mypic2 = image2.ConvertToBitmap()
		self.bitmap_yes.SetBitmap(wx.BitmapFromImage(mypic2))
		#def Onclick_back( self, event ):
		#	self.Close(True)
		#	frm = Bounding_Box_Show_Frame(None)
		#	frm.Show()
		#	app.MainLoop()

	def __del__( self ):
		pass

if __name__ == "__main__":
    app = wx.App()
    frm = MyFrame(None)
    frm.Show()
    app.MainLoop()
