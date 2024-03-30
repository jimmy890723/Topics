import wx
import wx.grid
import cv2 as cv
import result_gui
case_number = "100783334"
detection_type = "pancreas"

class FinalReport ( wx.Frame ):

	def __init__( self, parent ):
		result_gui.init(self, parent)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
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


		bSizer38.Add( bSizer211, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 20 )

		#--- left ---#

        #--- right ---#
		bSizer53 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = TransparentText( self, wx.ID_ANY, label="總評分表")
		self.m_staticText19.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ))
		self.m_staticText19.Wrap( -1 )

		bSizer53.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.TOP, 40 )

		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )

		# 当前表格的显示数据
		self.report_list = []
		# 当前表格显示的总条数
		self.page_count = 10
		# 当前显示从第几条开始
		self.page_index = 0

		self.row_label_list = ['AI\n胰腺評分', 'AI\n積液評分', '胰腺\n分割結果評分', '積液\n分割結果評分', 'CTSI評分', '最佳路徑評分']
		self.col_label_list = ['分數', '圖表', '備註']

		self.gridTable = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,600 ), 0 )

		# Grid
		self.gridTable.CreateGrid( 6, 3 )
		index = 0
		
		#設置label 標題
		while index < len(self.row_label_list):
			self.gridTable.SetRowLabelValue(index, self.row_label_list[index])
			index += 1
		index = 0
		while index < len(self.col_label_list):
			self.gridTable.SetColLabelValue(index, self.col_label_list[index])
			index += 1
		
		#表格居中
		self.gridTable.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
		self.gridTable.EnableEditing( False )
		self.gridTable.EnableGridLines( True )
		self.gridTable.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		self.gridTable.EnableDragGridSize( False )
		self.gridTable.SetMargins( 0, 0 )
		self.gridTable.SetCellSize(0, 2, 2, 1)
		self.gridTable.SetCellSize(2, 2, 2, 1)    #(x,y,合併幾列,合併幾行)

		# Columns
		self.gridTable.SetColSize( 0, 300)
		self.gridTable.SetColSize( 1, 180 )
		self.gridTable.SetColSize( 2, 344 )
		self.gridTable.EnableDragColMove( False )
		self.gridTable.EnableDragColSize( True )
		self.gridTable.SetColLabelSize( 30 )
		self.gridTable.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridTable.SetRowSize( 0, 95 )
		self.gridTable.SetRowSize( 1, 95 )
		self.gridTable.SetRowSize( 2, 95 )
		self.gridTable.SetRowSize( 3, 95 )
		self.gridTable.SetRowSize( 4, 95 )
		self.gridTable.SetRowSize( 5, 95 )
		self.gridTable.EnableDragRowSize( True )
		self.gridTable.SetRowLabelSize( 80 )
		self.gridTable.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		# 更新表格的数据
		self.get_report_list(self.page_index, self.page_count)
		# 页面的变化
		#self.Bind(wx.EVT_PAINT, self.on_resize, self)
		# 鼠标单击表格单元格的事件绑定
		self.gridTable.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.left_click_function)
		bSizer54.Add( self.gridTable, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer53.Add( bSizer54, 0, wx.ALL|wx.EXPAND, 15 )


		bSizer38.Add( bSizer53, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer38 )
		self.Layout()

		self.SetTitle('3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統 - 總評分表')
		self.Centre( wx.BOTH )

		pic_reg_path = '.\\button_bmp\\PNG\\recognize_left.png'
		size_recognize = self.m_panel3.GetSize()
		self.m_panel2.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_reg_path, W =size_recognize[0] ,H =size_recognize[1]+10: self.OnEraseBack_pic(evt,path,W,H))
		pic_deal_path = '.\\button_bmp\\PNG\\deal_left.png'
		size_deal = self.m_panel3.GetSize()
		self.m_panel3.Bind(wx.EVT_ERASE_BACKGROUND, lambda evt, path=pic_deal_path, W =size_deal[0] ,H =size_deal[1]: self.OnEraseBack_pic(evt,path,W,H))
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
'''
class FinalReport(wx.Frame):
    def __init__(self, parent):
        result_gui.init(self, parent)
        # 当前表格的显示数据
        self.report_list = []
        # 当前表格显示的总条数
        self.page_count = 10
        # 当前显示从第几条开始
        self.page_index = 0
        # 面板的大小
        self.panel_size = None
        # 选中查看详情
        detail_box = wx.BoxSizer(wx.HORIZONTAL)
        #detail_button = wx.Button(self, label="查看详情")
        #detail_box.Add(detail_button, 0, wx.LEFT, 10)
        # 表格的表头数据
        self.row_label_list = ['AI評分', '胰腺\n分割結果評分', 'CTSI評分', '最佳路徑評分', "階段"]
        self.col_label_list = ['分數', '圖表', '備註']
        # 创建表格（大小）
        self.gridTable = wx.grid.Grid(self, -1)
        # 设置行列数
        self.gridTable.CreateGrid(1, len(self.col_label_list))
        # 设置单元格最小的和高度
        self.gridTable.SetColSizes(wx.grid.GridSizesInfo(117, []))
        self.gridTable.SetRowSizes(wx.grid.GridSizesInfo(50, []))
        # 将第0列设置为选中框（该框将按照存入的值来判断，0是未选中，1是选中）
        #self.gridTable.SetColFormatBool(0)
        index = 0
        while index < len(self.row_label_list):
            self.gridTable.SetRowLabelValue(index, self.row_label_list[index])
            index += 1
        index = 0
        while index < len(self.col_label_list):
            self.gridTable.SetColLabelValue(index, self.col_label_list[index])
            index += 1
        # 设置标签居中显示
        #self.gridTable.SetCornerLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        # 设置表格内容居中显示
        self.gridTable.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        # 设置表格为不可编辑
        self.gridTable.EnableEditing(False)
        #grid_box = wx.BoxSizer(wx.VERTICAL)
        #grid_box.Add(self.gridTable, 1, wx.ALL | wx.EXPAND, 5)
        # 翻页的布局
        #pagination_box = wx.BoxSizer(wx.HORIZONTAL)
        #pre_button = wx.Button(self, label="上一页")
        #pre_button.Bind(wx.EVT_BUTTON, self.get_pre_page_date)
        #next_button = wx.Button(self, label="下一页")
        #next_button.Bind(wx.EVT_BUTTON, self.get_next_page_date)
        #des_text = wx.StaticText(self, label="显示结果的项数：")
        #self.current_page_text = wx.StaticText(self, label="当前显示为第1页     ")
        #count_list = ['10', '25', '50', '100']
        #self.page_count_select = wx.ComboBox(self, choices=count_list, value=count_list[0])
        #self.page_count_select.Bind(wx.EVT_COMBOBOX, self.change_page_count)
        #pagination_box.AddMany(
        #    [(self.current_page_text, 0, wx.TOP, 3), (des_text, 0, wx.TOP, 3), (self.page_count_select, 0, wx.LEFT, 10),
        #     (pre_button, 0, wx.LEFT, 10), (next_button, 0, wx.LEFT, 10)])
        # 整体布局
        #main_fgs = wx.FlexGridSizer(rows=3, cols=1, vgap=10, hgap=10)
        #main_fgs.AddMany(
        #    [(detail_box, 0, wx.ALL, 10), (grid_box, 1, wx.ALL, 10), (pagination_box, 0, wx.ALL | wx.ALIGN_RIGHT, 20)])
        #main_fgs.AddGrowableRow(1)
        #main_fgs.AddGrowableCol(0)
        #self.SetSizer(main_fgs)
        # 更新表格的数据
        self.get_report_list(self.page_index, self.page_count)
        # 页面的变化
        self.Bind(wx.EVT_PAINT, self.on_resize, self)
        # 鼠标单击表格单元格的事件绑定
        self.gridTable.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.left_click_function)
        self.SetSize((1050, 300))
        self.SetTitle('3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統 - 總評分表')
        self.Centre(True)
        self.Show(True)

    # 窗口size变化的监听
    def on_resize(self, event):
        self.panel_size = list(self.GetSize())
        # 设置表格的大小
        if self.panel_size[1] > len(self.report_list) * 50 + 50:
            # 设置列的宽度:面板大小减去第一列的固定长度/一共的列数
            grid_column_size = (self.panel_size[0] - 120) // len(self.col_label_list)
            grid_height = len(self.report_list) * 50 + 50
        else:
            # 行数超过面板的的大小需要上下滚动，列宽需要设置小一点
            grid_column_size = (self.panel_size[0] - 135) // len(self.col_label_list)
            grid_height = self.panel_size[1] - 120
        self.gridTable.SetColSizes(wx.grid.GridSizesInfo(grid_column_size, []))
        self.gridTable.SetSize((self.panel_size[0] - 30, grid_height))
        event.Skip()

    def left_click_function(self, event):
        # 表格当前点击的行和列
        click_col_index = event.GetCol()
        click_row_index = event.GetRow()
        if click_col_index == 1:
            # 点击表格的选择时的处理事件，模拟表格中的按钮
            if click_row_index == 0:
                img = cv.imread("../../Data/"+case_number+"/F1Score/F1_Score.jpg")
                cv.imshow('AI Result', img)
            elif click_row_index == 1:
                img = cv.imread("../../Data/"+case_number+"/"+detection_type+"/"+detection_type+"_seg/"+"segementation_chart.png")
                cv.imshow('Seg Result', img)
            elif click_row_index == 2:
                img = cv.imread("../../Data/"+case_number+"/CTSI/CTSI_chart.png")
                cv.imshow('CTSI Score', img)
            elif click_row_index == 3:
                img = cv.imread("../../Data/"+case_number+"/path/score/path_img.png")
                cv.imshow('Path Score', img)


        #elif click_col_index == 0:
        #    self._handle_click_check_box(click_row_index)
            # 点击第0列的选中的操作

    def _handle_click_check_box(self, click_row_index):
        if int(self.gridTable.GetCellValue(click_row_index, 0)):
            self.gridTable.SetCellValue(click_row_index, 0, '0')
        else:
            self.gridTable.SetCellValue(click_row_index, 0, '1')

    def get_report_list(self, start_index, show_count):
        # 清空表格數據重新顯示
        self.gridTable.ClearGrid()
        # 獲取表格的行数
        grid_row_number = self.gridTable.GetNumberRows() - 1
        # 清除表格的行
        self.gridTable.DeleteRows(0, grid_row_number)
        # 設置表格的最大大小
        self.gridTable.SetMaxSize((1200, (grid_row_number + 2) * 50))
        # 數據(暫時寫mock數據)
        data = []
        f1 = open("../../Data/"+case_number+"/F1Score/f1out.txt","r")
        data.append(f1.read())
        f1.close()
        seg = open("../../Data/"+case_number+"/"+detection_type+"/"+detection_type+"_seg/Output_chart.txt")
        data.append(seg.read())
        seg.close()
        ctsi = open("../../Data/"+case_number+"/CTSI/Output_chart.txt")
        data.append(ctsi.read())
        ctsi.close()
        path = open("../../Data/"+case_number+"/path/score/score.txt","r")
        data.append(path.read())
        path.close()
        
        
        self.report_list = [{"score": data[0], "graph": "點擊查看", "notes": "F1 Score越接近1,代表AI辨識越準確"},
                            {"score": data[1], "graph": "點擊查看", "notes": "DICE:預測值重和關係。該值越接近1，表示重和度越高\nVOE:體積誤差。越接近0，表示分割結果越準確\nRVD:相對體積誤差。越接近0，表示分割效果越好"},
                            {"score": data[2], "graph": "點擊查看", "notes": "CTSI值高表示病情嚴重，反之亦然"},
                            {"score": data[3], "graph": "點擊查看", "notes": "長度:規畫路徑長度\n通過率:路徑上無障礙物的比例"}]
        self.gridTable.AppendRows(len(self.report_list) - 1)
        for row in range(0, len(self.report_list)):
            for column in range(0, len(self.col_label_list)):
                report_list_item = self.report_list[row]
                # 處理從數據庫獲取的數據
                report_grid_dict = {
                    '0': report_list_item["score"],
                    '1': report_list_item["graph"],
                    '2': report_list_item["notes"]
                }
                # 將數據插入到第row行第column列
                self.gridTable.SetCellValue(row, column, str(report_grid_dict[str(column)]))
                # 根據结果修改表格的顯示颜色
                if report_list_item["notes"] == "最佳路徑評分":
                    self.gridTable.SetCellTextColour(row, 5, wx.Colour('#237804'))
                else:
                    self.gridTable.SetCellTextColour(row, 5, wx.Colour('#f5222d'))
                self.gridTable.SetCellTextColour(row, 6, wx.Colour('#2395f1'))
                self.gridTable.SetCellFont(row, 6, wx.Font(10, wx.FONTFAMILY_DEFAULT,
                                                           wx.FONTSTYLE_NORMAL,
                                                           wx.FONTWEIGHT_NORMAL, True))
                self.gridTable.SetCellValue(row, column, str(report_grid_dict[str(column)]))

    #def change_page_count(self, e):
    #    self.page_count = int(self.page_count_select.GetStringSelection())
    #    self.get_report_list(self.page_index, self.page_count)

    """def get_pre_page_date(self, e):
        点击上一页
        if self.page_index == 0:
            return
        self.page_index -= self.page_count
        self.get_report_list(self.page_index, self.page_count)
        self.current_page_text.SetLabel("当前显示为第" + str(self.page_index // self.page_count + 1) + "页   ")

    def get_next_page_date(self, e):
        点击下一页
        if self.page_count > len(self.report_list):
            return
        self.page_index += self.page_count
        self.get_report_list(self.page_index, self.page_count)
        self.current_page_text.SetLabel("当前显示为第" + str(self.page_index // self.page_count + 1) + "页   ")
    """


#if __name__ == '__main__':
#    app = wx.App(0)
#    frame = FinalReport(None)
#    app.MainLoop()
'''
