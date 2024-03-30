from typing_extensions import Final
import wx
from wx.core import RED
import wx.xrc
import os
import result_gui as gui
import ctsi_gui
import bnd_gui
import APP1
import test
import sys
import time
import final_r
import cv2 as cv
from os import mkdir
import shutil
import xml.etree.ElementTree as ET

i = 0
case_number = "100783334"
detection_type = ""
jpg_file = ""
Nowpath = os.getcwd()
app_logo = "./logo/logo.ico"
bk_color = "#a7b1c0"

def OnClick_pancreas_menu(self, event):
    global detection_type
    global i
    i = 0
    detection_type = "pancreas"
    find_jpg_file()
    self.Close(True)
    app = wx.App()
    frm = Bnd_Frame(None)
    frm.Show()
    app.MainLoop()
def OnClick_effusion_menu(self, event):
    global detection_type
    global i
    i = 0
    detection_type = "effusion"
    find_jpg_file()
    self.Close(True)
    app = wx.App()
    frm = Bnd_Frame(None)
    frm.Show()
    app.MainLoop()
def find_jpg_file():
    global jpg_file
    path = os.getcwd() + "/../../Data/" + case_number + "/" + detection_type
    for fn in os.listdir(path):
            if fn.endswith("_jpg"):
                jpg_file = fn
def OnClick_pancreas_compara_menu(self, event):
    global detection_type
    global i
    i = 0
    detection_type = "pancreas"
    find_jpg_file()
    self.Close(True)
    app = wx.App()
    frm = MyFrame(None)
    frm.Show()
    app.MainLoop()
def OnClick_effusion_compara_menu(self, event):
    global detection_type
    global i
    i = 0
    detection_type = "effusion"
    find_jpg_file()
    self.Close(True)
    app = wx.App()
    frm = MyFrame(None)
    frm.Show()
    app.MainLoop()
def OnClick_cut_pancreas_menu(self, event):
    global detection_type
    detection_type = "pancreas"
    find_jpg_file()
    self.Close(True)
    app = wx.App()
    frm = Segmentation_Analysis(None)
    frm.Show()
    app.MainLoop()
def OnClick_cut_effusion_menu(self, event):
    global detection_type
    detection_type = "effusion"
    find_jpg_file()
    self.Close(True)
    app = wx.App()
    frm = Segmentation_Analysis(None)
    frm.Show()
    app.MainLoop()
def CTSI_Score_menu(self, event):
    global i
    i = 0
    self.Close(True)
    app = wx.App()
    frm = CTSI_Analysis(None)
    frm.Show()
    app.MainLoop()
def Start_menu(self, event):
    sys.path.append("../3D")
    import test_main
    test_main.test_main(0,case_number)
def FReport_menu(self, event):
    self.Close(True)
    app = wx.App()
    frm = FinalReport(None)
    frm.Show()
    app.MainLoop()
def Home_menu(self, event):
    self.Close(True)
    app = wx.App()
    frm = StartFrame(None)
    frm.Show()
    app.MainLoop()
def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result
def creat_xml(anchor,num,case_number):
    """
    新建xml文件
    :param xml_file: second_check bounding box 4座標
    """
    root = ET.Element("annotation")
    child1 = ET.SubElement(root, "casenumber")
    child1.text = case_number
    object = ET.SubElement(root, "object")
    namen = ET.SubElement(object, "name")
    namen.text = 'pancreas'
    bndbox = ET.SubElement(object, "bndbox")
    xminn = ET.SubElement(bndbox, "xmin")
    xminn.text = str(anchor[0][0])
    yminn = ET.SubElement(bndbox, "ymin")
    yminn.text = str(anchor[0][1])
    xmaxn = ET.SubElement(bndbox, "xmax")
    xmaxn.text = str(anchor[0][2])
    ymaxn = ET.SubElement(bndbox, "ymax")
    ymaxn.text = str(anchor[0][3])
    tree = ET.ElementTree(root)
    path = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml'
    img_name = str(num).split(".")[0]
    writepath = '../../Data/'+ case_number + '/' + detection_type +'/' + detection_type + '_xml/' + img_name +'.xml'
    if detection_type == "effusion":
        path.replace("pancreas_xml","effusion_xml")
        writepath.replace("pancreas_xml","effusion_xml")
    if not os.path.exists(path):
        os.makedirs(path)
    
    tree.write(writepath,  encoding='utf-8')
    if len(anchor) >1:
        for i in range(len(anchor)-1,0,-1):
            edit_xml(anchor[len(anchor)-i],img_name)

def edit_xml(anchor,img_name):
    """
    修改xml文件
    :param xml_file:xml文件的路径
    :return:
    """
    #print(second_check[0])
    #print('../../Data/'+ case_number + "/" + detection_type +'/pancreas_xml/' + second_check[0] +'.xml')
    treepath = '../../Data/'+ case_number + '/' + detection_type +'/' + detection_type + '_xml/' + img_name +'.xml'
    if detection_type == "effusion":
        treepath.replace("pancreas_xml","effusion_xml")
    tree = ET.parse(treepath)
    root = tree.getroot()
    objs = ET.Element("object")
    root.append(objs)
    bndbox = ET.SubElement(objs, "bndbox")
    #print('error1')
    xminn = ET.SubElement(bndbox, "xmin")
    xminn.text = str(anchor[0])
    #print('error2')
    yminn = ET.SubElement(bndbox, "ymin")
    yminn.text = str(anchor[1])
    #print('error3')
    xmaxn = ET.SubElement(bndbox, "xmax")
    xmaxn.text = str(anchor[2])
    #print('error4')
    ymaxn = ET.SubElement(bndbox, "ymax")
    ymaxn.text = str(anchor[3])
    #print('error5')    
    tree.write(treepath,method='xml',encoding='utf-8')
def enhence_show(anchors,img_name):
    JPG='../../Data/'+ case_number + "/" + detection_type +'/testmodel/' + case_number + "/" + img_name
    only_number = img_name.split('-00')[2].split('.')[0]
    img = cv.imread(JPG)
    for anchor in anchors:
        cv.rectangle(img,(anchor[0],anchor[1]),(anchor[2],anchor[3]),(0,0,255),thickness=2)
    PATH = '../../Data/'+ case_number + "/" + detection_type +'/pancreas_bnd/'
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    cv.imwrite(PATH + img_name, img)


class First_Fram (gui.First_Fram):
    def __init__(self, parent):
        gui.First_Fram.__init__( self, parent)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
    def OnEraseBack( self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("./logo/first_bkg4.png")
        bitmap = scale_bitmap(bmp, 500, 350)
        dc.DrawBitmap(bitmap, 0, 0)

    def Onclick_StartFrame( self, parent ):
        self.Close(True)
        frm = StartFrame(None)
        frm.Show()
        app.MainLoop()


class StartFrame (gui.StartFrame):

    def __init__(self, parent):
        gui.StartFrame.__init__( self, parent)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
    def Onclick_Item(self, event):
        col_index = self.list.GetFirstSelected()
        msg = self.list.GetItem(col_index, col=0)
        #print(msg.GetText())
        msg_text = msg.GetText()
        self.Item_choose.SetLabel(msg_text)
        self.Item_choose.SetForegroundColour('black')
    def Onclick_Result( self, event ):
        msg = self.Item_choose.GetLabelText()
        global case_number
        case_number = msg
        # 判斷路徑是否存在
        file_path = "../../Data"
        files = os.listdir(file_path)
        for file in files:
            if file == case_number:
            # 判斷路徑是否存在
                file_result_path = file_path + "/" +case_number + "/path"
                result_files = os.listdir(file_result_path)
                check_f = 0
                for f in result_files:
                    if f == "3_line_dcm":                        
                        check_f = 1
                        self.Close(True)
                        frm = Result_Frame(None)
                        frm.Show()
                        app.MainLoop()
                if check_f == 0:
                    msg_hint = "此案例尚未分析"
                    self.Item_choose.SetLabel(msg_hint)
                    self.Item_choose.SetForegroundColour('red')
                     
    def Onclick_run_code( self, event ):
        msg = self.Item_choose.GetLabelText()
        global case_number
        case_number = msg
        # 判斷路徑是否存在
        file_path = "../../Data"
        files = os.listdir(file_path)
        for file in files:
            if file == case_number:
            # 判斷路徑是否存在
                self.Close(True)
                frm = WaitFrame(None)
                frm.Show()
                app.MainLoop()
    def Onclick_import_file( self, event):    
        target_paths = '../../Data/'
        check_dlg_dcm = 0

        dlg_dcm = wx.DirDialog(
            self, message="Choose the DICOM file",
            style=wx.DD_DEFAULT_STYLE  |
                    wx.DD_DIR_MUST_EXIST 
            )

        if dlg_dcm.ShowModal() == wx.ID_OK:
            check_dlg_dcm = 1
            paths_dcm = dlg_dcm.GetPath()
            list_case_number = paths_dcm.split('\\')
            str_case_number = list_case_number[len(list_case_number)-1]
            
            #print('path:' + paths_dcm)
            check_file = 0
            for fn in os.listdir(target_paths):
                if fn == str_case_number:
                    check_file = 1
                    break
            target_file_paths = target_paths + str_case_number
            if check_file == 0:
                mkdir(target_file_paths)
                mkdir(target_file_paths + '\\effusion')
                mkdir(target_file_paths + '\\pancreas')
                mkdir(target_file_paths + '\\path')

            shutil.move(paths_dcm, target_file_paths)

        dlg_dcm.Destroy()

        if check_dlg_dcm == 1:
            dlg_eff = wx.DirDialog(
                self, message="Choose the Effusion jpg file",
                style=wx.DD_DEFAULT_STYLE  |
                        wx.DD_DIR_MUST_EXIST 
                )

            if dlg_eff.ShowModal() == wx.ID_OK:
                paths_eff = dlg_eff.GetPath()
                shutil.move(paths_eff, target_file_paths + '\\effusion')
            
            dlg_eff.Destroy()

            dlg_pan = wx.DirDialog(
                self, message="Choose the Pancreas jpg file",
                style=wx.DD_DEFAULT_STYLE  |
                        wx.DD_DIR_MUST_EXIST 
                )

            if dlg_pan.ShowModal() == wx.ID_OK:
                paths_pan = dlg_pan.GetPath()
                shutil.move(paths_pan, target_file_paths + '\\pancreas')
            
            dlg_pan.Destroy()

        self.Close(True)
        app = wx.App()
        frm = StartFrame(None)
        frm.Show()
        app.MainLoop()
    def OnEraseBack( self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("./logo/blue_bkg3.jpg")
        bitmap = scale_bitmap(bmp, 500, 350)
        dc.DrawBitmap(bitmap, 0, 0)


class Result_Frame( gui.Result_Frame ):
    def __init__( self, parent ):
        gui.Result_Frame.__init__ ( self, parent, case_number)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
    def OnClick_pancreas(self, event):
        OnClick_pancreas_menu(self, event)
    def OnClick_effusion(self, event):
        OnClick_effusion_menu(self, event)
    def OnClick_pancreas_compara(self, event):
        OnClick_pancreas_compara_menu(self, event)
    def OnClick_effusion_compara(self, event):
        OnClick_effusion_compara_menu(self, event)
    def OnClick_cut_pancreas(self, event):
        OnClick_cut_pancreas_menu(self, event)
    def OnClick_cut_effusion(self, event):
        OnClick_cut_effusion_menu(self, event)
    def CTSI_Score(self, event):
        CTSI_Score_menu(self, event)
    def Start_page(self, event):
        Start_menu(self, event)
    def FReport_page(self, event):
        FReport_menu(self, event)
    def Home_page(self, event):
        Home_menu(self, event)
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

class MyFrame ( ctsi_gui.MyFrame ):

    def __init__( self, parent ):
        img_num = []
        ctsi_gui.MyFrame.__init__ ( self, parent, case_number, detection_type, jpg_file)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
    def imgs(self,img_num):
        path1 = "../../Data/" + case_number+ "/" + detection_type + "/" + detection_type + "_ove/"
        for fn in os.listdir(path1):
            if fn != '@eaDir' and fn.split('.')[1] == 'jpg':
                img_num.append(fn)
        img_num.sort()
    def txt_list(self,txt_num):
        path2 = "../../Data/" + case_number+ "/" + detection_type + "/" + detection_type + "_txt/"
        for fn in os.listdir(path2):
            if fn.endswith('.txt'):
                txt_num.append(fn)
        txt_num.sort()
    def next_picture(self, event,num,txt):
        global i
        if i ==len(num)-1:
            i = -1
        image1 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + jpg_file +  "/" + str(num[i+1]))
        image2 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + detection_type + "_ove/" + str(num[i+1]))
        #更新GridBagSizer()的self.bmp2
        image1.Rescale(300,300)
        image2.Rescale(300,300)
        
        mypic1 = image1.ConvertToBitmap()
        self.bitmap_no.SetBitmap(wx.BitmapFromImage(mypic1))
        mypic2 = image2.ConvertToBitmap()
        self.bitmap_yes.SetBitmap(wx.BitmapFromImage(mypic2))
        
        self.ctsi_list_Box.Clear()
        paths = '../../Data/' + case_number + '/' + detection_type + '/' + detection_type + '_txt/' + str(txt[i+1])
        fopen =  open(paths, 'r', encoding="ANSI")
        for line in fopen.readlines():
            self.ctsi_list_Box.Append(line)
        i = i + 1
    def last_picture(self, event,num,txt):
        global i
        if i ==0:
            i = len(num)
        image1 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + jpg_file +  "/" + str(num[i-1]))
        image2 = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + detection_type + "_ove/" + str(num[i-1]))
        #更新GridBagSizer()的self.bmp2
        image1.Rescale(300,300)
        image2.Rescale(300,300)
        
        mypic1 = image1.ConvertToBitmap()
        self.bitmap_no.SetBitmap(wx.BitmapFromImage(mypic1))
        mypic2 = image2.ConvertToBitmap()
        self.bitmap_yes.SetBitmap(wx.BitmapFromImage(mypic2))
        #def Onclick_back( self, event ):
        #	self.Close(True)
        #	frm = Bounding_Box_Show_Frame(None)
        #	frm.Show()
        #	app.MainLoop()
        self.ctsi_list_Box.Clear()
        paths = '../../Data/' + case_number + '/' + detection_type + '/' + detection_type + '_txt/' + str(txt[i-1])
        fopen =  open(paths, 'r', encoding="ANSI")
        for line in fopen.readlines():
            self.ctsi_list_Box.Append(line)
        i = i - 1
    def OnClick_pancreas(self, event):
        OnClick_pancreas_menu(self, event)
    def OnClick_effusion(self, event):
        OnClick_effusion_menu(self, event)
    def OnClick_pancreas_compara(self, event):
        OnClick_pancreas_compara_menu(self, event)
    def OnClick_effusion_compara(self, event):
        OnClick_effusion_compara_menu(self, event)
    def OnClick_cut_pancreas(self, event):
        OnClick_cut_pancreas_menu(self, event)
    def OnClick_cut_effusion(self, event):
        OnClick_cut_effusion_menu(self, event)
    def CTSI_Score(self, event):
        CTSI_Score_menu(self, event)
    def Start_page(self, event):
        Start_menu(self, event)
    def FReport_page(self, event):
        FReport_menu(self, event)
    def Home_page(self, event):
        Home_menu(self, event)
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
    def __del__( self ):
        pass

minx=0
miny=0
maxx=100
maxy=100

class Bnd_editFrame ( bnd_gui.Bnd_edit ):
    def __init__( self, parent ):
        bnd_gui.Bnd_edit.__init__ ( self, parent, case_number, detection_type)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
    def imgs(self,img_num):
        path = "../../Data/" + case_number + "/" + detection_type + "/" + detection_type +"_bnd/"
        for fn in os.listdir(path):
            if fn != '@eaDir' and fn.split('.')[1] == 'jpg':
                img_num.append(fn)
        img_num.sort()
    def next_picture(self, event,num):
        self.staticText_case_img_num.SetBackgroundColour(bk_color)
        global i
        if i ==len(num)-1:
            i = -1
        image = wx.Image("../../Data/" + case_number + "/" + detection_type + "/testmodel/" + "/" + case_number + "/" + str(num[i+1]))
        self.staticText_case_img_num.SetLabel("案例號碼:"+case_number+"  圖片代號:"+ num[i+1])
        #更新GridBagSizer()的self.bmp2
        i = i + 1
        mypic = image.ConvertToBitmap()
        self.bitmap_middle.SetBitmap(wx.BitmapFromImage(mypic))
    def last_picture(self, event,num):
        self.staticText_case_img_num.SetBackgroundColour(bk_color)
        global i
        if i ==0:
            i = len(num)
        image = wx.Image("../../Data/" + case_number + "/" + detection_type + "/testmodel/" + "/" + case_number + "/" + str(num[i-1]))
        self.staticText_case_img_num.SetLabel("案例號碼:"+case_number+"  圖片代號:"+ num[i-1])
        #更新GridBagSizer()的self.bmp2
        i = i - 1
        mypic = image.ConvertToBitmap()
        self.bitmap_middle.SetBitmap(wx.BitmapFromImage(mypic))
    def Onsavebtn(self, event, num, anchor):
        global i
        global case_number
        if len(anchor)>0:
            creat_xml(anchor,num[i],case_number)
            enhence_show(anchor,num[i])
        self.Close(True)
        app = wx.App()
        frm = Bnd_Frame(None)
        frm.Show()
        app.MainLoop()
    
    def OnClick_pancreas(self, event):
        OnClick_pancreas_menu(self, event)
    def OnClick_effusion(self, event):
        OnClick_effusion_menu(self, event)
    def OnClick_pancreas_compara(self, event):
        OnClick_pancreas_compara_menu(self, event)
    def OnClick_effusion_compara(self, event):
        OnClick_effusion_compara_menu(self, event)
    def OnClick_cut_pancreas(self, event):
        OnClick_cut_pancreas_menu(self, event)
    def OnClick_cut_effusion(self, event):
        OnClick_cut_effusion_menu(self, event)
    def CTSI_Score(self, event):
        CTSI_Score_menu(self, event)
    def Start_page(self, event):
        Start_menu(self, event)
    def FReport_page(self, event):
        FReport_menu(self, event)
    def Home_page(self, event):
        Home_menu(self, event)
    def OnClick_show_bnd(self, event):
        self.staticText_case_img_num.SetBackgroundColour(bk_color)
        global i
        selName = self.ctsi_list_Box.GetStringSelection()
        selName = selName.replace("xml", "jpg")
        image = wx.Image("../../Data/" + case_number + "/" + detection_type  + "/testmodel/" + "/" + case_number + "/" + selName)
        self.staticText_case_img_num.SetLabel("案例號碼:"+case_number+"  圖片代號:"+ selName)
        #更新GridBagSizer()的self.bmp2
        mypic = image.ConvertToBitmap()
        self.bitmap_middle.SetBitmap(wx.BitmapFromImage(mypic))
        i = int(selName.split("-00")[2].split(".jpg")[0])-1
    def OnPaint(self, event,anchor_position):#畫修改框
        dc = wx.ClientDC(self.bitmap_middle) 
        brush = wx.Brush("white")
        dc.SetBackground(brush)  
        #dc.Clear()
        
        pen = wx.Pen(wx.Colour(255,0,0) ,style=wx.SOLID)
        dc.SetPen(pen)
        dc.DrawLine(minx,miny,maxx,miny)
        dc.DrawLine(maxx,miny,maxx,maxy)
        dc.DrawLine(maxx,maxy,minx,maxy)
        dc.DrawLine(minx,maxy,minx,miny)
        anchor_position.append([minx,miny,maxx,maxy])
        print(anchor_position)
    def Onminpoint(self, event):#左鍵按下事件
        global minx,miny
        pos=event.GetPosition()
        minx = pos.x
        miny = pos.y
    def Onmaxpoint(self, event,anchor):#左鍵放開事件
        pos=event.GetPosition()
        global maxx,maxy,minx,miny
        maxx = pos.x
        maxy = pos.y
        self.OnPaint( event,anchor)

class Bnd_Frame ( bnd_gui.Bnd ):

    def __init__( self, parent ):
        bnd_gui.Bnd.__init__ ( self, parent, case_number, detection_type)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
    def imgs(self,img_num):
        path = "../../Data/" + case_number + "/" + detection_type + "/" + detection_type +"_bnd/"
        for fn in os.listdir(path):
            if fn != '@eaDir' and fn.split('.')[1] == 'jpg':
                img_num.append(fn)
        img_num.sort()
    def next_picture(self, event,num):
        self.staticText_case_img_num.SetBackgroundColour(bk_color)
        
        global i
        if i ==len(num)-1:
            i = -1
        image = wx.Image('../../Data/' + case_number +'/' + detection_type + '/' + detection_type + '_bnd/' + str(num[i+1]))
        self.staticText_case_img_num.SetLabel("案例號碼:"+case_number+"  圖片代號:"+ num[i+1])
        #更新GridBagSizer()的self.bmp2
        i = i + 1
        mypic = image.ConvertToBitmap()
        self.bitmap_middle.SetBitmap(wx.BitmapFromImage(mypic))
    def last_picture(self, event,num):
        self.staticText_case_img_num.SetBackgroundColour(bk_color)
        
        global i
        if i ==0:
            i = len(num)
        image = wx.Image("../../Data/" + case_number + "/" + detection_type + "/" + detection_type +"_bnd/" + str(num[i-1]))
        self.staticText_case_img_num.SetLabel("案例號碼:"+case_number+"  圖片代號:"+ num[i-1])
        #更新GridBagSizer()的self.bmp2
        i = i - 1
        mypic = image.ConvertToBitmap()
        self.bitmap_middle.SetBitmap(wx.BitmapFromImage(mypic))
    def Oneditbtn(self, event, num):
        import editimg
        editimg.edit_main(num,case_number,detection_type,i)
    def OnClick_pancreas(self, event):
        OnClick_pancreas_menu(self, event)
    def OnClick_effusion(self, event):
        OnClick_effusion_menu(self, event)
    def OnClick_pancreas_compara(self, event):
        OnClick_pancreas_compara_menu(self, event)
    def OnClick_effusion_compara(self, event):
        OnClick_effusion_compara_menu(self, event)
    def OnClick_cut_pancreas(self, event):
        OnClick_cut_pancreas_menu(self, event)
    def OnClick_cut_effusion(self, event):
        OnClick_cut_effusion_menu(self, event)
    def CTSI_Score(self, event):
        CTSI_Score_menu(self, event)
    def Start_page(self, event):
        Start_menu(self, event)
    def FReport_page(self, event):
        FReport_menu(self, event)
    def Home_page(self, event):
        Home_menu(self, event)
    def OnClick_show_bnd(self, event):
        self.staticText_case_img_num.SetBackgroundColour(bk_color)
        global i
        selName = self.ctsi_list_Box.GetStringSelection()
        selName = selName.replace("xml", "jpg")
        image = wx.Image('../../Data/' + case_number +'/' + detection_type + '/' + detection_type + '_bnd/' + selName)
        self.staticText_case_img_num.SetLabel("案例號碼:"+case_number+"  圖片代號:"+ selName)
        #更新GridBagSizer()的self.bmp2
        mypic = image.ConvertToBitmap()
        self.bitmap_middle.SetBitmap(wx.BitmapFromImage(mypic))
        i = int(selName.split("-00")[2].split(".jpg")[0])-1
        


###########################################################################
## Class Segmentation_Analysis
###########################################################################
class Segmentation_Analysis ( APP1.Segmentation_Analysis ):

    def __init__( self, parent ):
        APP1.Segmentation_Analysis.__init__ ( self, parent, case_number, detection_type)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

    def OnClick_pancreas(self, event):
        OnClick_pancreas_menu(self, event)
    def OnClick_effusion(self, event):
        OnClick_effusion_menu(self, event)
    def OnClick_pancreas_compara(self, event):
        OnClick_pancreas_compara_menu(self, event)
    def OnClick_effusion_compara(self, event):
        OnClick_effusion_compara_menu(self, event)
    def OnClick_cut_pancreas(self, event):
        OnClick_cut_pancreas_menu(self, event)
    def OnClick_cut_effusion(self, event):
        OnClick_cut_effusion_menu(self, event)
    def CTSI_Score(self, event):
        CTSI_Score_menu(self, event)
    def Start_page(self, event):
        Start_menu(self, event)
    def FReport_page(self, event):
        FReport_menu(self, event)
    def Home_page(self, event):
        Home_menu(self, event)
    def __del__( self ):
        pass

###########################################################################
## Class CTSI_Analysis
###########################################################################

class CTSI_Analysis ( APP1.CTSI_Analysis ):

    def __init__( self, parent ):
        APP1.CTSI_Analysis.__init__ ( self, parent, case_number)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
    def img_set( self, img_num, jpg_save , case_number , jpg_save_file):
        tmp_path = "../../Data/" + case_number + "/effusion"
        path_eff = tmp_path + "/effusion_ove/"
        eff_num = os.listdir(path_eff)
        for fn in eff_num:
            if fn.endswith('.jpg'):
                img_num.append(fn)

        if len(img_num) == 0:
            tmp_list = os.listdir(tmp_path)
            for fn in tmp_list:
                if fn.endswith('_jpg'):
                    jpg_save_file.append(fn)
            
            path_N_eff = tmp_path + '/' + jpg_save_file[0]
            
            eff_jpg = os.listdir(path_N_eff)
            for fn in eff_jpg:
                if fn.endswith('.jpg'):
                    jpg_save.append(fn)

    def read_txt( self, content_list, case_number):
        obj_file = "../../Data/" + case_number + "/CTSI/Effusion_count.txt"
        f =  open(obj_file,'r')
        line = f.readlines()
        for fn in line:
            content_list.append(fn)

    def Onclick_btn_next(self, event, num, jpg, j_file, content):
        self.txt_img_num.SetBackgroundColour(bk_color)
        self.txt_content_1.SetBackgroundColour(bk_color)
        self.txt_content_2.SetBackgroundColour(bk_color)
        global i
        if len(num) == 0:
            if i == len(jpg)-1:
                i = -1
            image1 = wx.Image("../../Data/" + case_number + "/effusion/" + j_file[0]  +  "/" + str(jpg[i+1]))
            self.txt_img_num.SetLabel(jpg[i+1])
            self.txt_content_1.SetLabel(content[0])
            self.txt_content_2.SetLabel(label=content[1])
            
        else:    
            if i ==len(num)-1:
                i = -1
            image1 = wx.Image("../../Data/" + case_number + "/effusion/effusion_ove" +  "/" + str(num[i+1]))
            j = (i+1)*2
            self.txt_img_num.SetLabel(num[i+1])
            self.txt_content_1.SetLabel(content[j])
            self.txt_content_2.SetLabel(content[j+1])
            
        #更新GridBagSizer()的self.bmp2
        i = i + 1
        image1.Rescale(255,255)
        mypic1 = image1.ConvertToBitmap()
        self.bitmap_no.SetBitmap(wx.BitmapFromImage(mypic1))
        
    def Onclick_btn_last(self, event, num, jpg, j_file, content):
        self.txt_img_num.SetBackgroundColour(bk_color)
        self.txt_content_1.SetBackgroundColour(bk_color)
        self.txt_content_2.SetBackgroundColour(bk_color)
        global i
        if len(num) == 0:
            if i ==0:
                i = len(jpg)
            image = wx.Image("../../Data/" + case_number + "/effusion/" + j_file[0]  +  "/" + str(jpg[i-1]))
            self.txt_img_num.SetLabel(jpg[i-1])
            self.txt_content_1.SetLabel(content[0])
            self.txt_content_2.SetLabel(content[1])
        else:
            if i ==0:
                i = len(num)
            image = wx.Image("../../Data/" + case_number + "/effusion/effusion_ove"  +  "/" + str(num[i-1]))
            j = (i-1)*2
            self.txt_img_num.SetLabel(num[i-1])
            self.txt_content_1.SetLabel(content[j])
            self.txt_content_2.SetLabel(content[j+1])
        #更新GridBagSizer()的self.bmp2
        i = i - 1
        image.Rescale(255,255)
        mypic1 = image.ConvertToBitmap()
        self.bitmap_no.SetBitmap(wx.BitmapFromImage(mypic1))

    def OnClick_pancreas(self, event):
        OnClick_pancreas_menu(self, event)
    def OnClick_effusion(self, event):
        OnClick_effusion_menu(self, event)
    def OnClick_pancreas_compara(self, event):
        OnClick_pancreas_compara_menu(self, event)
    def OnClick_effusion_compara(self, event):
        OnClick_effusion_compara_menu(self, event)
    def OnClick_cut_pancreas(self, event):
        OnClick_cut_pancreas_menu(self, event)
    def OnClick_cut_effusion(self, event):
        OnClick_cut_effusion_menu(self, event)
    def CTSI_Score(self, event):
        CTSI_Score_menu(self, event)
    def Start_page(self, event):
        Start_menu(self, event)
    def FReport_page(self, event):
        FReport_menu(self, event)
    def Home_page(self, event):
        Home_menu(self, event)

    def __del__( self ):
        
        pass



class Second_Frame ( test.Second_Frame ):

    def __init__( self, parent ):
        test.Second_Frame.__init__ ( self, parent, case_number)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

    def __del__( self ):
        pass
	
	# Virtual event handlers, overide them in your derived class
    def Onclick_processing( self, event):
        self.Close(True)
        frm = WaitFrame(None)	#放空白的Frame 
        frm.Show()
        #這裡我不確定app.MainLoop()需不需要放最後面，它的功能是讓Application的主事件循環
    #	self.Close(True)
    #	frm = run_yards(None) 	#放讀條的Frame
    #	frm.Show()
    #	app.MainLoop()
        
        #AI
        #sys.path.append(Nowpath + '\\..\\AI')
        #import AI
        #PATH_TO_DICOM_FILE= Nowpath + '\\..\\..\\Data\\'+ case_number + "\\" + detection_type + "\\testmodel\\" + case_number
        #print(PATH_TO_DICOM_FILE)
        #AI.convert2jpg(PATH_TO_DICOM_FILE)

        #AI.image_inference()

        print('Inference Done... ', end='\n')

        #Deal
        #sys.path.append(Nowpath + '\\..\\Deal')

        import Img_processing_def
        #Img_processing_def.Img_processing_def(case_number,'pancreas')
        #Img_processing_def.Img_processing_def(case_number,'effusion')

        print('Img processing Done... \n')

        #sys.path.append(Nowpath + '\\..\\Deal')
        #import CTSI_def
        #CTSI_def.CTSI_def(case_number)
        #print('CTSI Done...\n')

        #Path
        #sys.path.append(Nowpath + '\\..\\Path')

        #import straightLine
        #straightLine.straightLine(case_number)
        print('The Best Path Done... \n')
        
        app.MainLoop()

    def Onclick_result( self, event):
        self.Close(True)
        frm = Result_Frame(None)	#放空白的Frame 
        frm.Show()
        app.MainLoop()



class WaitFrame (wx.Frame):

    def __init__(self, parent):
        gui.init2(self, parent)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        WaitbSizer = wx.BoxSizer( wx.VERTICAL )

        self.Waitpanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        WaitbSizer_bg_panel = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText = wx.StaticText( self.Waitpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText.Wrap( -1 )

        WaitbSizer_bg_panel.Add( self.m_staticText, 0, wx.ALIGN_CENTER|wx.TOP, 3 )

        self.first_staticText = TransparentText( self.Waitpanel, wx.ID_ANY, label="AI辨識 . . . . . . .")
        self.first_staticText.Wrap( -1 )

        WaitbSizer_bg_panel.Add( self.first_staticText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.second_staticText = TransparentText( self.Waitpanel, wx.ID_ANY, label="影像處理 . . . . . ." )
        self.second_staticText.Wrap( -1 )

        WaitbSizer_bg_panel.Add( self.second_staticText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.third_staticText = TransparentText( self.Waitpanel, wx.ID_ANY, label="CTSI計算 . . . . ." )
        self.third_staticText.Wrap( -1 )

        WaitbSizer_bg_panel.Add( self.third_staticText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.forth_staticText = TransparentText( self.Waitpanel, wx.ID_ANY, label="最佳路徑演算 . ." )
        self.forth_staticText.Wrap( -1 )

        WaitbSizer_bg_panel.Add( self.forth_staticText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        self.Waitpanel.SetSizer( WaitbSizer_bg_panel )
        self.Waitpanel.Layout()
        WaitbSizer_bg_panel.Fit( self.Waitpanel )
        WaitbSizer.Add( self.Waitpanel, 1, wx.ALL|wx.EXPAND, 0 )




        self.gauge_count = 0
        self.panel_Gauge = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gauge_Sizer = wx.BoxSizer( wx.VERTICAL )

        self.gauge = wx.Gauge(self.panel_Gauge, range = 20, size = (250, 25), style =  wx.GA_HORIZONTAL) 
        gauge_Sizer.Add( self.gauge, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.panel_Gauge.SetSizer( gauge_Sizer )
        self.panel_Gauge.Layout()
        gauge_Sizer.Fit( self.panel_Gauge )
        WaitbSizer.Add( self.panel_Gauge, 1, wx.ALL|wx.EXPAND, 0 )




        self.panel_button = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        AI_pic = wx.Image('.\\button_bmp\\PNG\\AI.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        bmp_AI = scale_bitmap(AI_pic, 85, 35)
        self.AI_button = wx.BitmapButton( self.panel_button, wx.ID_ANY, bmp_AI, wx.DefaultPosition, wx.Size( 85,35 ), 0 )
        bSizer17.Add( self.AI_button, 0, wx.ALIGN_CENTER|wx.ALL, 18 )

        img_deal_pic = wx.Image('.\\button_bmp\\PNG\\img_deal.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        bmp_img_deal = scale_bitmap(img_deal_pic, 85, 35)
        self.imgp_button = wx.BitmapButton( self.panel_button, wx.ID_ANY, bmp_img_deal, wx.DefaultPosition, wx.Size( 85,35 ), 0 )
        bSizer17.Add( self.imgp_button, 0, wx.ALIGN_CENTER|wx.ALL, 18 )

        CTSI_pic = wx.Image('.\\button_bmp\\PNG\\CTSI.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        bmp_CTSI = scale_bitmap(CTSI_pic, 85, 38)
        self.CTSI_button = wx.BitmapButton( self.panel_button, wx.ID_ANY, bmp_CTSI, wx.DefaultPosition, wx.Size( 85,35 ), 0 )
        bSizer17.Add( self.CTSI_button, 0, wx.ALIGN_CENTER|wx.ALL, 18 )

        BP_pic = wx.Image('.\\button_bmp\\PNG\\best_paths.png',wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        bmp_BP = scale_bitmap(BP_pic, 85, 35)
        self.BP_button = wx.BitmapButton( self.panel_button, wx.ID_ANY, bmp_BP, wx.DefaultPosition, wx.Size( 85,35 ), 0 )
        bSizer17.Add( self.BP_button, 0, wx.ALIGN_CENTER|wx.ALL, 18 )
        '''
        self.AI_button = wx.Button( self.panel_button, wx.ID_ANY, u"AI", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.AI_button, 0, wx.ALIGN_CENTER|wx.ALL, 22 )
        
        self.imgp_button = wx.Button( self.panel_button, wx.ID_ANY, u"影像分析", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.imgp_button, 0, wx.ALIGN_CENTER|wx.ALL, 22 )

        self.CTSI_button = wx.Button( self.panel_button, wx.ID_ANY, u"CTSI", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.CTSI_button, 0, wx.ALIGN_CENTER|wx.ALL, 22 )

        self.BP_button = wx.Button( self.panel_button, wx.ID_ANY, u"最佳路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.BP_button, 0, wx.ALIGN_CENTER|wx.ALL, 22 )
        '''        
        self.panel_button.SetSizer( bSizer17 )
        self.panel_button.Layout()
        bSizer17.Fit( self.panel_button )
        WaitbSizer.Add( self.panel_button, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( WaitbSizer )
        self.Layout()

        self.Centre( wx.BOTH )

        
        #self.m_gauge4 = wx.Gauge(self.m_panel2, wx.ID_ANY, 1000,
        #                         (1000, 1000), wx.Size(1800, 20), wx.GA_HORIZONTAL)
        #if self.count >= 0:
        #    self.count = self.count + 1
        #    if self.count >= 50:
        #        self.count = 0

        # self.m_gauge4.SetValue(self.count)
        #self.m_gauge4.Pulse()
        #bSizer31.Add(self.m_gauge4, 0, wx.ALL, 5)

        self.Centre(wx.BOTH)
        
        self.AI_button.Bind( wx.EVT_BUTTON, self.Onclick_ai )
        self.imgp_button.Bind( wx.EVT_BUTTON, self.Onclick_imgp )
        self.CTSI_button.Bind( wx.EVT_BUTTON, self.Onclick_ctsi )
        self.BP_button.Bind( wx.EVT_BUTTON, self.Onclick_bp )
        self.Waitpanel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.panel_Gauge.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.panel_button.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
       
    def OnEraseBack( self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("./logo/blue_bkg3.jpg")
        bitmap = scale_bitmap(bmp, 500, 300)
        dc.DrawBitmap(bitmap, 0, 0)
    

    def __del__(self):
        pass
    def OnClick_pancreas(self, event):
        OnClick_pancreas_menu(self, event)
    def OnClick_effusion(self, event):
        OnClick_effusion_menu(self, event)
    def OnClick_pancreas_compara(self, event):
        OnClick_pancreas_compara_menu(self, event)
    def OnClick_effusion_compara(self, event):
        OnClick_effusion_compara_menu(self, event)
    def OnClick_cut_pancreas(self, event):
        OnClick_cut_pancreas_menu(self, event)
    def OnClick_cut_effusion(self, event):
        OnClick_cut_effusion_menu(self, event)
    def CTSI_Score(self, event):
        CTSI_Score_menu(self, event)
    def Start_page(self, event):
        Start_menu(self, event)
    def FReport_page(self, event):
        FReport_menu(self, event)
    def Home_page(self, event):
        Home_menu(self, event)
    def Onclick_ai(self, event):
        #AI
        sys.path.append(Nowpath + '\\..\\AI')
        import AI
        PATH_TO_DICOM_FILE= Nowpath + '\\..\\..\\Data\\'+ case_number + "\\" + case_number
        #print(PATH_TO_DICOM_FILE)
        
        AI.init_para(case_number,"pancreas")
        self.gauge.SetValue(0)
        AI.convert2jpg(PATH_TO_DICOM_FILE)
        self.gauge_count = self.gauge_count + 1 
        self.gauge.SetValue(self.gauge_count)
        AI.image_inference(self.gauge_count, self.gauge)
        print('Inference Done... ', end='\n')
        AI.init_para(case_number,"effusion")
        self.gauge.SetValue(0)
        AI.convert2jpg(PATH_TO_DICOM_FILE)
        self.gauge_count = self.gauge_count + 1 
        self.gauge.SetValue(self.gauge_count)
        AI.image_inference(self.gauge_count, self.gauge)
        print('Inference Done... ', end='\n')
        self.first_staticText.SetForegroundColour(RED)
        self.first_staticText.SetLabel("AI辨識完畢!")
    def Onclick_imgp(self, event):
        #Deal
        sys.path.append(Nowpath + '\\..\\Deal')

        import Img_processing_def
        
        self.gauge.SetValue(0)
        Img_processing_def.Img_processing_def(case_number,'pancreas', self.gauge_count, self.gauge)
        Img_processing_def.Img_processing_def(case_number,'effusion', self.gauge_count, self.gauge)

        #print('Img processing Done... \n')
        self.second_staticText.SetForegroundColour(RED)
        self.second_staticText.SetLabel("影像處理完畢!")
    def Onclick_ctsi(self, event):
        sys.path.append(Nowpath + '\\..\\Deal')
        import CTSI_def
        CTSI_def.CTSI_def(case_number)
        
        self.gauge.SetValue(0)
        self.gauge_count = self.gauge_count + 1 
        self.gauge.SetValue(self.gauge_count)
        #print('CTSI Done...\n')
        self.third_staticText.SetForegroundColour(RED)
        self.third_staticText.SetLabel("CTSI計算完畢!")
        
    def Onclick_bp(self, event):
        #Path
        sys.path.append(Nowpath + '\\..\\Path')

        import straightLine
        
        self.gauge.SetValue(0)
        straightLine.straightLine(case_number, self.gauge_count, self.gauge)
        #print('The Best Path Done... \n')
        self.forth_staticText.SetForegroundColour(RED)
        self.forth_staticText.SetLabel("最佳路徑演算完畢!")



class FinalReport (gui.StartFrame):

    def __init__(self, parent):
        final_r.FinalReport.__init__( self, parent)
        icon = wx.Icon(app_logo, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

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
                img = cv.imread('../../Data/'+case_number+'/F1Score/F1_Score_pancreas.jpg')
                cv.imshow('AI_pan Result', img)
            elif click_row_index == 1:
                img = cv.imread('../../Data/'+case_number+'/F1Score/F1_Score_effusion.jpg')
                cv.imshow('AI_eff Result', img)
            elif click_row_index == 2:
                img = cv.imread("../../Data/"+case_number+"/pancreas/pancreas_seg/segementation_chart.png")
                cv.imshow('Seg_pan Result', img)
            elif click_row_index == 3:
                img = cv.imread("../../Data/"+case_number+"/effusion/effusion_seg/segementation_chart.png")
                cv.imshow('Seg_eff Result', img)
            elif click_row_index == 4:
                img = cv.imread("../../Data/"+case_number+"/CTSI/CTSI_chart.png")
                cv.imshow('CTSI Score', img)
            elif click_row_index == 5:
                img = cv.imread("../../Data/"+case_number+"/path/score/path_img.png")
                cv.imshow('Path Score', img)

    '''
        #elif click_col_index == 0:
        #    self._handle_click_check_box(click_row_index)
            # 点击第0列的选中的操作

    def _handle_click_check_box(self, click_row_index):
        if int(self.gridTable.GetCellValue(click_row_index, 0)):
            self.gridTable.SetCellValue(click_row_index, 0, '0')
        else:
            self.gridTable.SetCellValue(click_row_index, 0, '1')
    '''

    def get_report_list(self, start_index, show_count):
        # 清空表格數據重新顯示
        self.gridTable.ClearGrid()
        # 獲取表格的行数
        #grid_row_number = self.gridTable.GetNumberRows() - 1
        # 清除表格的行
        #self.gridTable.DeleteRows(0, grid_row_number)
        # 設置表格的最大大小
        #self.gridTable.SetMaxSize((1200, (grid_row_number + 2) * 50))
        # 數據(暫時寫mock數據)
        data = []
        f1_pan = open("../../Data/"+case_number+"/F1Score/f1out_pancreas.txt","r")
        data.append(f1_pan.read())
        f1_pan.close()
        f1_eff = open("../../Data/"+case_number+"/F1Score/f1out_effusion.txt","r")
        data.append(f1_eff.read())
        f1_eff.close()
        seg_pan = open("../../Data/"+case_number+"/pancreas/"+"pancreas_seg/Output_chart.txt")
        data.append(seg_pan.read())
        seg_pan.close()
        seg_eff = open("../../Data/"+case_number+"/effusion/"+"effusion_seg/Output_chart.txt")
        data.append(seg_eff.read())
        seg_eff.close()
        ctsi = open("../../Data/"+case_number+"/"+"CTSI/Output_chart.txt")
        data.append(ctsi.read())
        ctsi.close()
        path = open("../../Data/"+case_number+"/path/score/score.txt","r")
        data.append(path.read())
        path.close()
        
        
        self.report_list = [{"score": data[0], "graph": "點擊查看", "notes": "F1 Score越接近1,代表AI辨識越準確"},
                            {"score": data[1], "graph": "點擊查看", "notes": ""},
                            {"score": data[2], "graph": "點擊查看", "notes": "DICE:預測值重和關係。該值越接近1，表示重和度越高。\nVOE:體積誤差。越接近0，表示分割結果越準確。\nRVD:相對體積誤差。越接近0，表示分割效果越好。"},
                            {"score": data[3], "graph": "點擊查看", "notes": ""},
                            {"score": data[4], "graph": "點擊查看", "notes": "CTSI值高表示病情嚴重，反之亦然"},
                            {"score": data[5], "graph": "點擊查看", "notes": "長度:規畫路徑長度\n通過率:路徑上無障礙物的比例"}]
        #self.gridTable.AppendRows(len(self.report_list) - 1)
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
    def OnClick_pancreas(self, event):
        OnClick_pancreas_menu(self, event)
    def OnClick_effusion(self, event):
        OnClick_effusion_menu(self, event)
    def OnClick_pancreas_compara(self, event):
        OnClick_pancreas_compara_menu(self, event)
    def OnClick_effusion_compara(self, event):
        OnClick_effusion_compara_menu(self, event)
    def OnClick_cut_pancreas(self, event):
        OnClick_cut_pancreas_menu(self, event)
    def OnClick_cut_effusion(self, event):
        OnClick_cut_effusion_menu(self, event)
    def CTSI_Score(self, event):
        CTSI_Score_menu(self, event)
    def Start_page(self, event):
        Start_menu(self, event)
    def FReport_page(self, event):
        FReport_menu(self, event)
    def Home_page(self, event):
        Home_menu(self, event)

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

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = First_Fram(None)
    frm.Show()
    app.MainLoop()