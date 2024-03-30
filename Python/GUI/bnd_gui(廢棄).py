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
import result_gui
###########################################################################
## Class Bnd_Frame
###########################################################################

class Bnd_Frame ( wx.Frame ):

	def __init__( self, parent, case_number , detection_type):
		img_num = []
		self.imgs(img_num)
		
		result_gui.init(self, parent)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Bnd_bSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.Bnd_panel_left = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Bnd_bSizer_left = wx.BoxSizer( wx.HORIZONTAL )

		self.Bnd_bSizer_left_button = wx.Button( self.Bnd_panel_left, wx.ID_ANY, u"上一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		Bnd_bSizer_left.Add( self.Bnd_bSizer_left_button, 0, wx.ALIGN_CENTER|wx.ALL, 80 )


		self.Bnd_panel_left.SetSizer( Bnd_bSizer_left )
		self.Bnd_panel_left.Layout()
		Bnd_bSizer_left.Fit( self.Bnd_panel_left )
		Bnd_bSizer.Add( self.Bnd_panel_left, 1, wx.EXPAND |wx.ALL, 5 )

		self.Bnd_panel_mid = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Bnd_bSizer_mid = wx.BoxSizer( wx.HORIZONTAL )

		image = wx.Image('../../Data/'+ case_number +'/' + detection_type + '/'+ detection_type + '_bnd/' + img_num[0])
		#圖片格式轉換
		btn_pic = image.ConvertToBitmap()
		self.Bnd_bitmap = wx.StaticBitmap( self.Bnd_panel_mid, bitmap=btn_pic )
		Bnd_bSizer_mid.Add( self.Bnd_bitmap, 0, wx.ALIGN_CENTER|wx.ALL, 130 )


		self.Bnd_panel_mid.SetSizer( Bnd_bSizer_mid )
		self.Bnd_panel_mid.Layout()
		Bnd_bSizer_mid.Fit( self.Bnd_panel_mid )
		Bnd_bSizer.Add( self.Bnd_panel_mid, 3, wx.EXPAND |wx.ALL, 5 )

		self.Bnd_panel_right = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Bnd_bSizer_right = wx.BoxSizer( wx.HORIZONTAL )

		self.Bnd_bSizer_right_button = wx.Button( self.Bnd_panel_right, wx.ID_ANY, u"下一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		Bnd_bSizer_right.Add( self.Bnd_bSizer_right_button, 0, wx.ALIGN_CENTER|wx.ALL, 80 )


		self.Bnd_panel_right.SetSizer( Bnd_bSizer_right )
		self.Bnd_panel_right.Layout()
		Bnd_bSizer_right.Fit( self.Bnd_panel_right )
		Bnd_bSizer.Add( self.Bnd_panel_right, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( Bnd_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		self.Bnd_bSizer_left_button.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.last_picture(evt,num))
		self.Bnd_bSizer_right_button.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.next_picture(evt,num))

	
if __name__ == "__main__":
    app = wx.App()
    frm = Bnd_Frame(None)
    frm.Show()
    app.MainLoop()