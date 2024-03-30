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
import wx.lib.mixins.listctrl as listmix
import csv

###########################################################################
## Class Start_Frame
###########################################################################
class Start_Frame ( wx.Frame ):

	def __init__( self, parent , case_number):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Start", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Start_bSizer = wx.BoxSizer( wx.VERTICAL )

		self.Start_show_case = wx.StaticText( self, wx.ID_ANY, u"Please enter casenumber...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Start_show_case.Wrap( -1 )

		Start_bSizer.Add( self.Start_show_case, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.Start_casenumber = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		Start_bSizer.Add( self.Start_casenumber, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )

		self.Start_submit = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		Start_bSizer.Add( self.Start_submit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )


		self.SetSizer( Start_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Start_submit.Bind( wx.EVT_BUTTON, self.Onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class


###########################################################################
## Class Menu_Frame
###########################################################################

class Menu_Frame ( wx.Frame ):

	def __init__( self, parent , case_number):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Menu_bSizer = wx.BoxSizer( wx.VERTICAL )

		self.Menu_show_case = wx.StaticText( self, wx.ID_ANY, str(case_number), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Menu_show_case.Wrap( -1 )

		Menu_bSizer.Add( self.Menu_show_case, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.Menu_deal = wx.Button( self, wx.ID_ANY, u"Deal", wx.DefaultPosition, wx.DefaultSize, 0 )
		Menu_bSizer.Add( self.Menu_deal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Menu_result = wx.Button( self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		Menu_bSizer.Add( self.Menu_result, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Menu_back = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		Menu_bSizer.Add( self.Menu_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )


		self.SetSizer( Menu_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Menu_deal.Bind( wx.EVT_BUTTON, self.Onclick_deal )
		self.Menu_result.Bind( wx.EVT_BUTTON, self.Onclick_result )
		self.Menu_back.Bind( wx.EVT_BUTTON, self.Onclick_back )

	def __del__( self ):
		pass





###########################################################################
## Class Deal_Frame
###########################################################################

class Deal_Frame ( wx.Frame ):

	def __init__( self, parent , case_number):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Deal", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Deal_bSizer = wx.BoxSizer( wx.VERTICAL )

		self.Deal_show_case = wx.StaticText( self, wx.ID_ANY, str(case_number), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Deal_show_case.Wrap( -1 )

		Deal_bSizer.Add( self.Deal_show_case, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.Deal_img_identify = wx.Button( self, wx.ID_ANY, u"Img Identify", wx.DefaultPosition, wx.DefaultSize, 0 )
		Deal_bSizer.Add( self.Deal_img_identify, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Deal_img_deal = wx.Button( self, wx.ID_ANY, u"Img Deal", wx.DefaultPosition, wx.DefaultSize, 0 )
		Deal_bSizer.Add( self.Deal_img_deal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Deal_best_path = wx.Button( self, wx.ID_ANY, u"Best Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		Deal_bSizer.Add( self.Deal_best_path, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Deal_back = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		Deal_bSizer.Add( self.Deal_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )


		self.SetSizer( Deal_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Deal_img_identify.Bind( wx.EVT_BUTTON, self.Onclick_img_identify )
		self.Deal_img_deal.Bind( wx.EVT_BUTTON, self.Onclick_Img_Processing )
		self.Deal_best_path.Bind( wx.EVT_BUTTON, self.Onclick_best_path )
		self.Deal_back.Bind( wx.EVT_BUTTON, self.Onclick_back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	


###########################################################################
## Class Result_Frame
###########################################################################

class Result_Frame ( wx.Frame ):

	def __init__( self, parent , case_number):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Result", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Result_bSizer = wx.BoxSizer( wx.VERTICAL )

		self.Result_show_case = wx.StaticText( self, wx.ID_ANY, str(case_number), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Result_show_case.Wrap( -1 )

		Result_bSizer.Add( self.Result_show_case, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.Result_img_show = wx.Button( self, wx.ID_ANY, u"Img Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		Result_bSizer.Add( self.Result_img_show, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Result_casescore = wx.Button( self, wx.ID_ANY, u"Cases Score", wx.DefaultPosition, wx.DefaultSize, 0 )
		Result_bSizer.Add( self.Result_casescore, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Result_3D = wx.Button( self, wx.ID_ANY, u"3D", wx.DefaultPosition, wx.DefaultSize, 0 )
		Result_bSizer.Add( self.Result_3D, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Result_back = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		Result_bSizer.Add( self.Result_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )


		self.SetSizer( Result_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Result_img_show.Bind( wx.EVT_BUTTON, self.Onclick_img_show )
		self.Result_casescore.Bind( wx.EVT_BUTTON, self.Onclick_casescore )
		self.Result_3D.Bind( wx.EVT_BUTTON, self.Onclick_3D )
		self.Result_back.Bind( wx.EVT_BUTTON, self.Onclick_back )

	def __del__( self ):
		pass





###########################################################################
## Class Img_Show_Frame
###########################################################################

class Img_Show_Frame ( wx.Frame ):

	def __init__( self, parent , case_number):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Img Show", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		img_show_bSizer = wx.BoxSizer( wx.VERTICAL )

		self.img_show_show_case = wx.StaticText( self, wx.ID_ANY, str(case_number), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.img_show_show_case.Wrap( -1 )

		img_show_bSizer.Add( self.img_show_show_case, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.img_show_bounding_box = wx.Button( self, wx.ID_ANY, u"Bounding Box", wx.DefaultPosition, wx.DefaultSize, 0 )
		img_show_bSizer.Add( self.img_show_bounding_box, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.img_show_pancreas = wx.Button( self, wx.ID_ANY, u"Pancreas", wx.DefaultPosition, wx.DefaultSize, 0 )
		img_show_bSizer.Add( self.img_show_pancreas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.img_show_effusion = wx.Button( self, wx.ID_ANY, u"Effusion", wx.DefaultPosition, wx.DefaultSize, 0 )
		img_show_bSizer.Add( self.img_show_effusion, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.img_show_back = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		img_show_bSizer.Add( self.img_show_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )


		self.SetSizer( img_show_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.img_show_bounding_box.Bind( wx.EVT_BUTTON, self.Onclick_bounding_box )
		self.img_show_pancreas.Bind( wx.EVT_BUTTON, self.Onclick )
		self.img_show_effusion.Bind( wx.EVT_BUTTON, self.Onclick )
		self.img_show_back.Bind( wx.EVT_BUTTON, self.Onclick_back )

	def __del__( self ):
		pass




###########################################################################
## Class Bounding_Box_Show_Frame
###########################################################################



class Bounding_Box_Show_Frame ( wx.Frame ):

    def __init__( self, parent , case_number):
        i = 0
        img_num = []
        self.imgs(img_num)
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Start", pos = wx.DefaultPosition, size = wx.Size( 500,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        Bounding_Box_bSizer = wx.BoxSizer( wx.VERTICAL )
        #宣告圖片物件
        image = wx.Image('D:/gui/' + str(case_number) + "/" + img_num[0])

        #圖片格式轉換
        mypic = image.ConvertToBitmap()
        #顯示圖片
        
        self.Start_StaticBitmap = wx.StaticBitmap(self,bitmap=mypic,pos=(0,0))
        Bounding_Box_bSizer.Add( self.Start_StaticBitmap, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.Bounding_Box_next = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
        Bounding_Box_bSizer.Add( self.Bounding_Box_next, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

        self.Bounding_Box_back = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
        Bounding_Box_bSizer.Add( self.Bounding_Box_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

        self.Bounding_Box_back_page = wx.Button( self, wx.ID_ANY, u"Back Page", wx.DefaultPosition, wx.DefaultSize, 0 )
        Bounding_Box_bSizer.Add( self.Bounding_Box_back_page, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

        self.SetSizer( Bounding_Box_bSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )

        self.Bounding_Box_next.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.next_picture(evt,num))
        self.Bounding_Box_back.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.back_picture(evt,num))
        self.Bounding_Box_back_page.Bind( wx.EVT_BUTTON, self.Onclick_back )




###########################################################################
## Class Cases_score_Frame
###########################################################################

class Cases_score_Frame ( wx.Frame ):

	def __init__( self, parent , case_number):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cases score", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Cases_score_bSizer = wx.BoxSizer( wx.VERTICAL )

		self.Cases_score_show_case = wx.StaticText( self, wx.ID_ANY, str(case_number), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Cases_score_show_case.Wrap( -1 )

		Cases_score_bSizer.Add( self.Cases_score_show_case, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.Cases_score_pancreas_cut_status = wx.Button( self, wx.ID_ANY, u"胰腺分割狀態", wx.DefaultPosition, wx.DefaultSize, 0 )
		Cases_score_bSizer.Add( self.Cases_score_pancreas_cut_status, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Cases_score_Check_CTSI = wx.Button( self, wx.ID_ANY, u"Check CTSI Score", wx.DefaultPosition, wx.DefaultSize, 0 )
		Cases_score_bSizer.Add( self.Cases_score_Check_CTSI, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Cases_score_CTSI = wx.Button( self, wx.ID_ANY, u"Run CTSI Score", wx.DefaultPosition, wx.DefaultSize, 0 )
		Cases_score_bSizer.Add( self.Cases_score_CTSI, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Cases_score_back = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		Cases_score_bSizer.Add( self.Cases_score_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )


		self.SetSizer( Cases_score_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Cases_score_pancreas_cut_status.Bind( wx.EVT_BUTTON, self.Onclick_pancreas_cut_status )
		self.Cases_score_Check_CTSI.Bind( wx.EVT_BUTTON, self.Onclick_Check_CTSI )
		self.Cases_score_CTSI.Bind( wx.EVT_BUTTON, self.Onclick_CTSI )
		self.Cases_score_back.Bind( wx.EVT_BUTTON, self.Onclick_back )

	def __del__( self ):
		pass





###########################################################################
## Class ThreeD_Frame
###########################################################################

class ThreeD_Frame ( wx.Frame ):

	def __init__( self, parent , case_number):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Best path", pos = wx.DefaultPosition, size = wx.Size( 467,399 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		ThreeD_bSizer = wx.BoxSizer( wx.VERTICAL )

		self.ThreeD_show_case = wx.StaticText( self, wx.ID_ANY, str(case_number), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThreeD_show_case.Wrap( -1 )

		ThreeD_bSizer.Add( self.ThreeD_show_case, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Please enter index number...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		ThreeD_bSizer.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.ThreeD_index = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		ThreeD_bSizer.Add( self.ThreeD_index, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )

		self.ThreeD_submit = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		ThreeD_bSizer.Add( self.ThreeD_submit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.ThreeD_back = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		ThreeD_bSizer.Add( self.ThreeD_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )


		self.SetSizer( ThreeD_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.ThreeD_submit.Bind( wx.EVT_BUTTON, self.Onclick )
		self.ThreeD_back.Bind( wx.EVT_BUTTON, self.Onclick_back )

	def __del__( self ):
		pass



