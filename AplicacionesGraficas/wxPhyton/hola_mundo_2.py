__author__ = 'Daniel'


import wx
class Frame(wx.Frame):

    def __init__(self):
           wx.Frame.__init__(self, parent=None)
           panel = wx.Panel(self)

#Lo de arriba siempre en aplicaciones graficas

#Declaramos los elementos
           text = wx.StaticText(panel, -1, "Hola mundo")
           c1 = wx.CheckBox(panel, -1, label="Uno")
           c2 = wx.CheckBox(panel, -1, label="Dos")
           c3 = wx.CheckBox(panel, -1, label="Dos")
           t = wx.TextCtrl(panel)
           b1 = wx.Button(panel, -1,label="Aceptar")
           b2 = wx.Button(panel, -1,label="Cancelar")


#Introducimos sus propiedades
           sizer = wx.BoxSizer(wx.VERTICAL)
           sizer.Add(text, 0, wx.ALL, 0)
           sizer.Add(c1, 0, wx.ALL, 0)
           sizer.Add(c2, 0, wx.ALL, 0)
           sizer.Add(c3, 0, wx.ALL, 0)
           sizer.Add(t, 0, wx.ALL, 0)
           sizer.Add(b1, 0, wx.ALL, 0)
           sizer.Add(b2, 0, wx.ALL, 0)
           panel.SetSizer(sizer)
           panel.Layout()

#Siempre al final en aplicaciones graficas

app = wx.App(redirect=True)
Frame().Show()
app.MainLoop()
