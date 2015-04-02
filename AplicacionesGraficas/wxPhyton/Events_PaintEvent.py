__author__ = 'Daniel'
#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.count = 0
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetSize((250, 180))
        self.Centre()
        self.Show(True)

    def OnPaint(self, e):

        self.count += 1
        self.SetTitle(str(self.count))

def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()