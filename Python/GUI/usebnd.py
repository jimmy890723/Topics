from numpy.lib.function_base import delete
import wx
import result_gui
import os
case_number = "100783334"
detection_type = "pancreas"
class MainWidget(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u'ListBox Test ...', pos=wx.DefaultPosition, size=wx.Size(
        1300, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer = wx.BoxSizer( wx.VERTICAL )
		
        bnd_list = []
        xmlpath = "../../Data/"+case_number+"/"+detection_type+"/"+detection_type+"_xml"
        
        self.CTSI_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_top = wx.BoxSizer( wx.VERTICAL )

        self.ctsi_list_Box = wx.ListBox( self.CTSI_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,300 ), bnd_list, 0 )
        self.ctsi_list_Box.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

        bSizer_top.Add( self.ctsi_list_Box, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.CTSI_panel.SetSizer( bSizer_top )
        self.CTSI_panel.Layout()
        bSizer_top.Fit( self.CTSI_panel )
        bSizer.Add( self.CTSI_panel, 5, wx.EXPAND |wx.ALL, 0 )
        for fn in os.listdir(xmlpath):
            if fn != '@eaDir' and fn.split('.')[1] == 'xml':
                self.ctsi_list_Box.Append(fn)
        self.Bind(wx.EVT_LISTBOX, self.OnClick, self.ctsi_list_Box)

    def OnClick(self, event):
        selName = self.ctsi_list_Box.GetStringSelection()
        self.SetTitle(selName)



if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainWidget(None, "ListCtrl Test")
    frame.Show(True)
    app.MainLoop()