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

i = 0
###########################################################################
## Class MyFrame
###########################################################################
def scale_bitmap(bitmap, width, height):
		image = wx.ImageFromBitmap(bitmap)
		image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
		result = wx.BitmapFromImage(image)
		return result

class MyFrame ( wx.Frame ):

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
	
	def __init__( self, parent, case_number, detection_type, jpg_file ):
		img_num = []
		txt_num = []
		num = []
		self.imgs(img_num)
		self.txt_list(txt_num)
		result_gui.init(self, parent)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

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


		bSizer20.Add( bSizer211, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 20 )
		#--- right ---#

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		Nowpath = os.getcwd()
		#choose_type 視選擇哪個type來輸出結果(看下拉式選單選得是effusion，還是pancreas)
		paths = Nowpath + '\\..\\..\\Data\\' + case_number + '\\' + detection_type + '\\' + detection_type + '_txt\\' + str(txt_num[0])
		fopen = open(paths, 'r', encoding="ANSI")

		ctsi_list = []
		self.ctsi_list_Box = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,290 ), ctsi_list, 0 )
		self.ctsi_list_Box.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		bSizer42.Add( self.ctsi_list_Box, 1, wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 20 )


		bSizer22.Add( bSizer42, 1, wx.LEFT, 140 )

		for line in fopen.readlines():
			self.ctsi_list_Box.Append(line)

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		overlap_compete = wx.Image('.\\button_bmp\\PNG\\overlap_compete.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_overlap_compete = scale_bitmap(overlap_compete, 100, 50)
		self.btn_overlap_cmp = wx.BitmapButton( self, wx.ID_ANY, bmp_overlap_compete, wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		bSizer25.Add( self.btn_overlap_cmp, 0, wx.ALL, 20 )
		
		seg_result = wx.Image('.\\button_bmp\\PNG\\seg_result.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_seg_result = scale_bitmap(seg_result, 100, 50)
		self.btn_seg_result = wx.BitmapButton( self, wx.ID_ANY, bmp_seg_result, wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		bSizer25.Add( self.btn_seg_result, 0, wx.LEFT|wx.RIGHT, 20 )

		bSizer22.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer28.Add( bSizer22, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 3, 2, 0, 0 )

		self.staticText_dr = TransparentText( self, wx.ID_ANY, label="Doctor標記")
		self.staticText_dr.Wrap( -1 )
		self.staticText_dr.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		gSizer4.Add( self.staticText_dr, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 1 )

		self.staticText_add = TransparentText( self, wx.ID_ANY, label="影像分析結果")
		self.staticText_add.Wrap( -1 )
		self.staticText_add.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		gSizer4.Add( self.staticText_add, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 1 )

		'''
		self.panel_leftimg = wx.Panel( self.panel_buttom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_left = wx.BoxSizer( wx.VERTICAL )
		image1 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + jpg_file +  "/" + str(img_num[0]))
		#圖片格式轉換
		image1.Rescale(400,400)
		pic_no = image1.ConvertToBitmap()
		self.bitmap_no = wx.StaticBitmap( self.panel_leftimg, bitmap=pic_no )
		bSizer_left.Add( self.bitmap_no, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


		self.panel_leftimg.SetSizer( bSizer_left )
		self.panel_leftimg.Layout()
		bSizer_left.Fit( self.panel_leftimg )
		bSizer_buttom.Add( self.panel_leftimg, 4, wx.EXPAND |wx.ALL, 5 )
		'''
		self.panel_leftimg = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		image1 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + jpg_file +  "/" + str(img_num[0]))
		image1.Rescale(300,300)
		pic_no = image1.ConvertToBitmap()
		
		self.bitmap_no = wx.StaticBitmap( self.panel_leftimg, wx.ID_ANY, pic_no, wx.DefaultPosition, wx.Size( 300,300 ), 0 )
		bSizer54.Add( self.bitmap_no, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.LEFT|wx.BOTTOM, 5 )

		self.panel_leftimg.SetSizer( bSizer54 )
		self.panel_leftimg.Layout()
		bSizer54.Fit( self.panel_leftimg )
		gSizer4.Add( self.panel_leftimg, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.panel_rightimg = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		image2 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + detection_type + "_ove/" + str(img_num[0]))
		image2.Rescale(300,300)
		pic_yes = image2.ConvertToBitmap()

		self.bitmap_yes = wx.StaticBitmap( self.panel_rightimg, wx.ID_ANY, pic_yes, wx.DefaultPosition, wx.Size( 300,300 ), 0 )
		bSizer55.Add( self.bitmap_yes, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.LEFT|wx.BOTTOM, 5 )

		self.panel_rightimg.SetSizer( bSizer55 )
		self.panel_rightimg.Layout()
		bSizer55.Fit( self.panel_rightimg )
		gSizer4.Add( self.panel_rightimg, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		last_pic = wx.Image('.\\button_bmp\\PNG\\last_pic.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_last_pic = scale_bitmap(last_pic, 100, 40)
		self.btn_last = wx.BitmapButton( self, wx.ID_ANY, bmp_last_pic, wx.DefaultPosition, wx.Size( 100,40 ), 0 )
		gSizer4.Add( self.btn_last, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 15 )

		next_pic = wx.Image('.\\button_bmp\\PNG\\next_pic.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_next_pic = scale_bitmap(next_pic, 100, 40)
		self.btn_next = wx.BitmapButton( self, wx.ID_ANY, bmp_next_pic, wx.DefaultPosition, wx.Size( 100,40 ), 0 )
		gSizer4.Add( self.btn_next, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 15 )


		bSizer28.Add( gSizer4, 1, wx.BOTTOM|wx.EXPAND, 20 )


		bSizer20.Add( bSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

		pic_reg_path = '.\\button_bmp\\PNG\\recognize_left.png'
		size_recognize = self.m_panel3.GetSize()
		self.m_panel2.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_reg_path, W =size_recognize[0] ,H =size_recognize[1]+10: self.OnEraseBack_pic(evt,path,W,H))
		pic_deal_path = '.\\button_bmp\\PNG\\deal_left.png'
		size_deal = self.m_panel3.GetSize()
		self.m_panel3.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_deal_path, W =size_deal[0] ,H =size_deal[1]: self.OnEraseBack_pic(evt,path,W,H))
		self.panel_rightimg.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_leftimg.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.btn_next.Bind(wx.EVT_BUTTON, lambda evt, num=img_num,txt=txt_num: self.next_picture(evt,num,txt))
		self.btn_last.Bind(wx.EVT_BUTTON, lambda evt, num=img_num,txt=txt_num: self.last_picture(evt,num,txt))
		self.btn_reg_pan.Bind( wx.EVT_BUTTON, self.OnClick_pancreas )
		self.btn_reg_eff.Bind( wx.EVT_BUTTON, self.OnClick_effusion )
		self.btn_deal_pan.Bind( wx.EVT_BUTTON, self.OnClick_pancreas_compara )
		self.btn_deal_eff.Bind( wx.EVT_BUTTON, self.OnClick_effusion_compara )
		self.btn_deal_CTSI.Bind( wx.EVT_BUTTON, self.CTSI_Score )
		self.bnt_ThreeD_left.Bind( wx.EVT_BUTTON, self.Start_page )
		self.bnt_result_left.Bind( wx.EVT_BUTTON, self.FReport_page )
		if detection_type == "pancreas":
			self.btn_overlap_cmp.Bind( wx.EVT_BUTTON, self.OnClick_pancreas_compara)
			self.btn_seg_result.Bind( wx.EVT_BUTTON, self.OnClick_cut_pancreas)
		elif detection_type == "effusion":
			self.btn_overlap_cmp.Bind( wx.EVT_BUTTON, self.OnClick_effusion_compara )
			self.btn_seg_result.Bind( wx.EVT_BUTTON, self.OnClick_cut_effusion )
	
		
	def __del__( self ):
		pass

'''
	def __init__( self, parent, case_number, detection_type, jpg_file):
		img_num = []
		txt_num = []
		num = []
		self.imgs(img_num)
		self.txt_list(txt_num)
		result_gui.init(self, parent)

		

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		Nowpath = os.getcwd()
		#choose_type 視選擇哪個type來輸出結果(看下拉式選單選得是effusion，還是pancreas)
		paths = Nowpath + '\\..\\..\\Data\\' + case_number + '\\' + detection_type + '\\' + detection_type + '_txt\\' + str(txt_num[0])
		fopen = open(paths, 'r', encoding="ANSI")
		
		ctsi_list = []
		

		self.CTSI_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_top = wx.BoxSizer( wx.VERTICAL )

		self.ctsi_list_Box = wx.ListBox( self.CTSI_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,300 ), ctsi_list, 0 )
		self.ctsi_list_Box.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		bSizer_top.Add( self.ctsi_list_Box, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.CTSI_panel.SetSizer( bSizer_top )
		self.CTSI_panel.Layout()
		bSizer_top.Fit( self.CTSI_panel )
		bSizer.Add( self.CTSI_panel, 5, wx.EXPAND |wx.ALL, 0 )


		for line in fopen.readlines():
			self.ctsi_list_Box.Append(line)

		
		
		self.panel_comment = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_comment = wx.BoxSizer( wx.HORIZONTAL )
######################

		self.panel_space1 = wx.Panel( self.panel_comment, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_space1 = wx.BoxSizer( wx.VERTICAL )
		self.panel_space1.SetSizer( bSizer_space1 )
		self.panel_space1.Layout()
		bSizer_space1.Fit( self.panel_space1 )
		bSizer_comment.Add( self.panel_space1, 1, wx.EXPAND |wx.ALL, 5 )
#######################


		self.panel_dr = wx.Panel( self.panel_comment, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_dr = wx.BoxSizer( wx.VERTICAL )

		self.staticText_dr = TransparentText( self.panel_dr, wx.ID_ANY, label="Doctor標記" )
		self.staticText_dr.Wrap( -1 )
		self.staticText_dr.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "標楷體" ) )

		bSizer_dr.Add( self.staticText_dr, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.panel_dr.SetSizer( bSizer_dr )
		self.panel_dr.Layout()
		bSizer_dr.Fit( self.panel_dr )
		bSizer_comment.Add( self.panel_dr, 4, wx.EXPAND |wx.ALL, 5 )
#######################
		self.panel_add = wx.Panel( self.panel_comment, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_add = wx.BoxSizer( wx.VERTICAL )

		self.staticText_add = TransparentText( self.panel_add, wx.ID_ANY, label="影像分析結果" )
		self.staticText_add.Wrap( -1 )
		self.staticText_add.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "標楷體" ) )

		bSizer_add.Add( self.staticText_add, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.panel_add.SetSizer( bSizer_add )
		self.panel_add.Layout()
		bSizer_add.Fit( self.panel_add )
		bSizer_comment.Add( self.panel_add, 4, wx.EXPAND |wx.ALL, 0 )


		self.panel_comment.SetSizer( bSizer_comment )
		self.panel_comment.Layout()
		bSizer_comment.Fit( self.panel_comment )
		bSizer.Add( self.panel_comment, 4, wx.EXPAND |wx.ALL, 0 )
######################

		self.panel_space2 = wx.Panel( self.panel_comment, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_space2 = wx.BoxSizer( wx.VERTICAL )
		self.panel_space2.SetSizer( bSizer_space2 )
		self.panel_space2.Layout()
		bSizer_space2.Fit( self.panel_space2 )
		bSizer_comment.Add( self.panel_space2, 1, wx.EXPAND |wx.ALL, 5 )
#######################

######################


		self.panel_buttom = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_buttom = wx.BoxSizer( wx.HORIZONTAL )

		self.panel_left = wx.Panel( self.panel_buttom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_left = wx.BoxSizer( wx.HORIZONTAL )

		self.button_last = wx.Button( self.panel_left, wx.ID_ANY, u"上一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_left.Add( self.button_last, 0, wx.ALIGN_CENTER|wx.ALL, 30 )


		self.panel_left.SetSizer( bSizer_left )
		self.panel_left.Layout()
		bSizer_left.Fit( self.panel_left )
		bSizer_buttom.Add( self.panel_left, 1, wx.EXPAND |wx.ALL, 5 )
		





		self.panel_leftimg = wx.Panel( self.panel_buttom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_left = wx.BoxSizer( wx.VERTICAL )
		image1 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + jpg_file +  "/" + str(img_num[0]))
		#圖片格式轉換
		image1.Rescale(400,400)
		pic_no = image1.ConvertToBitmap()
		self.bitmap_no = wx.StaticBitmap( self.panel_leftimg, bitmap=pic_no )
		bSizer_left.Add( self.bitmap_no, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


		self.panel_leftimg.SetSizer( bSizer_left )
		self.panel_leftimg.Layout()
		bSizer_left.Fit( self.panel_leftimg )
		bSizer_buttom.Add( self.panel_leftimg, 4, wx.EXPAND |wx.ALL, 5 )







		self.panel_right = wx.Panel( self.panel_buttom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_right = wx.BoxSizer( wx.VERTICAL )

		image2 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + detection_type + "_ove/" + str(img_num[0]))
		#圖片格式轉換
		image2.Rescale(400,400)
		pic_yes = image2.ConvertToBitmap()
		self.bitmap_yes = wx.StaticBitmap( self.panel_right, bitmap=pic_yes )
		bSizer_right.Add( self.bitmap_yes, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		
		self.panel_right.SetSizer( bSizer_right )
		self.panel_right.Layout()
		bSizer_right.Fit( self.panel_right )
		bSizer_buttom.Add( self.panel_right, 4, wx.EXPAND |wx.ALL, 5 )






		self.panel_right_bnt = wx.Panel( self.panel_buttom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_right = wx.BoxSizer( wx.HORIZONTAL )

		self.button_next = wx.Button( self.panel_right_bnt, wx.ID_ANY, u"下一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_right.Add( self.button_next, 0, wx.ALIGN_CENTER|wx.ALL, 30 )



		self.panel_right_bnt.SetSizer( bSizer_right )
		self.panel_right_bnt.Layout()
		bSizer_right.Fit( self.panel_right_bnt )
		bSizer_buttom.Add( self.panel_right_bnt, 1, wx.EXPAND |wx.ALL, 5 )







		self.panel_buttom.SetSizer( bSizer_buttom )
		self.panel_buttom.Layout()
		bSizer_buttom.Fit( self.panel_buttom )
		bSizer.Add( self.panel_buttom, 2, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )
		self.button_next.Bind(wx.EVT_BUTTON, lambda evt, num=img_num,txt=txt_num: self.next_picture(evt,num,txt))
		self.button_last.Bind(wx.EVT_BUTTON, lambda evt, num=img_num,txt=txt_num: self.last_picture(evt,num,txt))
		self.CTSI_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_comment.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_space1.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_dr.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_add.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)	
		self.panel_space2.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_buttom.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_left.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_leftimg.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_right.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)			
		self.panel_right_bnt.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
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
