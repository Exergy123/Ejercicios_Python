__author__ = 'Daniel'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()


    def InitUI(self):

        wx.StaticText(self, label='x:', pos=(10,10))
        wx.StaticText(self, label='y:', pos=(10,30))

        self.st1 = wx.StaticText(self, label='', pos=(30, 10))
        self.st2 = wx.StaticText(self, label='', pos=(30, 30))

        self.Bind(wx.EVT_MOVE, self.OnMove)

        self.SetSize((250, 180))
        self.SetTitle('Move event')
        self.Centre()
        self.Show(True)

    def OnMove(self, e):

        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()