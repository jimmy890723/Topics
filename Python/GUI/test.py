# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class Second_Frame
###########################################################################


class Second_Frame (wx.Frame):

    def __init__(self, parent, case_number):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            800, 500), style= wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        Second_Frame_sizer = wx.GridSizer(0, 2, 0, 0)

        self.processing = wx.Button(
            self, wx.ID_ANY, u"跑程式", wx.DefaultPosition, wx.DefaultSize, 0)
        Second_Frame_sizer.Add(self.processing, 0, wx.ALL |
                    wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.result = wx.Button(
            self, wx.ID_ANY, u"成果", wx.DefaultPosition, wx.DefaultSize, 0)
        Second_Frame_sizer.Add(self.result, 0, wx.ALIGN_CENTER_HORIZONTAL |
                    wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SetSizer(Second_Frame_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        #connect events
        self.processing.Bind( wx.EVT_BUTTON, self.Onclick_processing )
        self.result.Bind( wx.EVT_BUTTON, self.Onclick_result )

    def __del__(self):
        pass

'''
if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MyFrame1(None)
    frm.Show()
    app.MainLoop()
'''