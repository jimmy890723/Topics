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
# Class MainFrame
###########################################################################


class MainFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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
        self.疊圖比較 = wx.MenuItem(self.Pancreas1, wx.ID_ANY,
                                u"疊圖比較", wx.EmptyString, wx.ITEM_NORMAL)
        self.Pancreas1.Append(self.疊圖比較)

        self.分割結果 = wx.MenuItem(self.Pancreas1, wx.ID_ANY,
                                u"分割結果", wx.EmptyString, wx.ITEM_NORMAL)
        self.Pancreas1.Append(self.分割結果)

        self.Deal.AppendSubMenu(self.Pancreas1, u"胰腺")

        self.Effusion1 = wx.Menu()
        self.疊圖比較 = wx.MenuItem(self.Effusion1, wx.ID_ANY,
                                u"疊圖比較", wx.EmptyString, wx.ITEM_NORMAL)
        self.Effusion1.Append(self.疊圖比較)

        self.分割結果 = wx.MenuItem(self.Effusion1, wx.ID_ANY,
                                u"分割結果", wx.EmptyString, wx.ITEM_NORMAL)
        self.Effusion1.Append(self.分割結果)

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

        self.m_menu5 = wx.Menu()
        self.Start = wx.MenuItem(
            self.m_menu5, wx.ID_ANY, u"回到首頁", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu5.Append(self.Start)

        self.m_menubar1.Append(self.m_menu5, u"首頁")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()
