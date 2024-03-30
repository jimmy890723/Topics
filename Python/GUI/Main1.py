# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.9.0 Sep  5 2021)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame2
###########################################################################


class Main (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(
            self, wx.ID_ANY, u"3D引流管穿刺路徑於胰腺炎治療的智慧規劃系統", wx.DefaultPosition, wx.Size(700, 300), 0)
        self.m_staticText5.Wrap(-1)

        self.m_staticText5.SetFont(wx.Font(
            24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "新細明體"))

        bSizer5.Add(self.m_staticText5, 1,
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(
            self, wx.ID_ANY, u"Please enter casenumber...", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer5.Add(self.m_staticText6, 0,
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, 30), 0)
        bSizer5.Add(self.m_textCtrl4, 0,
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)

        self.m_button4 = wx.Button(
            self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == "__main__":
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frame = Main(None)
    frame.Show()
    app.MainLoop()
