import wx
import wx.xrc
import os
from pydicom import dcmread 

def init(self, parent):
    wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統 - 結果查看', pos=wx.DefaultPosition, size=wx.Size(
        1300, 800), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)

    self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

    bSizer2 = wx.BoxSizer(wx.VERTICAL)

    bSizer3 = wx.BoxSizer(wx.VERTICAL)

    bSizer2.Add(bSizer3, 1, wx.EXPAND, 5)

    self.SetSizer(bSizer2)
    self.Layout()
    self.m_menubar1 = wx.MenuBar(0)
    self.Identify = wx.Menu()
    self.Pancreas = wx.MenuItem(
        self.Identify, wx.ID_ANY, u"胰臟", wx.EmptyString, wx.ITEM_NORMAL)
    self.Identify.Append(self.Pancreas)

    self.Effusion = wx.MenuItem(
        self.Identify, wx.ID_ANY, u"積液", wx.EmptyString, wx.ITEM_NORMAL)
    self.Identify.Append(self.Effusion)

    self.m_menubar1.Append(self.Identify, u"影像辨識")

    self.Deal = wx.Menu()
    self.Pancreas1 = wx.Menu()
    self.compara1 = wx.MenuItem(self.Pancreas1, wx.ID_ANY,
                            u"疊圖比較", wx.EmptyString, wx.ITEM_NORMAL)
    self.Pancreas1.Append(self.compara1)

    self.cut_pancreas = wx.MenuItem(self.Pancreas1, wx.ID_ANY,
                            u"分割結果", wx.EmptyString, wx.ITEM_NORMAL)
    self.Pancreas1.Append(self.cut_pancreas)

    self.Deal.AppendSubMenu(self.Pancreas1, u"胰腺")

    self.Effusion1 = wx.Menu()
    self.compara2 = wx.MenuItem(self.Effusion1, wx.ID_ANY,
                            u"疊圖比較", wx.EmptyString, wx.ITEM_NORMAL)
    self.Effusion1.Append(self.compara2)

    self.cut_effusion = wx.MenuItem(self.Effusion1, wx.ID_ANY,
                            u"分割結果", wx.EmptyString, wx.ITEM_NORMAL)
    self.Effusion1.Append(self.cut_effusion)

    self.Deal.AppendSubMenu(self.Effusion1, u"積液")

    self.CTSI = wx.MenuItem(self.Deal, wx.ID_ANY,
                            u"CTSI", wx.EmptyString, wx.ITEM_NORMAL)
    self.Deal.Append(self.CTSI)

    self.m_menubar1.Append(self.Deal, u"Deal")

    self.m_menu4 = wx.Menu()
    self.Start = wx.MenuItem(
        self.m_menu4, wx.ID_ANY, u"開始", wx.EmptyString, wx.ITEM_NORMAL)
    self.m_menu4.Append(self.Start)

    self.m_menubar1.Append(self.m_menu4, u"3D")

    self.final_r = wx.Menu()
    self.Result = wx.MenuItem(
        self.final_r, wx.ID_ANY, u"報告", wx.EmptyString, wx.ITEM_NORMAL)
    self.final_r.Append(self.Result)

    self.m_menubar1.Append(self.final_r, u"結果報告")

    self.m_menu5 = wx.Menu()
    self.Home = wx.MenuItem(
        self.m_menu5, wx.ID_ANY, u"回到首頁", wx.EmptyString, wx.ITEM_NORMAL)
    self.m_menu5.Append(self.Home)

    self.m_menubar1.Append(self.m_menu5, u"首頁")
    

    self.SetMenuBar(self.m_menubar1)

    self.Centre(wx.BOTH)
    self.Bind(wx.EVT_MENU, self.OnClick_pancreas, self.Pancreas)
    self.Bind(wx.EVT_MENU, self.OnClick_effusion, self.Effusion)
    self.Bind(wx.EVT_MENU, self.OnClick_pancreas_compara, self.compara1)
    self.Bind(wx.EVT_MENU, self.OnClick_effusion_compara, self.compara2)
    self.Bind(wx.EVT_MENU, self.OnClick_cut_pancreas, self.cut_pancreas)
    self.Bind(wx.EVT_MENU, self.OnClick_cut_effusion, self.cut_effusion)
    self.Bind(wx.EVT_MENU, self.CTSI_Score, self.CTSI)
    self.Bind(wx.EVT_MENU, self.Start_page, self.Start)
    self.Bind(wx.EVT_MENU, self.FReport_page, self.Result)
    self.Bind(wx.EVT_MENU, self.Home_page, self.Home)
    

def init2(self, parent):
    wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統 - 分析', pos=wx.DefaultPosition, size=wx.Size(
        500, 300), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)

    self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

    bSizer2 = wx.BoxSizer(wx.VERTICAL)

    bSizer3 = wx.BoxSizer(wx.VERTICAL)

    bSizer2.Add(bSizer3, 1, wx.EXPAND, 5)

    self.SetSizer(bSizer2)
    self.Layout()
    self.m_menubar1 = wx.MenuBar(0)
    self.Identify = wx.Menu()
    self.Pancreas = wx.MenuItem(
        self.Identify, wx.ID_ANY, u"胰臟", wx.EmptyString, wx.ITEM_NORMAL)
    self.Identify.Append(self.Pancreas)

    self.Effusion = wx.MenuItem(
        self.Identify, wx.ID_ANY, u"積液", wx.EmptyString, wx.ITEM_NORMAL)
    self.Identify.Append(self.Effusion)

    self.m_menubar1.Append(self.Identify, u"影像辨識")

    self.Deal = wx.Menu()
    self.Pancreas1 = wx.Menu()
    self.compara1 = wx.MenuItem(self.Pancreas1, wx.ID_ANY,
                            u"疊圖比較", wx.EmptyString, wx.ITEM_NORMAL)
    self.Pancreas1.Append(self.compara1)

    self.cut_pancreas = wx.MenuItem(self.Pancreas1, wx.ID_ANY,
                            u"分割結果", wx.EmptyString, wx.ITEM_NORMAL)
    self.Pancreas1.Append(self.cut_pancreas)

    self.Deal.AppendSubMenu(self.Pancreas1, u"胰腺")

    self.Effusion1 = wx.Menu()
    self.compara2 = wx.MenuItem(self.Effusion1, wx.ID_ANY,
                            u"疊圖比較", wx.EmptyString, wx.ITEM_NORMAL)
    self.Effusion1.Append(self.compara2)

    self.cut_effusion = wx.MenuItem(self.Effusion1, wx.ID_ANY,
                            u"分割結果", wx.EmptyString, wx.ITEM_NORMAL)
    self.Effusion1.Append(self.cut_effusion)

    self.Deal.AppendSubMenu(self.Effusion1, u"積液")

    self.CTSI = wx.MenuItem(self.Deal, wx.ID_ANY,
                            u"CTSI", wx.EmptyString, wx.ITEM_NORMAL)
    self.Deal.Append(self.CTSI)

    self.m_menubar1.Append(self.Deal, u"Deal")

    self.m_menu4 = wx.Menu()
    self.Start = wx.MenuItem(
        self.m_menu4, wx.ID_ANY, u"開始", wx.EmptyString, wx.ITEM_NORMAL)
    self.m_menu4.Append(self.Start)

    self.m_menubar1.Append(self.m_menu4, u"3D")

    self.final_r = wx.Menu()
    self.Result = wx.MenuItem(
        self.final_r, wx.ID_ANY, u"報告", wx.EmptyString, wx.ITEM_NORMAL)
    self.final_r.Append(self.Result)

    self.m_menubar1.Append(self.final_r, u"結果報告")



    self.m_menu5 = wx.Menu()
    self.Home = wx.MenuItem(
        self.m_menu5, wx.ID_ANY, u"回到首頁", wx.EmptyString, wx.ITEM_NORMAL)
    self.m_menu5.Append(self.Home)

    self.m_menubar1.Append(self.m_menu5, u"首頁")
    

    self.SetMenuBar(self.m_menubar1)

    self.Centre(wx.BOTH)
    self.Bind(wx.EVT_MENU, self.OnClick_pancreas, self.Pancreas)
    self.Bind(wx.EVT_MENU, self.OnClick_effusion, self.Effusion)
    self.Bind(wx.EVT_MENU, self.OnClick_pancreas_compara, self.compara1)
    self.Bind(wx.EVT_MENU, self.OnClick_effusion_compara, self.compara2)
    self.Bind(wx.EVT_MENU, self.OnClick_cut_pancreas, self.cut_pancreas)
    self.Bind(wx.EVT_MENU, self.OnClick_cut_effusion, self.cut_effusion)
    self.Bind(wx.EVT_MENU, self.CTSI_Score, self.CTSI)
    self.Bind(wx.EVT_MENU, self.Start_page, self.Start)
    self.Bind(wx.EVT_MENU, self.FReport_page, self.Result)
    self.Bind(wx.EVT_MENU, self.Home_page, self.Home)

def ctsi_init(self, parent):
    wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統 - CTSI評分', pos=wx.DefaultPosition, size=wx.Size(
        800, 700), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)

    self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

    bSizer2 = wx.BoxSizer(wx.VERTICAL)

    bSizer3 = wx.BoxSizer(wx.VERTICAL)

    bSizer2.Add(bSizer3, 1, wx.EXPAND, 5)

    self.SetSizer(bSizer2)
    self.Layout()
    self.m_menubar1 = wx.MenuBar(0)
    self.Identify = wx.Menu()
    self.Pancreas = wx.MenuItem(
        self.Identify, wx.ID_ANY, u"胰臟", wx.EmptyString, wx.ITEM_NORMAL)
    self.Identify.Append(self.Pancreas)

    self.Effusion = wx.MenuItem(
        self.Identify, wx.ID_ANY, u"積液", wx.EmptyString, wx.ITEM_NORMAL)
    self.Identify.Append(self.Effusion)

    self.m_menubar1.Append(self.Identify, u"影像辨識")

    self.Deal = wx.Menu()
    self.Pancreas1 = wx.Menu()
    self.compara1 = wx.MenuItem(self.Pancreas1, wx.ID_ANY,
                            u"疊圖比較", wx.EmptyString, wx.ITEM_NORMAL)
    self.Pancreas1.Append(self.compara1)

    self.cut_pancreas = wx.MenuItem(self.Pancreas1, wx.ID_ANY,
                            u"分割結果", wx.EmptyString, wx.ITEM_NORMAL)
    self.Pancreas1.Append(self.cut_pancreas)

    self.Deal.AppendSubMenu(self.Pancreas1, u"胰腺")

    self.Effusion1 = wx.Menu()
    self.compara2 = wx.MenuItem(self.Effusion1, wx.ID_ANY,
                            u"疊圖比較", wx.EmptyString, wx.ITEM_NORMAL)
    self.Effusion1.Append(self.compara2)

    self.cut_effusion = wx.MenuItem(self.Effusion1, wx.ID_ANY,
                            u"分割結果", wx.EmptyString, wx.ITEM_NORMAL)
    self.Effusion1.Append(self.cut_effusion)

    self.Deal.AppendSubMenu(self.Effusion1, u"積液")

    self.CTSI = wx.MenuItem(self.Deal, wx.ID_ANY,
                            u"CTSI", wx.EmptyString, wx.ITEM_NORMAL)
    self.Deal.Append(self.CTSI)

    self.m_menubar1.Append(self.Deal, u"Deal")

    self.m_menu4 = wx.Menu()
    self.Start = wx.MenuItem(
        self.m_menu4, wx.ID_ANY, u"開始", wx.EmptyString, wx.ITEM_NORMAL)
    self.m_menu4.Append(self.Start)

    self.m_menubar1.Append(self.m_menu4, u"3D")

    self.final_r = wx.Menu()
    self.Result = wx.MenuItem(
        self.final_r, wx.ID_ANY, u"報告", wx.EmptyString, wx.ITEM_NORMAL)
    self.final_r.Append(self.Result)

    self.m_menubar1.Append(self.final_r, u"結果報告")


    self.m_menu5 = wx.Menu()
    self.Home = wx.MenuItem(
        self.m_menu5, wx.ID_ANY, u"回到首頁", wx.EmptyString, wx.ITEM_NORMAL)
    self.m_menu5.Append(self.Home)

    self.m_menubar1.Append(self.m_menu5, u"首頁")
    

    self.SetMenuBar(self.m_menubar1)

    self.Centre(wx.BOTH)
    self.Bind(wx.EVT_MENU, self.OnClick_pancreas, self.Pancreas)
    self.Bind(wx.EVT_MENU, self.OnClick_effusion, self.Effusion)
    self.Bind(wx.EVT_MENU, self.OnClick_pancreas_compara, self.compara1)
    self.Bind(wx.EVT_MENU, self.OnClick_effusion_compara, self.compara2)
    self.Bind(wx.EVT_MENU, self.OnClick_cut_pancreas, self.cut_pancreas)
    self.Bind(wx.EVT_MENU, self.OnClick_cut_effusion, self.cut_effusion)
    self.Bind(wx.EVT_MENU, self.CTSI_Score, self.CTSI)
    self.Bind(wx.EVT_MENU, self.Start_page, self.Start)
    self.Bind(wx.EVT_MENU, self.FReport_page, self.Result)
    self.Bind(wx.EVT_MENU, self.Home_page, self.Home)
class Result_Frame( wx.Frame ):
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
	
	

	def __init__( self, parent, case_number ):
		init(self, parent)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer3 = wx.GridSizer( 2, 2, 0, 0 )

		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer73 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel20 = wx.Panel( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText23 = wx.StaticText( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer74.Add( self.m_staticText23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer75 = wx.BoxSizer( wx.HORIZONTAL )

		reg_pan_choose = wx.Image('.\\button_bmp\\PNG\\reg_pan_choose.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_reg_pan = scale_bitmap(reg_pan_choose, 180, 140)
		self.btn_reg_pan = wx.BitmapButton( self.m_panel20, wx.ID_ANY, bmp_reg_pan, wx.DefaultPosition, wx.Size( 180,140 ), 0)
		bSizer75.Add( self.btn_reg_pan, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 30 )

		reg_eff_choose = wx.Image('.\\button_bmp\\PNG\\reg_eff_choose.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_reg_eff = scale_bitmap(reg_eff_choose, 180, 140)
		self.btn_reg_eff = wx.BitmapButton( self.m_panel20, wx.ID_ANY, bmp_reg_eff, wx.DefaultPosition, wx.Size( 180,140 ), 0 )
		bSizer75.Add( self.btn_reg_eff, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 30 )


		bSizer74.Add( bSizer75, 1, wx.EXPAND|wx.RIGHT, 6 )


		self.m_panel20.SetSizer( bSizer74 )
		self.m_panel20.Layout()
		bSizer74.Fit( self.m_panel20 )
		bSizer73.Add( self.m_panel20, 1, wx.ALL|wx.BOTTOM|wx.EXPAND|wx.TOP, 5 )


		self.m_panel18.SetSizer( bSizer73 )
		self.m_panel18.Layout()
		bSizer73.Fit( self.m_panel18 )
		gSizer3.Add( self.m_panel18, 1, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 40 )

		self.m_panel181 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer731 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel201 = wx.Panel( self.m_panel181, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer741 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText231 = wx.StaticText( self.m_panel201, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )

		bSizer741.Add( self.m_staticText231, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer751 = wx.BoxSizer( wx.HORIZONTAL )

		deal_pan_choose = wx.Image('.\\button_bmp\\PNG\\deal_pan_choose.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_pan = scale_bitmap(deal_pan_choose, 115, 140)
		self.btn_deal_pan = wx.BitmapButton( self.m_panel201, wx.ID_ANY, bmp_deal_pan, wx.DefaultPosition, wx.Size( 115,140 ), 0 )
		bSizer751.Add( self.btn_deal_pan, 0, wx.BOTTOM|wx.LEFT|wx.TOP, 30 )

		deal_eff_choose = wx.Image('.\\button_bmp\\PNG\\deal_eff_choose.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_eff = scale_bitmap(deal_eff_choose, 115, 140)
		self.btn_deal_eff = wx.BitmapButton( self.m_panel201, wx.ID_ANY, bmp_deal_eff, wx.DefaultPosition, wx.Size( 115,140 ), 0 )
		bSizer751.Add( self.btn_deal_eff, 0, wx.ALL, 30 )

		deal_CTSI_choose = wx.Image('.\\button_bmp\\PNG\\deal_CTSI_choose.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_deal_CTSI = scale_bitmap(deal_CTSI_choose, 115, 140)
		self.btn_deal_CTSI = wx.BitmapButton( self.m_panel201, wx.ID_ANY, bmp_deal_CTSI, wx.DefaultPosition, wx.Size( 115,140 ), 0 )
		bSizer751.Add( self.btn_deal_CTSI, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 30 )


		bSizer741.Add( bSizer751, 1, wx.EXPAND|wx.RIGHT, 0 )


		self.m_panel201.SetSizer( bSizer741 )
		self.m_panel201.Layout()
		bSizer741.Fit( self.m_panel201 )
		bSizer731.Add( self.m_panel201, 1, wx.ALL|wx.BOTTOM|wx.EXPAND|wx.TOP, 6 )


		self.m_panel181.SetSizer( bSizer731 )
		self.m_panel181.Layout()
		bSizer731.Fit( self.m_panel181 )
		gSizer3.Add( self.m_panel181, 1, wx.ALIGN_BOTTOM|wx.ALIGN_LEFT|wx.ALL|wx.LEFT, 40 )

		ThreeD_choose = wx.Image('.\\button_bmp\\PNG\\3D_choose.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_ThreeD_choose = scale_bitmap(ThreeD_choose, 468, 234)
		self.btn_TreeD_choose = wx.BitmapButton( self, wx.ID_ANY, bmp_ThreeD_choose, wx.DefaultPosition, wx.Size( 468,234 ), 0 )
		gSizer3.Add( self.btn_TreeD_choose, 0, wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.RIGHT|wx.TOP, 40 )

		result_choose = wx.Image('.\\button_bmp\\PNG\\result_choose.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		bmp_result_choose = scale_bitmap(result_choose, 476, 234)
		self.btn_result_choose = wx.BitmapButton( self, wx.ID_ANY, bmp_result_choose, wx.DefaultPosition, wx.Size( 476,234 ), 0 )
		gSizer3.Add( self.btn_result_choose, 0, wx.ALIGN_LEFT|wx.ALIGN_TOP|wx.LEFT|wx.TOP, 40 )


		self.SetSizer( gSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		pic_reg_path = '.\\button_bmp\\PNG\\recognize_choose.png'
		size_reg = self.m_panel20.GetSize()
		self.m_panel20.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_reg_path, W =size_reg[0] ,H =size_reg[1]: self.OnEraseBack_pic(evt,path,W,H))
		pic_deal_path = '.\\button_bmp\\PNG\\deal_choose.png'
		size_deal = self.m_panel201.GetSize()
		self.m_panel201.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_deal_path, W =size_deal[0] ,H =size_deal[1]: self.OnEraseBack_pic(evt,path,W,H))
		self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
		self.btn_reg_pan.Bind( wx.EVT_BUTTON, self.OnClick_pancreas )
		self.btn_reg_eff.Bind( wx.EVT_BUTTON, self.OnClick_effusion )
		self.btn_deal_pan.Bind( wx.EVT_BUTTON, self.OnClick_pancreas_compara )
		self.btn_deal_eff.Bind( wx.EVT_BUTTON, self.OnClick_effusion_compara )
		self.btn_deal_CTSI.Bind( wx.EVT_BUTTON, self.CTSI_Score )
		self.btn_TreeD_choose.Bind( wx.EVT_BUTTON, self.Start_page )
		self.btn_result_choose.Bind( wx.EVT_BUTTON, self.FReport_page )
	def __del__( self ):
		pass    

class First_Fram (wx.Frame):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX )
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        Title_Sizer = wx.BoxSizer( wx.VERTICAL )
        self.Title_staticText_1 = TransparentText( self, wx.ID_ANY, label="歡迎使用")
        self.Title_staticText_1.Wrap( -1 )

        self.Title_staticText_1.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

        Title_Sizer.Add( self.Title_staticText_1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.Title_staticText_2 = TransparentText( self, wx.ID_ANY, label="3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統" )
        self.Title_staticText_2.Wrap( -1 )

        self.Title_staticText_2.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

        Title_Sizer.Add( self.Title_staticText_2, 0, wx.ALIGN_CENTER|wx.ALL, 15 )
        
        START_pic = wx.Image('.\\button_bmp\\PNG\\START.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        bmp_START = scale_bitmap(START_pic, 80, 45)
        self.btn_START = wx.BitmapButton( self, wx.ID_ANY, bmp_START, wx.DefaultPosition, wx.Size( 80,40 ), 0 )
        Title_Sizer.Add( self.btn_START, 0, wx.ALIGN_CENTER|wx.TOP, 165 )
        
        self.SetSizer( Title_Sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        self.btn_START.Bind( wx.EVT_BUTTON, self.Onclick_StartFrame )
        self.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)

    def __del__( self ):
        pass


###########################################################################
## Class StartFrame
###########################################################################
class StartFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統 - 首頁", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX )

        case_data = []
        Nowpath = os.getcwd()
        paths = Nowpath + '\\..\\..\\Data'
        files = os.listdir(paths)
        tmp_counter = 0
        
        for fn in files:
            tmp_fn = fn.split('-')
                
            if fn.isdigit() == True:
                tmp_counter += 1 
            else:
                check_str = 0
                for str_count in range(len(tmp_fn)):
                    if tmp_fn[str_count].isdigit() == False:
                        check_str = 1
                        break
                if check_str == 0:
                    tmp_counter += 1 
        for i in range(tmp_counter):
            case_data.append([])
        counter = 0        
        for fn in files:
            tmp_fn = fn.split('-')
            if fn.isdigit() == True:
                file_case = []
                path_1 = paths + '\\' + fn + '\\' + fn 
                file_tmp = os.listdir(path_1)
                for ff in file_tmp:
                    if ff.endswith('.dcm') == True:
                        file_case.append(ff)
                if len(file_case) == 0:
                    print('case:' + fn + '，檔案內容有誤，請檢察')
                    continue
                ds = dcmread(path_1 + '\\' + file_case[0])
                case_data[counter].append(fn)
                case_data[counter].append(str(ds[0x0010, 0x0010].value))
                case_data[counter].append(str(ds[0x0010, 0x0040].value))
                path_2 = paths + '\\' + fn + '\\path'
                check_done = os.listdir(path_2)
                check_Y = 0
                for f in check_done:
                    if f == '3_line_dcm':
                        case_data[counter].append('Y')
                        check_Y = 1
                        break 
                if check_Y == 0:
                    case_data[counter].append('N')
                counter += 1
            else:
                check_str = 0
                for str_count in range(len(tmp_fn)):
                    if tmp_fn[str_count].isdigit() == False:
                        check_str = 1
                        break
                if check_str == 0:
                    file_case = []
                    path_1 = paths + '\\' + fn + '\\' + fn 
                    file_tmp = os.listdir(path_1)
                    for ff in file_tmp:
                        if ff.endswith('.dcm') == True:
                            file_case.append(ff)
                    if len(file_case) == 0:
                        print('case:' + fn + '，檔案內容有誤，請檢察')
                        continue
                    ds = dcmread(path_1 + '\\' + file_case[0])
                    case_data[counter].append(fn)
                    case_data[counter].append(str(ds[0x0010, 0x0010].value))
                    case_data[counter].append(str(ds[0x0010, 0x0040].value))
                    path_2 = paths + '\\' + fn + '\\path'
                    check_done = os.listdir(path_2)
                    check_Y = 0
                    for f in check_done:
                        if f == '3_line_dcm':
                            case_data[counter].append('Y')
                            check_Y = 1
                            break 
                    if check_Y == 0:
                        case_data[counter].append('N')
                    counter += 1
                     

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        Title_bSizer = wx.BoxSizer( wx.VERTICAL )

        self.Title_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Title_bSizer_mid = wx.BoxSizer( wx.HORIZONTAL )
        
        self.Title_panel_left = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Title_bSizer_mid.Add( self.Title_panel_left, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.Title_panel_mid = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

        self.Title_staticText_mid2 = TransparentText( self.Title_panel, wx.ID_ANY, label="3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統")
        self.Title_staticText_mid2.Wrap( -1 )

        self.Title_staticText_mid2.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

        Title_bSizer_mid.Add( self.Title_staticText_mid2, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 30 )


        self.Title_panel_mid.Layout()

        Title_bSizer_mid.Add( self.Title_panel_mid, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.Title_panel_right = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Title_bSizer_mid.Add( self.Title_panel_right, 1, wx.EXPAND |wx.ALL, 5 )
        

        self.Title_panel.SetSizer( Title_bSizer_mid )
        self.Title_panel.Layout()
        Title_bSizer_mid.Fit( self.Title_panel )
        Title_bSizer.Add( self.Title_panel, 1, wx.EXPAND |wx.ALL, 0 )



        self.Title_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Case_number_bSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.Case_number_panel_left = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Case_number_bSizer.Add( self.Case_number_panel_left, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.Case_number_panel_mid = wx.Panel( self.Title_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Case_number_bSizer_mid = wx.BoxSizer( wx.VERTICAL )

        self.list = wx.ListCtrl(self.Case_number_panel_mid, -1, style = wx.LC_REPORT) 
        self.list.InsertColumn(0, '案例碼', width = 100 ) 
        self.list.InsertColumn(1, '姓名', wx.LIST_FORMAT_CENTER, 180) 
        self.list.InsertColumn(2, '性別', wx.LIST_FORMAT_CENTER, 50) 
        self.list.InsertColumn(3, '是否完成分析', wx.LIST_FORMAT_CENTER,100)

        for i in case_data: 
            index = self.list.InsertStringItem(2, i[0]) 
            self.list.SetStringItem(index, 1, i[1]) 
            self.list.SetStringItem(index, 2, i[2])
            self.list.SetStringItem(index, 3, i[3])  

        Case_number_bSizer_mid.Add( self.list, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.Case_number_panel_mid.SetSizer( Case_number_bSizer_mid )
        self.Case_number_panel_mid.Layout()
        Case_number_bSizer_mid.Fit( self.Case_number_panel_mid )
        Case_number_bSizer.Add( self.Case_number_panel_mid, 1, wx.EXPAND |wx.ALL, 5 )

        self.Case_number_panel_right = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Case_number_bSizer.Add( self.Case_number_panel_right, 1, wx.EXPAND |wx.ALL, 5 )


        self.Title_panel2.SetSizer( Case_number_bSizer )
        self.Title_panel2.Layout()
        Case_number_bSizer.Fit( self.Title_panel2 )
        Title_bSizer.Add( self.Title_panel2, 1, wx.EXPAND |wx.ALL, 0 )

        self.Item_choose = wx.StaticText( self, wx.ID_ANY, label="未選取任一案例")
        self.Item_choose.Wrap( -1 )

        Title_bSizer.Add( self.Item_choose, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.Button_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Button_bSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.Button_panel_left = wx.Panel( self.Button_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Button_bSizer.Add( self.Button_panel_left, 1, wx.EXPAND |wx.ALL, 5 )
        

        self.Button_panel_mid = wx.Panel( self.Button_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Button_bSizer_mid = wx.BoxSizer( wx.HORIZONTAL )

        import_file_pic = wx.Image('.\\button_bmp\\PNG\\import_file.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        bmp_import_file = scale_bitmap(import_file_pic, 85, 35)
        self.Button_import = wx.BitmapButton( self.Button_panel_mid, wx.ID_ANY, bmp_import_file, wx.DefaultPosition, wx.Size( 85,35 ), 0 )
        Button_bSizer_mid.Add( self.Button_import, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.BOTTOM, 10 )

        analysis_case_pic = wx.Image('.\\button_bmp\\PNG\\analysis_case.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        bmp_analysis_case = scale_bitmap(analysis_case_pic, 85, 35)
        self.Button_run_code = wx.BitmapButton( self.Button_panel_mid, wx.ID_ANY, bmp_analysis_case, wx.DefaultPosition, wx.Size( 85,35 ), 0 )
        Button_bSizer_mid.Add( self.Button_run_code, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.BOTTOM, 10 )
    
        search_result_pic = wx.Image('.\\button_bmp\\PNG\\search_result.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        bmp_search_result = scale_bitmap(search_result_pic, 85, 35)
        self.Button_result = wx.BitmapButton( self.Button_panel_mid, wx.ID_ANY, bmp_search_result, wx.DefaultPosition, wx.Size( 85,35 ), 0 )
        Button_bSizer_mid.Add( self.Button_result, 0, wx.TOP | wx.RIGHT | wx.LEFT | wx.BOTTOM, 10 )
        '''
        self.Button_import = wx.Button( self.Button_panel_mid, wx.ID_ANY, u"匯入檔案", wx.DefaultPosition, wx.DefaultSize, 0 )
        Button_bSizer_mid.Add( self.Button_import, 0, wx.TOP | wx.RIGHT | wx.LEFT, 10 )

        self.Button_run_code = wx.Button( self.Button_panel_mid, wx.ID_ANY, u"分析案例", wx.DefaultPosition, wx.DefaultSize, 0 )
        Button_bSizer_mid.Add( self.Button_run_code, 0, wx.TOP | wx.RIGHT | wx.LEFT, 10 )

        self.Button_result = wx.Button( self.Button_panel_mid, wx.ID_ANY, u"查看結果", wx.DefaultPosition, wx.DefaultSize, 0 )
        Button_bSizer_mid.Add( self.Button_result, 0, wx.TOP | wx.RIGHT | wx.LEFT, 10 )
        '''
        self.Button_panel_mid.SetSizer( Button_bSizer_mid )
        self.Button_panel_mid.Layout()
        Button_bSizer_mid.Fit( self.Button_panel_mid )
        Button_bSizer.Add( self.Button_panel_mid, 1, wx.EXPAND |wx.ALL, 5 )

        self.Button_panel_right = wx.Panel( self.Button_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        Button_bSizer.Add( self.Button_panel_right, 1, wx.EXPAND |wx.ALL, 5 )


        self.Button_panel.SetSizer( Button_bSizer )
        self.Button_panel.Layout()
        Button_bSizer.Fit( self.Button_panel )
        Title_bSizer.Add( self.Button_panel, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( Title_bSizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.Onclick_Item )
        self.Button_run_code.Bind( wx.EVT_BUTTON, self.Onclick_run_code )
        self.Button_result.Bind( wx.EVT_BUTTON, self.Onclick_Result )
        self.Button_import.Bind( wx.EVT_BUTTON, self.Onclick_import_file)
        self.Title_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Title_panel2.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Title_panel_mid.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Case_number_panel_left.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Case_number_panel_right.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Button_panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Button_panel_left.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Button_panel_right.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.Button_panel_mid.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)

    def __del__( self ):
        pass

def scale_bitmap(bitmap, width, height):
	image = wx.ImageFromBitmap(bitmap)
	image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
	result = wx.BitmapFromImage(image)
	return result

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
