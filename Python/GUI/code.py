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
import APP
sys.path.append("D:\\gui\\3D\\Python")
sys.path.append("D:\\gui\\3D\\Python\\AI")

###########################################################################
## Class Start_Frame
###########################################################################
case_number = 0
i = 0
class Start_Frame ( APP.Start_Frame ):

	def __init__( self, parent ):
		APP.Start_Frame.__init__ ( self, parent, case_number)


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Onclick( self, event ):
		msg = self.Start_casenumber.GetValue()
		global case_number
		case_number = msg
		self.Start_show_case.SetLabel(case_number)
		self.Close(True)
		frm = Menu_Frame(None)
		frm.Show()
		app.MainLoop()


###########################################################################
## Class Menu_Frame
###########################################################################

class Menu_Frame ( APP.Menu_Frame ):

	def __init__( self, parent ):
		APP.Menu_Frame.__init__ ( self, parent, case_number)


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Onclick_deal( self, event ):
		self.Close(True)
		frm = Deal_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_result( self, event ):
		self.Close(True)
		frm = Result_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_back( self, event ):
		self.Close(True)
		frm = Start_Frame(None)
		frm.Show()
		app.MainLoop()



###########################################################################
## Class Deal_Frame
###########################################################################

class Deal_Frame ( APP.Deal_Frame ):

    def __init__( self, parent ):
    	APP.Deal_Frame.__init__ ( self, parent, case_number)

    def __del__( self ):
    	pass


    # Virtual event handlers, overide them in your derived class
    def Onclick( self, event ):
    	event.Skip()
    def Onclick_back( self, event ):
    	self.Close(True)
    	frm = Menu_Frame(None)
    	frm.Show()
    	app.MainLoop()
    def Onclick_best_path( self, event ):
    	import straightLine
    def Onclick_Img_Processing( self, event ):
    	import Img_processing2
    def Onclick_img_identify( self, event ):
        
        import AI
        PATH_TO_DICOM_FILE='D:/gui/testmodel/' + case_number
        print(PATH_TO_DICOM_FILE)
        AI.convert2jpg(PATH_TO_DICOM_FILE)
        AI.image_inference()
        print('Inference Done... ', end='\n')



###########################################################################
## Class Result_Frame
###########################################################################

class Result_Frame ( APP.Result_Frame ):

	def __init__( self, parent ):
		APP.Result_Frame.__init__ ( self, parent, case_number)


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Onclick_3D( self, event ):
		self.Close(True)
		frm = ThreeD_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_back( self, event ):
		self.Close(True)
		frm = Menu_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_img_show( self, event ):
		self.Close(True)
		frm = Img_Show_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_casescore( self, event ):
		self.Close(True)
		frm = Cases_score_Frame(None)
		frm.Show()
		app.MainLoop()





###########################################################################
## Class Img_Show_Frame
###########################################################################

class Img_Show_Frame ( APP.Img_Show_Frame ):

	def __init__( self, parent ):
		APP.Img_Show_Frame.__init__ ( self, parent, case_number)

		

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Onclick( self, event ):
		event.Skip()
	def Onclick_back( self, event ):
		self.Close(True)
		frm = Result_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_bounding_box( self, event ):
		self.Close(True)
		frm = Bounding_Box_Show_Frame(None)
		frm.Show()
		app.MainLoop()



###########################################################################
## Class Bounding_Box_Show_Frame
###########################################################################



class Bounding_Box_Show_Frame ( APP.Bounding_Box_Show_Frame ):#有設定初始參數i img_num self.imgs(img_num)需檢查有無錯誤

    def __init__( self, parent ):
        APP.Bounding_Box_Show_Frame.__init__ ( self, parent, case_number)
        
        
    def imgs(self,img_num):
        path = "D:/gui/1003204775"
        for fn in os.listdir(path):
            if fn != '@eaDir' and fn.split('.')[1] == 'jpg':
                img_num.append(fn)
        img_num.sort()
    def next_picture(self, event,num):
        global i
        if i ==len(num)-1:
            i = -1
        image = wx.Image('D:/gui/' + str(case_number) + "/" + str(num[i+1]))
        #更新GridBagSizer()的self.bmp2
        i = i + 1
        mypic = image.ConvertToBitmap()
        self.Start_StaticBitmap.SetBitmap(wx.BitmapFromImage(mypic))
    def back_picture(self, event,num):
        global i
        if i ==0:
            i = len(num)
        image = wx.Image('D:/gui/' + str(case_number) + "/" + str(num[i-1]))
        #更新GridBagSizer()的self.bmp2
        i = i - 1
        mypic = image.ConvertToBitmap()
        self.Start_StaticBitmap.SetBitmap(wx.BitmapFromImage(mypic))
    def Onclick_back( self, event ):
        self.Close(True)
        frm = Img_Show_Frame(None)
        frm.Show()
        app.MainLoop()



###########################################################################
## Class Cases_score_Frame
###########################################################################

class Cases_score_Frame ( APP.Cases_score_Frame ):

	def __init__( self, parent ):
		APP.Cases_score_Frame.__init__ ( self, parent, case_number)


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Onclick( self, event ):
		event.Skip()
	def Onclick_back( self, event ):
		self.Close(True)
		frm = Result_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_pancreas_cut_status( self, event ):
		frm = Pancreas_cut_status_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_Check_CTSI( self, event ):
		frm = CTSI_Frame(None)
		frm.Show()
		app.MainLoop()
	def Onclick_CTSI( self, event ):
		import CTSI




###########################################################################
## Class TestListCtrl
###########################################################################
#此CLASS GUI不需要有
listctrldata = {
1 : ("使用方法，請參照下方指示進行操作!", "", "", ""),
2 : ("1.點擊下方Open按鈕", "", "", ""),
3 : ("2.開啟視窗後，右下檔案類別，選擇All files", "", "", ""),
4 : ("3.尋找要開啟的案例csv檔", "", "", ""),
5 : ("4.找到後點選，按下右下角開啟", "", "", ""),
6 : ("ps:想查看其他檔案，再次按下Open即可", "", "", ""),
}
class TestListCtrl(wx.ListCtrl,
                   listmix.ListCtrlAutoWidthMixin,
                   listmix.TextEditMixin):
    

    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.Populate(listctrldata)
        listmix.TextEditMixin.__init__(self)


    def Populate(self, listctrldata):
        # for normal, simple columns, you can add them like this:
        
        self.InsertColumn(0, "No.")
        self.InsertColumn(1, "DICE")
        self.InsertColumn(2, "VOE")
        self.InsertColumn(3, "RVD")

        items = listctrldata.items()
        for key, data in items:
            index = self.InsertItem(self.GetItemCount(), data[0])
            self.SetItem(index, 1, data[1])
            self.SetItem(index, 2, data[2])
            self.SetItem(index, 3, data[3])
            self.SetItemData(index, key)

        self.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(3, wx.LIST_AUTOSIZE)

        self.currentItem = 0


    def SetStringItem(self, index, col, data):
        if col in range(3):
            wx.ListCtrl.SetItem(self, index, col, data)
            wx.ListCtrl.SetItem(self, index, 3+col, str(len(data)))
        else:
            try:
                datalen = int(data)
            except:
                return

            wx.ListCtrl.SetItem(self, index, col, data)

            data = self.GetItem(index, col-3).GetText()
            wx.ListCtrl.SetItem(self, index, col-3, data[0:datalen])

#此CLLAS GUI不需要 但要加一個介面輸入參數

class Pancreas_cut_status_Frame(wx.Frame):
    def __init__(self, *args, **kw):
        
        wildcard = "All files (*.*)|*.*"

        super(Pancreas_cut_status_Frame, self).__init__(*args, **kw)
        
        #create a penel in the frame
        pnl = wx.Panel(self)
        lst = TestListCtrl(pnl, 10,
                                 style=wx.LC_REPORT
                                 | wx.BORDER_NONE
                                 #| wx.LC_SORT_ASCENDING            # Content of list as instructions is
                                 | wx.LC_HRULES | wx.LC_VRULES      # nonsense with auto-sort enabled
                                 )
        self.lsv = lst
        b1 = wx.Button(pnl, 11, "Open")
        
        #create sizer to manage layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lst, 10, wx.EXPAND)
        sizer.Add(b1, 11 , wx.EXPAND)
        pnl.SetSizer(sizer)

        #event
        self.Bind(wx.EVT_BUTTON,lambda evt, wildcard=wildcard: self.OnOpen(evt,wildcard), b1)

    def OnOpen(self, event, wildcard):

        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
            )

        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            path = paths[0]
            with open(path, 'r') as f:
                rows = csv.reader(f)
                global listctrldata
                listctrldata.clear()
                for idx, val in enumerate(rows):
                    tex = tuple([i for i in val])
                    listctrldata[idx] = tex
                f.close
            self.lsv.ClearAll()
            self.lsv.Populate(listctrldata)

        dlg.Destroy()




#此CLLAS GUI不需要
class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.my_text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        btn = wx.Button(self, label='Open Text File')
        btn.Bind(wx.EVT_BUTTON, self.onOpen)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.my_text, 1, wx.ALL|wx.EXPAND)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(sizer)

    def onOpen(self, event):
        wildcard = "TXT files (*.txt)|*.txt"
        dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        path = dialog.GetPath()

        if os.path.exists(path):
            with open(path) as fobj:
                self.my_text.Clear()
                for line in fobj:
                    self.my_text.WriteText(line)

#此CLLAS GUI不需要 但要加一個介面輸入參數
class CTSI_Frame(wx.Frame):

    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, None, title='Text File Reader')

        panel = MyPanel(self)

        self.Show()
		





###########################################################################
## Class ThreeD_Frame
###########################################################################

class ThreeD_Frame ( APP.ThreeD_Frame ):

	def __init__( self, parent ):
		APP.ThreeD_Frame.__init__ ( self, parent, case_number)


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Onclick( self, event ):
		msg = self.ThreeD_index.GetValue()
		import test_main
		test_main.test_main(msg)
	def Onclick_back( self, event ):
		self.Close(True)
		frm = Result_Frame(None)
		frm.Show()
		app.MainLoop()



if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = Start_Frame(None)
    frm.Show()
    app.MainLoop()


