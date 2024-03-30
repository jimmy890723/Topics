# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from sys import path
import wx
import wx.xrc
import result_gui
import os

###########################################################################
## Class Bnd
###########################################################################
def scale_bitmap(bitmap, width, height):
		image = wx.ImageFromBitmap(bitmap)
		image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
		result = wx.BitmapFromImage(image)
		return result

class Bnd ( wx.Frame ):
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

	def __init__( self, parent,case_number, detection_type):
		img_num = []
		self.imgs(img_num)
		
		result_gui.init(self, parent)


		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

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


		bSizer29.Add( bSizer211, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 20 )

		#--- left ---#
		#--- right ---#

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.staticText_title = TransparentText( self, wx.ID_ANY, label="AI辨識")
		self.staticText_title.Wrap( -1 )
		self.staticText_title.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		bSizer33.Add( self.staticText_title, 0, wx.ALIGN_CENTER|wx.TOP, 20 )


		self.staticText_case_img_num = TransparentText( self, wx.ID_ANY, label="案例編號:"+case_number+"    圖片代號:"+img_num[0])
		self.staticText_case_img_num.Wrap( -1 )
		self.staticText_case_img_num.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		bSizer33.Add( self.staticText_case_img_num, 0, wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM|wx.LEFT, 12 )

		self.img_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		image = wx.Image('../../Data/'+ case_number +'/' + detection_type + '/'+ detection_type + '_bnd/' + img_num[0])
		#圖片格式轉換
		btn_pic = image.ConvertToBitmap()
		self.bitmap_middle = wx.StaticBitmap( self.img_panel, wx.ID_ANY, btn_pic, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer57.Add( self.bitmap_middle, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

		self.img_panel.SetSizer( bSizer57 )
		self.img_panel.Layout()
		bSizer57.Fit( self.img_panel )
		bSizer33.Add( self.img_panel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		last_pic = wx.Image('.\\button_bmp\\PNG\\last_pic.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_last_pic = scale_bitmap(last_pic, 100, 43)
		self.btn_last = wx.BitmapButton( self, wx.ID_ANY, bmp_last_pic, wx.DefaultPosition, wx.Size( 100,40 ), 0 )
		bSizer37.Add( self.btn_last, 0, wx.RIGHT|wx.TOP, 18 )
	
		next_pic = wx.Image('.\\button_bmp\\PNG\\next_pic.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_next_pic = scale_bitmap(next_pic, 100, 43)
		self.btn_next = wx.BitmapButton( self, wx.ID_ANY, bmp_next_pic, wx.DefaultPosition, wx.Size( 100,40 ), 0 )
		bSizer37.Add( self.btn_next, 0, wx.LEFT|wx.TOP, 18 )


		bSizer33.Add( bSizer37, 1, wx.ALIGN_CENTER, 5 )


		bSizer29.Add( bSizer33, 2, wx.EXPAND, 5 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer35.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.TOP, 25 )

		path = "../../Data/"+case_number+"/F1Score/f1out_"+ detection_type + ".txt"
		f = open(path, 'r')
		self.staticText_f1score = TransparentText( self, wx.ID_ANY, label=f.read())
		self.staticText_f1score.Wrap( -1 )
		self.staticText_f1score.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		bSizer35.Add( self.staticText_f1score, 0, wx.ALIGN_CENTER|wx.ALL, 25 )

		bnd_list = []
		xmlpath = "../../Data/"+case_number+"/"+detection_type+"/"+detection_type+"_xml"

		self.ctsi_list_Box = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,520 ), bnd_list, 0 )
		self.ctsi_list_Box.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )
		bSizer35.Add( self.ctsi_list_Box, 0, wx.ALIGN_RIGHT|wx.ALL, 0 )
		for fn in os.listdir(xmlpath):
			if fn != '@eaDir' and fn.split('.')[1] == 'xml':
				f_name = fn.replace("xml","jpg")
				self.ctsi_list_Box.Append(f_name)
		self.Bind(wx.EVT_LISTBOX, self.OnClick_show_bnd, self.ctsi_list_Box)

		edit_pic = wx.Image('.\\button_bmp\\PNG\\edit.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_edit_pic = scale_bitmap(edit_pic, 80, 43)
		self.editbtn = wx.BitmapButton( self, wx.ID_ANY, bmp_edit_pic, wx.DefaultPosition, wx.Size( 80,40 ), 0 )
		bSizer35.Add( self.editbtn, 0, wx.ALIGN_CENTER|wx.TOP, 30 )


		bSizer29.Add( bSizer35, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		pic_reg_path = '.\\button_bmp\\PNG\\recognize_left.png'
		size_recognize = self.m_panel3.GetSize()
		self.m_panel2.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_reg_path, W =size_recognize[0] ,H =size_recognize[1]+10: self.OnEraseBack_pic(evt,path,W,H))
		pic_deal_path = '.\\button_bmp\\PNG\\deal_left.png'
		size_deal = self.m_panel3.GetSize()
		self.m_panel3.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_deal_path, W =size_deal[0] ,H =size_deal[1]: self.OnEraseBack_pic(evt,path,W,H))
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.btn_last.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.last_picture(evt,num))
		self.btn_next.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.next_picture(evt,num))
		self.editbtn.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.Oneditbtn(evt,num))
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
	def __init__( self, parent, case_number , detection_type ):
		img_num = []
		self.imgs(img_num)
		
		result_gui.init(self, parent)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		bSizer_inner = wx.BoxSizer( wx.VERTICAL )

		self.panel_top = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_top = wx.StaticBoxSizer( wx.StaticBox( self.panel_top, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.panel_title = wx.Panel( bSizer_top.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_title = wx.BoxSizer( wx.VERTICAL )

		self.staticText_title = TransparentText( self.panel_title, wx.ID_ANY, label="AI辨識")
		self.staticText_title.Wrap( -1 )
		self.staticText_title.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "標楷體" ) )

		bSizer_title.Add( self.staticText_title, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.panel_title.SetSizer( bSizer_title )
		self.panel_title.Layout()
		bSizer_title.Fit( self.panel_title )
		bSizer_top.Add( self.panel_title, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_inf = wx.Panel( bSizer_top.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_inf = wx.BoxSizer( wx.HORIZONTAL )

####################
		self.panel_f1score2 = wx.Panel( self.panel_inf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_f1score2 = wx.BoxSizer( wx.VERTICAL )

		self.panel_f1score2.SetSizer( bSizer_f1score2 )
		self.panel_f1score2.Layout()
		bSizer_f1score2.Fit( self.panel_f1score2 )
		bSizer_inf.Add( self.panel_f1score2, 1, wx.EXPAND |wx.ALL, 0 )
#################

		self.panel_casenum = wx.Panel( self.panel_inf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_casenum = wx.BoxSizer( wx.VERTICAL )

		self.staticText_case_img_num = TransparentText( self.panel_casenum, wx.ID_ANY, label="案例號碼:"+case_number+"  圖片代號:"+img_num[0])
		self.staticText_case_img_num.Wrap( -1 )
		self.staticText_case_img_num.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "標楷體" ) )

		bSizer_casenum.Add( self.staticText_case_img_num, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


		self.panel_casenum.SetSizer( bSizer_casenum )
		self.panel_casenum.Layout()
		bSizer_casenum.Fit( self.panel_casenum )
		bSizer_inf.Add( self.panel_casenum, 3, wx.EXPAND |wx.ALL, 0 )


		path = "../../Data/"+case_number+"/F1Score/f1out.txt"
		f = open(path, 'r')


		self.panel_f1score = wx.Panel( self.panel_inf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_f1score = wx.BoxSizer( wx.VERTICAL )

		self.staticText_f1score = TransparentText( self.panel_f1score, wx.ID_ANY, label=f.read() )
		self.staticText_f1score.Wrap( -1 )
		self.staticText_f1score.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "標楷體" ) )

		bSizer_f1score.Add( self.staticText_f1score, 0, wx.ALIGN_LEFT|wx.ALL, 0 )


		self.panel_f1score.SetSizer( bSizer_f1score )
		self.panel_f1score.Layout()
		bSizer_f1score.Fit( self.panel_f1score )
		bSizer_inf.Add( self.panel_f1score, 1, wx.EXPAND |wx.ALL, 0 )	

		self.panel_inf.SetSizer( bSizer_inf )
		self.panel_inf.Layout()
		bSizer_inf.Fit( self.panel_inf )
		bSizer_top.Add( self.panel_inf, 1, wx.EXPAND |wx.ALL, 0 )


		self.panel_top.SetSizer( bSizer_top )
		self.panel_top.Layout()
		bSizer_top.Fit( self.panel_top )
		bSizer_inner.Add( self.panel_top, 1, wx.EXPAND |wx.ALL, 0 )
###################################
		self.panel_middle = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_middle = wx.BoxSizer( wx.HORIZONTAL )
		self.panel_middle_space = wx.Panel( self.panel_middle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		bSizer_editbtn = wx.BoxSizer( wx.VERTICAL )
		self.editbtn = wx.Button( self.panel_middle_space, wx.ID_ANY, u"編輯", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_editbtn.Add( self.editbtn, 0, wx.ALIGN_CENTER, 0 )
		self.panel_middle_space.SetSizer( bSizer_editbtn )
		self.panel_middle_space.Layout()
		bSizer_editbtn.Fit( self.panel_middle_space )
		bSizer_editbtn.Add( self.panel_middle_space, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer_middle_space = wx.BoxSizer( wx.VERTICAL )
		self.panel_middle_space.SetSizer( bSizer_middle_space )
		self.panel_middle_space.Layout()
		bSizer_middle_space.Fit( self.panel_middle_space )
		bSizer_middle.Add( self.panel_middle_space, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_middle_img = wx.Panel( self.panel_middle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_middle_img = wx.BoxSizer( wx.VERTICAL )
		image = wx.Image('../../Data/'+ case_number +'/' + detection_type + '/'+ detection_type + '_bnd/' + img_num[0])
		#圖片格式轉換
		btn_pic = image.ConvertToBitmap()
		self.bitmap_middle = wx.StaticBitmap( self.panel_middle_img, bitmap=btn_pic )
		bSizer_middle_img.Add( self.bitmap_middle, 0, wx.ALIGN_CENTER|wx.ALL, 0 )
		self.panel_middle_img.SetSizer( bSizer_middle_img )
		self.panel_middle_img.Layout()
		bSizer_middle_img.Fit( self.panel_middle_img )
		bSizer_middle.Add( self.panel_middle_img, 4, wx.ALIGN_CENTER |wx.ALL, 0 )

		bnd_list = []
		xmlpath = "../../Data/"+case_number+"/"+detection_type+"/"+detection_type+"_xml"

		self.list_panel = wx.Panel( self.panel_middle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_mid_list = wx.BoxSizer( wx.HORIZONTAL )

		self.ctsi_list_Box = wx.ListBox( self.list_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bnd_list, 0 )
		self.ctsi_list_Box.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )
		#self.ctsi_list_Box.SetScrollPos(wx.VERTICAL,self.ctsi_list_Box.GetScrollRange(wx.HORIZONTAL),refresh=True)

		bSizer_mid_list.Add( self.ctsi_list_Box, 0, wx.EXPAND|wx.ALL|wx.Centre, 0 )


		self.list_panel.SetSizer( bSizer_mid_list )
		self.list_panel.Layout()
		bSizer_mid_list.Fit( self.list_panel )
		bSizer_middle.Add( self.list_panel, 1, wx.EXPAND |wx.ALL, 0 )
		for fn in os.listdir(xmlpath):
			if fn != '@eaDir' and fn.split('.')[1] == 'xml':
				f_name = fn.replace("xml","jpg")
				self.ctsi_list_Box.Append(f_name)
		self.Bind(wx.EVT_LISTBOX, self.OnClick_show_bnd, self.ctsi_list_Box)
############################################

		self.panel_middle.SetSizer( bSizer_middle )
		self.panel_middle.Layout()
		bSizer_middle.Fit( self.panel_middle )
		bSizer_inner.Add( self.panel_middle, 0, wx.EXPAND |wx.ALL, 0 )

		self.panel_bottom = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_bottom = wx.StaticBoxSizer( wx.StaticBox( self.panel_bottom, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.panel_bottom_left = wx.Panel( bSizer_bottom.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_bottom.Add( self.panel_bottom_left, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_button = wx.Panel( bSizer_bottom.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_button = wx.BoxSizer( wx.VERTICAL )
		
		self.panelm2up = wx.Panel( self.panel_button, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_button.Add( self.panelm2up, 1, wx.EXPAND |wx.ALL, 0 )

		self.panelm2middle = wx.Panel( self.panel_button, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_button.Add( self.panelm2middle, 1, wx.EXPAND |wx.ALL, 0 )

		self.panelm2bottom = wx.Panel( self.panel_button, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.left_bottom_panel = wx.Panel( self.panelm2bottom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_button13 = wx.Button( self.left_bottom_panel, wx.ID_ANY, u"上一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button13, 0, wx.ALIGN_CENTER, 0 )


		self.left_bottom_panel.SetSizer( bSizer12 )
		self.left_bottom_panel.Layout()
		bSizer12.Fit( self.left_bottom_panel )
		bSizer11.Add( self.left_bottom_panel, 1, wx.EXPAND |wx.ALL, 0 )

		self.right_bottom_panel = wx.Panel( self.panelm2bottom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_button14 = wx.Button( self.right_bottom_panel, wx.ID_ANY, u"下一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button14, 0, wx.ALIGN_CENTER, 0 )

		self.right_bottom_panel.SetSizer( bSizer13 )
		self.right_bottom_panel.Layout()
		bSizer13.Fit( self.right_bottom_panel )
		bSizer11.Add( self.right_bottom_panel, 1, wx.EXPAND |wx.ALL, 0 )


		self.panelm2bottom.SetSizer( bSizer11 )
		self.panelm2bottom.Layout()
		bSizer11.Fit( self.panelm2bottom )
		bSizer_button.Add( self.panelm2bottom, 1, wx.EXPAND |wx.ALL, 0 )


		self.panel_button.SetSizer( bSizer_button )
		self.panel_button.Layout()
		bSizer_button.Fit( self.panel_button )
		bSizer_bottom.Add( self.panel_button, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_bottom_right = wx.Panel( bSizer_bottom.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_bottom.Add( self.panel_bottom_right, 1, wx.EXPAND |wx.ALL, 0 )


		self.panel_bottom.SetSizer( bSizer_bottom )
		self.panel_bottom.Layout()
		bSizer_bottom.Fit( self.panel_bottom )
		bSizer_inner.Add( self.panel_bottom, 1, wx.EXPAND , 0 )


		bSizer.Add( bSizer_inner, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		self.m_button13.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.last_picture(evt,num))
		self.m_button14.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.next_picture(evt,num))
		self.panel_top.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_title.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_inf.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_f1score2.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_f1score.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_casenum.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_middle.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_middle_space.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_middle_img.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_bottom.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panelm2up.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panelm2middle.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panelm2bottom.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.left_bottom_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_bottom_right.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_bottom_left.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_button.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.list_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.right_bottom_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.editbtn.Bind(wx.EVT_BUTTON, self.Oneditbtn)

		
	def OnEraseBack( self, event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap("./logo/blue_bkg3.jpg")
		bitmap = scale_bitmap(bmp, 1300, 800)
		dc.DrawBitmap(bitmap, 0, 0)
'''

class Bnd_edit ( wx.Frame ):

	def __init__( self, parent, case_number , detection_type ):
		img_num = []
		self.imgs(img_num)
		
		result_gui.init(self, parent)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		bSizer_inner = wx.BoxSizer( wx.VERTICAL )

		self.panel_top = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_top = wx.StaticBoxSizer( wx.StaticBox( self.panel_top, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.panel_title = wx.Panel( bSizer_top.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_title = wx.BoxSizer( wx.VERTICAL )

		self.staticText_title = TransparentText( self.panel_title, wx.ID_ANY, label="AI辨識")
		self.staticText_title.Wrap( -1 )
		self.staticText_title.SetFont( wx.Font( 20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		bSizer_title.Add( self.staticText_title, 0, wx.ALIGN_CENTER|wx.ALL, 0 )


		self.panel_title.SetSizer( bSizer_title )
		self.panel_title.Layout()
		bSizer_title.Fit( self.panel_title )
		bSizer_top.Add( self.panel_title, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_inf = wx.Panel( bSizer_top.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_inf = wx.BoxSizer( wx.HORIZONTAL )

####################
		self.panel_f1score2 = wx.Panel( self.panel_inf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_f1score2 = wx.BoxSizer( wx.VERTICAL )

		self.panel_f1score2.SetSizer( bSizer_f1score2 )
		self.panel_f1score2.Layout()
		bSizer_f1score2.Fit( self.panel_f1score2 )
		bSizer_inf.Add( self.panel_f1score2, 1, wx.EXPAND |wx.ALL, 0 )
#################

		self.panel_casenum = wx.Panel( self.panel_inf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_casenum = wx.BoxSizer( wx.VERTICAL )

		self.staticText_case_img_num = TransparentText( self.panel_casenum, wx.ID_ANY, label="案例號碼:"+case_number+"  圖片代號:"+img_num[0])
		self.staticText_case_img_num.Wrap( -1 )
		self.staticText_case_img_num.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		bSizer_casenum.Add( self.staticText_case_img_num, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.panel_casenum.SetSizer( bSizer_casenum )
		self.panel_casenum.Layout()
		bSizer_casenum.Fit( self.panel_casenum )
		bSizer_inf.Add( self.panel_casenum, 3, wx.EXPAND |wx.ALL, 0 )



		path = "../../Data/"+case_number+"/F1score/f1out_"+ detection_type + ".txt"
		f = open(path, 'r')


		self.panel_f1score = wx.Panel( self.panel_inf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_f1score = wx.BoxSizer( wx.VERTICAL )

		self.staticText_f1score = TransparentText( self.panel_f1score, wx.ID_ANY, label=f.read())
		self.staticText_f1score.Wrap( -1 )
		self.staticText_f1score.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		bSizer_f1score.Add( self.staticText_f1score, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


		self.panel_f1score.SetSizer( bSizer_f1score )
		self.panel_f1score.Layout()
		bSizer_f1score.Fit( self.panel_f1score )
		bSizer_inf.Add( self.panel_f1score, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_inf.SetSizer( bSizer_inf )
		self.panel_inf.Layout()
		bSizer_inf.Fit( self.panel_inf )
		bSizer_top.Add( self.panel_inf, 1, wx.EXPAND |wx.ALL, 0 )


		self.panel_top.SetSizer( bSizer_top )
		self.panel_top.Layout()
		bSizer_top.Fit( self.panel_top )
		bSizer_inner.Add( self.panel_top, 1, wx.EXPAND |wx.ALL, 0 )
###################################
		self.panel_middle = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_middle = wx.BoxSizer( wx.HORIZONTAL )

		self.panel_middle_space = wx.Panel( self.panel_middle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_savebtn = wx.BoxSizer( wx.VERTICAL )
		self.savebtn = wx.Button( self.panel_middle_space, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_savebtn.Add( self.savebtn, 0, wx.ALIGN_CENTER, 0 )
		self.panel_middle_space.SetSizer( bSizer_savebtn )
		self.panel_middle_space.Layout()
		bSizer_savebtn.Fit( self.panel_middle_space )
		bSizer_savebtn.Add( self.panel_middle_space, 1, wx.EXPAND |wx.ALL, 0 )





		bSizer_middle_space = wx.BoxSizer( wx.VERTICAL )

		self.panel_middle_space.SetSizer( bSizer_middle_space )
		self.panel_middle_space.Layout()
		bSizer_middle_space.Fit( self.panel_middle_space )
		bSizer_middle.Add( self.panel_middle_space, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_middle_img = wx.Panel( self.panel_middle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_middle_img = wx.BoxSizer( wx.VERTICAL )
		image = wx.Image('../../Data/'+ case_number +'/' + detection_type + '/testmodel/' + case_number +"/" + img_num[0])
		#圖片格式轉換
		btn_pic = image.ConvertToBitmap()
		self.bitmap_middle = wx.StaticBitmap( self.panel_middle_img, bitmap=btn_pic )
		bSizer_middle_img.Add( self.bitmap_middle, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		self.panel_middle_img.SetSizer( bSizer_middle_img )
		self.panel_middle_img.Layout()
		bSizer_middle_img.Fit( self.panel_middle_img )
		bSizer_middle.Add( self.panel_middle_img, 4, wx.ALIGN_CENTER |wx.ALL, 0 )

		bnd_list = []
		xmlpath = "../../Data/"+case_number+"/"+detection_type+"/"+detection_type+"_xml"

		self.list_panel = wx.Panel( self.panel_middle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_mid_list = wx.BoxSizer( wx.HORIZONTAL )

		self.ctsi_list_Box = wx.ListBox( self.list_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bnd_list, 0 )
		self.ctsi_list_Box.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )
		#self.ctsi_list_Box.SetScrollPos(wx.VERTICAL,self.ctsi_list_Box.GetScrollRange(wx.HORIZONTAL),refresh=True)

		bSizer_mid_list.Add( self.ctsi_list_Box, 0, wx.EXPAND|wx.ALL|wx.Centre, 5 )


		self.list_panel.SetSizer( bSizer_mid_list )
		self.list_panel.Layout()
		bSizer_mid_list.Fit( self.list_panel )
		bSizer_middle.Add( self.list_panel, 1, wx.EXPAND |wx.ALL, 0 )
		for fn in os.listdir(xmlpath):
			if fn != '@eaDir' and fn.split('.')[1] == 'xml':
				f_name = fn.replace("xml","jpg")
				self.ctsi_list_Box.Append(f_name)
		self.Bind(wx.EVT_LISTBOX, self.OnClick_show_bnd, self.ctsi_list_Box)
############################################

		self.panel_middle.SetSizer( bSizer_middle )
		self.panel_middle.Layout()
		bSizer_middle.Fit( self.panel_middle )
		bSizer_inner.Add( self.panel_middle, 5, wx.EXPAND |wx.ALL, 0 )

		self.panel_bottom = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_bottom = wx.StaticBoxSizer( wx.StaticBox( self.panel_bottom, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.panel_bottom_left = wx.Panel( bSizer_bottom.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_bottom.Add( self.panel_bottom_left, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_button = wx.Panel( bSizer_bottom.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_button = wx.BoxSizer( wx.VERTICAL )

		self.panelm2up = wx.Panel( self.panel_button, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_button.Add( self.panelm2up, 1, wx.EXPAND |wx.ALL, 0 )

		self.panelm2middle = wx.Panel( self.panel_button, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_button.Add( self.panelm2middle, 1, wx.EXPAND |wx.ALL, 0 )

		self.panelm2bottom = wx.Panel( self.panel_button, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.left_bottom_panel = wx.Panel( self.panelm2bottom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_button13 = wx.Button( self.left_bottom_panel, wx.ID_ANY, u"上一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button13, 0, wx.ALIGN_CENTER, 0 )


		self.left_bottom_panel.SetSizer( bSizer12 )
		self.left_bottom_panel.Layout()
		bSizer12.Fit( self.left_bottom_panel )
		bSizer11.Add( self.left_bottom_panel, 1, wx.EXPAND |wx.ALL, 0 )

		self.right_bottom_panel = wx.Panel( self.panelm2bottom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_button14 = wx.Button( self.right_bottom_panel, wx.ID_ANY, u"下一張", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button14, 0, wx.ALIGN_CENTER, 0 )


		self.right_bottom_panel.SetSizer( bSizer13 )
		self.right_bottom_panel.Layout()
		bSizer13.Fit( self.right_bottom_panel )
		bSizer11.Add( self.right_bottom_panel, 1, wx.EXPAND |wx.ALL, 0 )


		self.panelm2bottom.SetSizer( bSizer11 )
		self.panelm2bottom.Layout()
		bSizer11.Fit( self.panelm2bottom )
		bSizer_button.Add( self.panelm2bottom, 1, wx.EXPAND |wx.ALL, 0 )


		self.panel_button.SetSizer( bSizer_button )
		self.panel_button.Layout()
		bSizer_button.Fit( self.panel_button )
		bSizer_bottom.Add( self.panel_button, 1, wx.EXPAND |wx.ALL, 0 )

		self.panel_bottom_right = wx.Panel( bSizer_bottom.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_bottom.Add( self.panel_bottom_right, 1, wx.EXPAND |wx.ALL, 0 )


		self.panel_bottom.SetSizer( bSizer_bottom )
		self.panel_bottom.Layout()
		bSizer_bottom.Fit( self.panel_bottom )
		bSizer_inner.Add( self.panel_bottom, 1, wx.EXPAND |wx.ALL, 0 )


		bSizer.Add( bSizer_inner, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		self.m_button13.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.last_picture(evt,num))
		self.m_button14.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.next_picture(evt,num))
		anchor_position = []
		self.savebtn.Bind(wx.EVT_BUTTON, lambda evt, num=img_num, anchor=anchor_position: self.Onsavebtn(evt,num,anchor))
		self.bitmap_middle.Bind(wx.EVT_LEFT_DOWN, self.Onminpoint)
		self.bitmap_middle.Bind(wx.EVT_LEFT_UP,lambda evt, anchor=anchor_position: self.Onmaxpoint(evt,anchor))
		self.m_button13.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.last_picture(evt,num))
		self.m_button14.Bind(wx.EVT_BUTTON, lambda evt, num=img_num: self.next_picture(evt,num))
		self.panel_top.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_title.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_inf.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_f1score2.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_f1score.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_casenum.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_middle.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_middle_space.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_middle_img.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_bottom.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panelm2up.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panelm2middle.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panelm2bottom.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.left_bottom_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_bottom_right.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_bottom_left.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.panel_button.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.list_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.right_bottom_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)

	def OnEraseBack( self, event):
		dc = event.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		bmp = wx.Bitmap("./logo/blue_bkg3.jpg")
		bitmap = scale_bitmap(bmp, 1300, 800)
		dc.DrawBitmap(bitmap, 0, 0)

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

if __name__ == "__main__":
    app = wx.App()
    frm = Bnd(None)
    frm.Show()
    app.MainLoop()