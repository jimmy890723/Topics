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
import result_gui

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

###########################################################################
## Class Cases_score_Frame
###########################################################################

class Cases_score_Frame ( wx.Frame ):

	def __init__( self, parent , case_number):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cases score", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Cases_score_bSizer = wx.BoxSizer( wx.VERTICAL )

		self.Show_Segmentation = wx.Button( self, wx.ID_ANY, u"Segmentation", wx.DefaultPosition, wx.DefaultSize, 0 )
		Cases_score_bSizer.Add( self.Show_Segmentation, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.Show_CTSI = wx.Button( self, wx.ID_ANY, u"CTSI Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		Cases_score_bSizer.Add( self.Show_CTSI, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.SetSizer( Cases_score_bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Show_Segmentation.Bind( wx.EVT_BUTTON, self.Onclick_Segmentation)
		self.Show_CTSI.Bind( wx.EVT_BUTTON, self.Onclick_CTSI_Result)

	def __del__( self ):
		pass


###########################################################################
## Class Segmentation_Analysis
###########################################################################

class Segmentation_Analysis ( wx.Frame ):
	def OnEraseBack_pic( self, event , pic_path, W, H):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap(pic_path)
		bitmap = scale_bitmap(bmp, W, H)
		dc.DrawBitmap(bitmap, 0, 0)
	
	def OnEraseBack( self, event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap(".\\button_bmp\\PNG\\background.png")
		bitmap = scale_bitmap(bmp, 1300, 800)
		dc.DrawBitmap(bitmap, 0, 0)

	def __init__( self, parent , case_number , choose_type ):
		result_gui.init(self, parent)
		self.SetTitle('3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統 - 分割結果')
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		#--- left ---#

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer291 = wx.BoxSizer( wx.VERTICAL )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		reg_pan_left = wx.Image('.\\button_bmp\\PNG\\reg_pan_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_reg_pan = scale_bitmap(reg_pan_left, 130, 90)
		self.btn_reg_pan = wx.BitmapButton( self.m_panel2, wx.ID_ANY, bmp_reg_pan, wx.DefaultPosition, wx.Size( 110,90 ), 0 )
		bSizer32.Add( self.btn_reg_pan, 1, wx.ALIGN_BOTTOM|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, 10 )
		
		reg_eff_left = wx.Image('.\\button_bmp\\PNG\\reg_eff_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_reg_eff = scale_bitmap(reg_eff_left, 130, 90)
		self.btn_reg_eff = wx.BitmapButton( self.m_panel2, wx.ID_ANY, bmp_reg_eff, wx.DefaultPosition, wx.Size( 110,90 ), 0 )
		bSizer32.Add( self.btn_reg_eff, 1, wx.ALIGN_BOTTOM|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, 10 )


		bSizer291.Add( bSizer32, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer291 )
		self.m_panel2.Layout()
		bSizer291.Fit( self.m_panel2 )
		bSizer211.Add( self.m_panel2, 1, wx.BOTTOM|wx.EXPAND|wx.TOP, 1 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer211.Add( self.m_staticText21, 0, wx.ALL, 10 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer331 = wx.BoxSizer( wx.VERTICAL )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		deal_pan_left = wx.Image('.\\button_bmp\\PNG\\deal_pan_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_pan = scale_bitmap(deal_pan_left, 80, 85)
		self.btn_deal_pan = wx.BitmapButton( self.m_panel3, wx.ID_ANY, bmp_deal_pan, wx.DefaultPosition, wx.Size( 80,85 ), 0 )
		bSizer34.Add( self.btn_deal_pan, 0, wx.ALIGN_BOTTOM|wx.BOTTOM|wx.LEFT|wx.RIGHT, 15 )

		deal_eff_left = wx.Image('.\\button_bmp\\PNG\\deal_eff_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_eff = scale_bitmap(deal_eff_left, 80, 90)
		self.btn_deal_eff = wx.BitmapButton( self.m_panel3, wx.ID_ANY, bmp_deal_eff, wx.DefaultPosition, wx.Size( 80,85 ), 0 )
		bSizer34.Add( self.btn_deal_eff, 0, wx.ALIGN_BOTTOM|wx.BOTTOM, 15 )

		deal_CTSI_left = wx.Image('.\\button_bmp\\PNG\\deal_CTSI_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_CTSI = scale_bitmap(deal_CTSI_left, 80, 85)
		self.btn_deal_CTSI = wx.BitmapButton( self.m_panel3, wx.ID_ANY, bmp_deal_CTSI, wx.DefaultPosition, wx.Size( 80,85 ), 0 )
		bSizer34.Add( self.btn_deal_CTSI, 0, wx.ALIGN_BOTTOM|wx.BOTTOM|wx.LEFT|wx.RIGHT, 15 )


		bSizer331.Add( bSizer34, 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer331 )
		self.m_panel3.Layout()
		bSizer331.Fit( self.m_panel3 )
		bSizer211.Add( self.m_panel3, 1, wx.BOTTOM, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer211.Add( self.m_staticText20, 0, wx.ALL, 10 )

		ThreeD_left = wx.Image('.\\button_bmp\\PNG\\3D_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_ThreeD_left = scale_bitmap(ThreeD_left, 300, 150)
		self.bnt_ThreeD_left = wx.BitmapButton( self, wx.ID_ANY, bmp_ThreeD_left, wx.DefaultPosition, wx.Size( 300,150 ), 0 )
		bSizer211.Add( self.bnt_ThreeD_left, 1, )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer211.Add( self.m_staticText22, 0, wx.ALL, 10 )
		
		result_left = wx.Image('.\\button_bmp\\PNG\\result_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_result_left = scale_bitmap(result_left, 300, 150)
		self.bnt_result_left = wx.BitmapButton( self, wx.ID_ANY, bmp_result_left, wx.DefaultPosition, wx.Size( 300,150 ), 0 )
		bSizer211.Add( self.bnt_result_left, 1, wx.BOTTOM, 10 )


		bSizer12.Add( bSizer211, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 20 )

		#--- left ---#
		#--- right ---#

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer54 = wx.BoxSizer( wx.VERTICAL )

		Nowpath = os.getcwd()
		#choose_type 視選擇哪個type來輸出結果(看下拉式選單選得是effusion，還是pancreas)
		paths = Nowpath + '\\..\\..\\Data\\' + case_number + '\\' + choose_type + '\\' + choose_type + '_ove\\Output.txt'
		fopen = open(paths, 'r', encoding="ANSI")

		Segmentation_list = []
		self.Segmentation_list_Box = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 580,360 ), Segmentation_list, 0 )
		self.Segmentation_list_Box.SetFont( wx.Font(  wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		bSizer54.Add( self.Segmentation_list_Box, 2, wx.ALL, 20 )

		for line in fopen.readlines():
			self.Segmentation_list_Box.Append(line)

		bSizer19.Add( bSizer54, 1, wx.LEFT, 62 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		overlap_compete = wx.Image('.\\button_bmp\\PNG\\overlap_compete.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_overlap_compete = scale_bitmap(overlap_compete, 100, 50)
		self.btn_overlap_cmp = wx.BitmapButton( self, wx.ID_ANY, bmp_overlap_compete, wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		bSizer16.Add( self.btn_overlap_cmp, 0, wx.ALL, 20 )

		seg_result = wx.Image('.\\button_bmp\\PNG\\seg_result.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_seg_result = scale_bitmap(seg_result, 100, 50)
		self.btn_seg_result = wx.BitmapButton( self, wx.ID_ANY, bmp_seg_result, wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		bSizer16.Add( self.btn_seg_result, 0, wx.LEFT|wx.RIGHT, 20 )


		bSizer19.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer14.Add( bSizer19, 0, wx.EXPAND, 5 )

		bSizer55 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer55.Add( self.m_staticText21, 0, wx.ALL, 8 )

		SG = wx.Image('./logo/SG.png').Rescale(756,280).ConvertToBitmap()

		self.SG_Img = wx.StaticBitmap( self, wx.ID_ANY, SG, wx.Point( -1,-1 ), wx.Size( 756,280 ), 0 )
		bSizer55.Add( self.SG_Img, 0, wx.LEFT, 2 )


		bSizer14.Add( bSizer55, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 80 )


		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		pic_reg_path = '.\\button_bmp\\PNG\\recognize_left.png'
		size_recognize = self.m_panel3.GetSize()
		self.m_panel2.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_reg_path, W =size_recognize[0] ,H =size_recognize[1]+10: self.OnEraseBack_pic(evt,path,W,H))
		pic_deal_path = '.\\button_bmp\\PNG\\deal_left.png'
		size_deal = self.m_panel3.GetSize()
		self.m_panel3.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_deal_path, W =size_deal[0] ,H =size_deal[1]: self.OnEraseBack_pic(evt,path,W,H))
		self.btn_reg_pan.Bind( wx.EVT_BUTTON, self.OnClick_pancreas )
		self.btn_reg_eff.Bind( wx.EVT_BUTTON, self.OnClick_effusion )
		self.btn_deal_pan.Bind( wx.EVT_BUTTON, self.OnClick_pancreas_compara )
		self.btn_deal_eff.Bind( wx.EVT_BUTTON, self.OnClick_effusion_compara )
		self.btn_deal_CTSI.Bind( wx.EVT_BUTTON, self.CTSI_Score )
		self.bnt_ThreeD_left.Bind( wx.EVT_BUTTON, self.Start_page )
		self.bnt_result_left.Bind( wx.EVT_BUTTON, self.FReport_page )
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		if choose_type == "pancreas":
			self.btn_overlap_cmp.Bind( wx.EVT_BUTTON, self.OnClick_pancreas_compara)
			self.btn_seg_result.Bind( wx.EVT_BUTTON, self.OnClick_cut_pancreas)
		elif choose_type == "effusion":
			self.btn_overlap_cmp.Bind( wx.EVT_BUTTON, self.OnClick_effusion_compara )
			self.btn_seg_result.Bind( wx.EVT_BUTTON, self.OnClick_cut_effusion )

	def __del__( self ):
		pass
'''
	def __init__( self, parent , case_number , choose_type):
		result_gui.ctsi_init(self, parent)
		

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Segmentation_sizer = wx.BoxSizer( wx.VERTICAL )
		
		SG = wx.Image('./logo/SG.png').Rescale(756,250).ConvertToBitmap()
		self.SG_Img = wx.StaticBitmap( self, wx.ID_ANY, SG, wx.Point( -1,-1 ), wx.Size( 756,240 ), 0 )
		Segmentation_sizer.Add( self.SG_Img, 0, wx.ALIGN_CENTER|wx.TOP, 25 )
		

		Nowpath = os.getcwd()
		#choose_type 視選擇哪個type來輸出結果(看下拉式選單選得是effusion，還是pancreas)
		paths = Nowpath + '\\..\\..\\Data\\' + case_number + '\\' + choose_type + '\\' + choose_type + '_ove\\Output.txt'
		fopen = open(paths, 'r', encoding="ANSI")

		Segmentation_list = []
		
		self.Segmentation_list_Box = wx.ListBox( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 400,300 ), Segmentation_list, 0 )
		self.Segmentation_list_Box.SetFont( wx.Font(  wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		Segmentation_sizer.Add( self.Segmentation_list_Box, 0, wx.ALIGN_CENTER|wx.TOP, 40 )

		for line in fopen.readlines():
			self.Segmentation_list_Box.Append(line)

		self.SetSizer( Segmentation_sizer )
		self.Layout()

		self.Centre( wx.BOTH )
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
    
	def OnEraseBack( self, event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap("./logo/blue_bkg3.jpg")
		bitmap = scale_bitmap(bmp, 800, 700)
		dc.DrawBitmap(bitmap, 0, 0)
'''

###########################################################################
## Class CTSI_Analysis
###########################################################################

class CTSI_Analysis ( wx.Frame ):

	def OnEraseBack_pic( self, event , pic_path, W, H):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap(pic_path)
		bitmap = scale_bitmap(bmp, W, H)
		dc.DrawBitmap(bitmap, 0, 0)
	
	def OnEraseBack( self, event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap(".\\button_bmp\\PNG\\background.png")
		bitmap = scale_bitmap(bmp, 1300, 800)
		dc.DrawBitmap(bitmap, 0, 0)

	def OnEraseBack_pic( self, event , pic_path, W, H):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap(pic_path)
		bitmap = scale_bitmap(bmp, W, H)
		dc.DrawBitmap(bitmap, 0, 0)
	
	def OnEraseBack( self, event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap(".\\button_bmp\\PNG\\background.png")
		bitmap = scale_bitmap(bmp, 1300, 800)
		dc.DrawBitmap(bitmap, 0, 0)

	def __init__( self, parent, case_number  ):

		img_num = []
		jpg_save = []
		jpg_save_file = []
		content_list = []
		self.img_set(img_num,jpg_save,case_number,jpg_save_file)
		self.read_txt(content_list,case_number)
		
		result_gui.init(self, parent)
		self.SetTitle('3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統 - CTSI分析')

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		#--- left ---#

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer291 = wx.BoxSizer( wx.VERTICAL )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		reg_pan_left = wx.Image('.\\button_bmp\\PNG\\reg_pan_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_reg_pan = scale_bitmap(reg_pan_left, 130, 90)
		self.btn_reg_pan = wx.BitmapButton( self.m_panel2, wx.ID_ANY, bmp_reg_pan, wx.DefaultPosition, wx.Size( 110,90 ), 0 )
		bSizer32.Add( self.btn_reg_pan, 1, wx.ALIGN_BOTTOM|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, 10 )
		
		reg_eff_left = wx.Image('.\\button_bmp\\PNG\\reg_eff_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_reg_eff = scale_bitmap(reg_eff_left, 130, 90)
		self.btn_reg_eff = wx.BitmapButton( self.m_panel2, wx.ID_ANY, bmp_reg_eff, wx.DefaultPosition, wx.Size( 110,90 ), 0 )
		bSizer32.Add( self.btn_reg_eff, 1, wx.ALIGN_BOTTOM|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, 10 )


		bSizer291.Add( bSizer32, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer291 )
		self.m_panel2.Layout()
		bSizer291.Fit( self.m_panel2 )
		bSizer211.Add( self.m_panel2, 1, wx.BOTTOM|wx.EXPAND|wx.TOP, 1 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer211.Add( self.m_staticText21, 0, wx.ALL, 10 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer331 = wx.BoxSizer( wx.VERTICAL )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		deal_pan_left = wx.Image('.\\button_bmp\\PNG\\deal_pan_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_pan = scale_bitmap(deal_pan_left, 80, 85)
		self.btn_deal_pan = wx.BitmapButton( self.m_panel3, wx.ID_ANY, bmp_deal_pan, wx.DefaultPosition, wx.Size( 80,85 ), 0 )
		bSizer34.Add( self.btn_deal_pan, 0, wx.ALIGN_BOTTOM|wx.BOTTOM|wx.LEFT|wx.RIGHT, 15 )

		deal_eff_left = wx.Image('.\\button_bmp\\PNG\\deal_eff_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_eff = scale_bitmap(deal_eff_left, 80, 90)
		self.btn_deal_eff = wx.BitmapButton( self.m_panel3, wx.ID_ANY, bmp_deal_eff, wx.DefaultPosition, wx.Size( 80,85 ), 0 )
		bSizer34.Add( self.btn_deal_eff, 0, wx.ALIGN_BOTTOM|wx.BOTTOM, 15 )

		deal_CTSI_left = wx.Image('.\\button_bmp\\PNG\\deal_CTSI_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_CTSI = scale_bitmap(deal_CTSI_left, 80, 85)
		self.btn_deal_CTSI = wx.BitmapButton( self.m_panel3, wx.ID_ANY, bmp_deal_CTSI, wx.DefaultPosition, wx.Size( 80,85 ), 0 )
		bSizer34.Add( self.btn_deal_CTSI, 0, wx.ALIGN_BOTTOM|wx.BOTTOM|wx.LEFT|wx.RIGHT, 15 )


		bSizer331.Add( bSizer34, 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer331 )
		self.m_panel3.Layout()
		bSizer331.Fit( self.m_panel3 )
		bSizer211.Add( self.m_panel3, 1, wx.BOTTOM, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer211.Add( self.m_staticText20, 0, wx.ALL, 10 )

		ThreeD_left = wx.Image('.\\button_bmp\\PNG\\3D_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_ThreeD_left = scale_bitmap(ThreeD_left, 300, 150)
		self.bnt_ThreeD_left = wx.BitmapButton( self, wx.ID_ANY, bmp_ThreeD_left, wx.DefaultPosition, wx.Size( 300,150 ), 0 )
		bSizer211.Add( self.bnt_ThreeD_left, 1, )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer211.Add( self.m_staticText22, 0, wx.ALL, 10 )
		
		result_left = wx.Image('.\\button_bmp\\PNG\\result_left.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_result_left = scale_bitmap(result_left, 300, 150)
		self.bnt_result_left = wx.BitmapButton( self, wx.ID_ANY, bmp_result_left, wx.DefaultPosition, wx.Size( 300,150 ), 0 )
		bSizer211.Add( self.bnt_result_left, 1, wx.BOTTOM, 10 )


		bSizer1.Add( bSizer211, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 20 )

		#--- left ---#

		#--- right ---#

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.txt_list = TransparentText( self, wx.ID_ANY, label="CTSI預測結果")
		self.txt_list.SetFont( wx.Font(  wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		self.txt_list.Wrap( -1 )

		self.txt_list.SetMinSize( wx.Size( -1,35 ) )

		bSizer7.Add( self.txt_list, 0, wx.ALIGN_CENTER|wx.TOP, 20 )

		Nowpath = os.getcwd()

		paths_txt = Nowpath + '\\..\\..\\Data\\' + case_number + '\\Output_CTSI.txt'
		fopen = open(paths_txt, 'r', encoding="ANSI")

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,340 ), m_listBox1Choices, 0 )
		self.m_listBox1.SetFont( wx.Font(  wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		for line in fopen.readlines():
			self.m_listBox1.Append(line)
		bSizer7.Add( self.m_listBox1, 0, wx.ALIGN_CENTER, 0 )


		bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.txt_img = TransparentText( self, wx.ID_ANY, label="積液疊合結果")
		self.txt_img.SetFont( wx.Font(  wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		self.txt_img.Wrap( -1 )

		

		bSizer8.Add( self.txt_img, 0, wx.ALIGN_CENTER|wx.TOP, 20 )

		if len(img_num) == 0: 
			self.txt_img_num = TransparentText( self, wx.ID_ANY, label=jpg_save[0] )
		else:
			self.txt_img_num = TransparentText( self, wx.ID_ANY, label=img_num[0] )
		self.txt_img_num.SetFont( wx.Font(  wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		self.txt_img_num.Wrap( -1 )

		self.txt_img_num.SetMinSize( wx.Size( 165,22 ) )

		bSizer8.Add( self.txt_img_num, 0, wx.ALIGN_CENTER|wx.TOP, 1 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_content_1 = TransparentText( self, wx.ID_ANY, label=content_list[0])
		self.txt_content_1.SetFont( wx.Font(  wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		self.txt_content_1.Wrap( -1 )

		self.txt_content_1.SetMinSize( wx.Size( 180,20 ) )

		bSizer9.Add( self.txt_content_1, 0, wx.ALL, 3 )

		self.txt_content_2 = TransparentText( self, wx.ID_ANY, label=content_list[1] )
		self.txt_content_2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )
		self.txt_content_2.Wrap( -1 )

		self.txt_content_2.SetMinSize( wx.Size( 180,20 ) )

		bSizer9.Add( self.txt_content_2, 0, wx.ALL, 3 )


		bSizer8.Add( bSizer9, 0, wx.ALIGN_CENTER, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		last_pic = wx.Image('.\\button_bmp\\PNG\\last_pic.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_last_pic = scale_bitmap(last_pic, 60, 30)
		self.btn_last = wx.BitmapButton( self, wx.ID_ANY, bmp_last_pic, wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		bSizer11.Add( self.btn_last, 0, wx.LEFT|wx.RIGHT, 8 )

		next_pic = wx.Image('.\\button_bmp\\PNG\\next_pic.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_next_pic = scale_bitmap(next_pic, 60, 30)
		self.btn_next = wx.BitmapButton( self, wx.ID_ANY, bmp_next_pic, wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		bSizer11.Add( self.btn_next, 0, wx.LEFT|wx.RIGHT, 8 )

		bSizer8.Add( bSizer11, 0, wx.ALIGN_CENTER, 5 )
		self.img_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		if len(img_num) == 0:
			image1 = wx.Image("../../Data/" + case_number + "/effusion/" + jpg_save_file[0] +  "/" + str(jpg_save[0]))
		else:
			image1 = wx.Image("../../Data/" + case_number + "/effusion/effusion_ove" +  "/" + str(img_num[0]))

		#圖片格式轉換
		image1.Rescale(255,255)
		pic_no = image1.ConvertToBitmap()
		self.bitmap_no = wx.StaticBitmap( self.img_panel, bitmap=pic_no )
		bSizer56.Add( self.bitmap_no, 0, wx.ALIGN_CENTER|wx.ALL|wx.TOP, 5 )

		self.img_panel.SetSizer( bSizer56 )
		self.img_panel.Layout()
		bSizer56.Fit( self.img_panel )
		bSizer8.Add( self.img_panel, 1, wx.ALIGN_CENTER|wx.ALL, 0 )

		bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 3, 0, 0 )

		paths_jpg = Nowpath + '\\CTSI_output\\'

		Balthazar = wx.Image(paths_jpg + 'Balthazar.jpg').Rescale(250,240).ConvertToBitmap()
		self.Balthazar_Img = wx.StaticBitmap( self, wx.ID_ANY, Balthazar, wx.DefaultPosition, wx.Size( 250,240 ), 0 )
		gSizer2.Add( self.Balthazar_Img, 0, wx.LEFT, 5 )

		pancreas_death = wx.Image(paths_jpg + 'pancreas_death.jpg').Rescale(220,240).ConvertToBitmap()
		self.pancreas_death_Img = wx.StaticBitmap( self, wx.ID_ANY, pancreas_death, wx.DefaultPosition, wx.Size( 220,240 ), 0 )
		gSizer2.Add( self.pancreas_death_Img, 0, wx.LEFT, 17 )

		CTSI = wx.Image(paths_jpg + 'CTSI.jpg').Rescale(220,240).ConvertToBitmap()
		self.CTSI_Img = wx.StaticBitmap( self, wx.ID_ANY, CTSI, wx.DefaultPosition, wx.Size( 220,240 ), 0 )
		gSizer2.Add( self.CTSI_Img, 0, wx.ALIGN_LEFT, 0 )


		bSizer4.Add( gSizer2, 1, wx.EXPAND|wx.LEFT|wx.TOP, 30 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )
		
		pic_reg_path = '.\\button_bmp\\PNG\\recognize_left.png'
		size_recognize = self.m_panel3.GetSize()
		self.m_panel2.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_reg_path, W =size_recognize[0] ,H =size_recognize[1]+10: self.OnEraseBack_pic(evt,path,W,H))
		pic_deal_path = '.\\button_bmp\\PNG\\deal_left.png'
		size_deal = self.m_panel3.GetSize()
		self.m_panel3.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_deal_path, W =size_deal[0] ,H =size_deal[1]: self.OnEraseBack_pic(evt,path,W,H))
		self.btn_last.Bind( wx.EVT_BUTTON, lambda evt, num=img_num, jpg=jpg_save, j_file=jpg_save_file, content=content_list: self.Onclick_btn_last(evt,num,jpg,j_file,content) )
		self.btn_next.Bind( wx.EVT_BUTTON, lambda evt, num=img_num, jpg=jpg_save, j_file=jpg_save_file, content=content_list: self.Onclick_btn_next(evt,num,jpg,j_file,content) )
		self.img_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.btn_reg_pan.Bind( wx.EVT_BUTTON, self.OnClick_pancreas )
		self.btn_reg_eff.Bind( wx.EVT_BUTTON, self.OnClick_effusion )
		self.btn_deal_pan.Bind( wx.EVT_BUTTON, self.OnClick_pancreas_compara )
		self.btn_deal_eff.Bind( wx.EVT_BUTTON, self.OnClick_effusion_compara )
		self.btn_deal_CTSI.Bind( wx.EVT_BUTTON, self.CTSI_Score )
		self.bnt_ThreeD_left.Bind( wx.EVT_BUTTON, self.Start_page )
		self.bnt_result_left.Bind( wx.EVT_BUTTON, self.FReport_page )

	def __del__( self ):
		pass
'''
	def __init__( self, parent, case_number ):
		img_num = []
		jpg_save = []
		jpg_save_file = []
		content_list = []
		self.img_set(img_num,jpg_save,case_number,jpg_save_file)
		self.read_txt(content_list,case_number)
		
		result_gui.init(self, parent)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		All_Panel_Sizer = wx.BoxSizer( wx.VERTICAL )

		CTSI_Sizer = wx.GridSizer( 0, 3, 0, 10 )

		Nowpath = os.getcwd()
		paths_jpg = Nowpath + '\\CTSI_output\\'

		Balthazar = wx.Image(paths_jpg + 'Balthazar.jpg').Rescale(235,250).ConvertToBitmap()
		self.Balthazar_Img = wx.StaticBitmap( self, wx.ID_ANY, Balthazar, wx.Point( -1,-1 ), wx.Size( 238,250 ), 0 )
		CTSI_Sizer.Add( self.Balthazar_Img, 0, wx.TOP|wx.RIGHT|wx.LEFT, 12 )

		pancreas_death = wx.Image(paths_jpg + 'pancreas_death.jpg').Rescale(225,230).ConvertToBitmap()
		self.pancreas_death_Img = wx.StaticBitmap( self, wx.ID_ANY, pancreas_death, wx.Point( -1,-1 ), wx.Size( 225,230 ), 0 )
		CTSI_Sizer.Add( self.pancreas_death_Img, 0, wx.TOP|wx.RIGHT|wx.LEFT, 10|10|13 )

		CTSI = wx.Image(paths_jpg + 'CTSI.jpg').Rescale(225,230).ConvertToBitmap()
		self.CTSI_Img = wx.StaticBitmap( self, wx.ID_ANY, CTSI, wx.Point( -1,-1 ), wx.Size( 228,230 ), 0 )
		CTSI_Sizer.Add( self.CTSI_Img, 0, wx.TOP|wx.RIGHT|wx.LEFT, 10 )

		All_Panel_Sizer.Add( CTSI_Sizer, 1, wx.EXPAND, 5 )

		Result_Sizer = wx.GridSizer( 0, 2, 0, 0 )

		List_Sizer = wx.BoxSizer( wx.VERTICAL )

		self.txt_list = TransparentText( self, wx.ID_ANY, label="CTSI預測結果")
		self.txt_list.SetFont( wx.Font(  wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		self.txt_list.Wrap( -1 )

		List_Sizer.Add( self.txt_list, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		paths_txt = Nowpath + '\\..\\..\\Data\\' + case_number + '\\Output_CTSI.txt'
		fopen = open(paths_txt, 'r', encoding="ANSI")

		m_listBox1Choices = []
		
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 380,320 ), m_listBox1Choices, 0 )
		self.m_listBox1.SetFont( wx.Font(  wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )

		for line in fopen.readlines():
			self.m_listBox1.Append(line)
		
		List_Sizer.Add( self.m_listBox1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		Result_Sizer.Add( List_Sizer, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		img_sizer = wx.BoxSizer( wx.VERTICAL )
		
		
		self.txt_img = TransparentText( self, wx.ID_ANY, label="積液疊合結果")
		self.txt_img.SetFont( wx.Font(  wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		self.txt_img.Wrap( -1 )

		img_sizer.Add( self.txt_img, 0,  wx.ALIGN_CENTER|wx.ALL, 5 )

		if len(img_num) == 0: 
			self.txt_img_num = TransparentText( self, wx.ID_ANY, label=jpg_save[0] )
		else:
			self.txt_img_num = TransparentText( self, wx.ID_ANY, label=img_num[0] )
		self.txt_img_num.SetFont( wx.Font(  wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		self.txt_img_num.Wrap( -1 )

		img_sizer.Add( self.txt_img_num, 0,  wx.ALIGN_CENTER|wx.ALL, 5 )

		content_sizer = wx.BoxSizer( wx.HORIZONTAL )
		self.txt_content_1 = TransparentText( self, wx.ID_ANY, label=content_list[0])
		self.txt_content_1.SetFont( wx.Font(  wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" )) )
		self.txt_content_1.Wrap( -1 )

		content_sizer.Add( self.txt_content_1, 0,  wx.ALIGN_CENTER|wx.LEFT, 5 )

		self.txt_content_2 = TransparentText( self, wx.ID_ANY, label=content_list[1] )
		self.txt_content_2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )
		self.txt_content_2.Wrap( -1 )

		content_sizer.Add( self.txt_content_2, 0,  wx.ALIGN_CENTER|wx.LEFT, 10 )

		img_sizer.Add( content_sizer, 0, wx.ALIGN_TOP|wx.ALIGN_CENTER, 0 )
		
		btn_sizer = wx.BoxSizer( wx.HORIZONTAL )
		self.button_last = wx.Button( self, wx.ID_ANY, u"上一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		btn_sizer.Add( self.button_last, 0, wx.ALIGN_TOP|wx.ALIGN_CENTER|wx.LEFT, 5 )
		self.button_next = wx.Button( self, wx.ID_ANY, u"下一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		btn_sizer.Add( self.button_next, 0, wx.ALIGN_TOP|wx.ALIGN_CENTER|wx.LEFT, 10 )

		img_sizer.Add( btn_sizer, 0, wx.ALIGN_TOP|wx.ALIGN_CENTER, 0 )
		
		if len(img_num) == 0:
			image1 = wx.Image("../../Data/" + case_number + "/effusion/" + jpg_save_file[0] +  "/" + str(jpg_save[0]))
		else:
			image1 = wx.Image("../../Data/" + case_number + "/effusion/effusion_ove" +  "/" + str(img_num[0]))
		#圖片格式轉換
		image1.Rescale(220,220)
		pic_no = image1.ConvertToBitmap()
		self.bitmap_no = wx.StaticBitmap( self, bitmap=pic_no )
		img_sizer.Add( self.bitmap_no, 0, wx.TOP|wx.ALIGN_CENTER|wx.ALL, 5 )
		
		Result_Sizer.Add( img_sizer, 0, wx.ALIGN_TOP|wx.ALL, 1  )

		All_Panel_Sizer.Add( Result_Sizer, 1, wx.EXPAND, 5 )
		self.SetSizer( All_Panel_Sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		
		self.button_last.Bind( wx.EVT_BUTTON, lambda evt, num=img_num, jpg=jpg_save, j_file=jpg_save_file, content=content_list: self.Onclick_btn_last(evt,num,jpg,j_file,content) )
		self.button_next.Bind( wx.EVT_BUTTON, lambda evt, num=img_num, jpg=jpg_save, j_file=jpg_save_file, content=content_list: self.Onclick_btn_next(evt,num,jpg,j_file,content) )
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)

	def __del__( self ):
		pass

	def OnEraseBack( self, event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap("./logo/blue_bkg3.jpg")
		bitmap = scale_bitmap(bmp, 800, 700)
		dc.DrawBitmap(bitmap, 0, 0)
'''

class TransparentText(wx.StaticText):#繼承了wx.Statictext的類，並對相應的方法進行重寫;
    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TRANSPARENT_WINDOW, name='transparenttext'):
        wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.on_size)
    def on_paint(self, event):#重寫on_paint可以對控件進行重寫重新構造形狀
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)
    def on_size(self, event):
        self.Refresh()
        event.Skip()