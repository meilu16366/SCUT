'''
Created on 2019年8月14日

截图的全屏窗口

@author: ml
'''
import tkinter as tk
import services.ChooseWin as cw
import services.SCcut as sc


class CutWindow:
    
    isDestroy = False
    
    def __init__(self):
        '''初始化坐标'''
        self.clearPoint()
        win = tk.Tk()
        
        self.w = _w = win.winfo_screenwidth()
        self.h = _h = win.winfo_screenheight()
        
        win.geometry("%dx%d+%d+%d" % (_w,_h,0,0) )
        win.attributes("-topmost",True)
        win.attributes("-alpha",0.4)
        win.overrideredirect(True)
        p = tk.Canvas(win,width=_w,height=_h)
        
        p.pack()
        
        self.p = p
        win.bind('<B1-Motion>', self.drag)
        win.bind('<ButtonRelease-3>', self.ext)
        win.bind('<ButtonPress-1>', self.keyDown)
        win.bind('<ButtonRelease-1>', self.keyUp)
        self.win = win
    def ext(self,t):
        self.win.destroy()
        self.isDestroy = True
        if hasattr(self, 'cwin'):
            self.cwin.win.destroy()
    def drag(self,e):
        self.paint(self.kd.x, self.kd.y, e.x, e.y)
    def paint(self,x1, y1, x2, y2):
        self.p.delete('all')
        self.p.create_rectangle(x1, y1, x2, y2, outline='red',width=4)
    def keyDown(self,e):
        self.kd.x = e.x
        self.kd.y = e.y
    def keyUp(self,e):
        self.ku.x = e.x
        self.ku.y = e.y
        self.paint(self.kd.x,self.kd.y, e.x,e.y)
        
        if (e.x+135) > self.w or (e.y+30) > self.h:
            cwin = cw.ChooseWin(e.x-135,e.y-30,self)
        else:
            cwin = cw.ChooseWin(e.x,e.y,self)
        self.cwin = cwin
        cwin.win.mainloop()
    def clearPoint(self):
        self.kd = Point(0,0) #鼠标按下时的坐标
        self.ku = Point(1,1) #鼠标抬起时的坐标
    
    def savePng(self):
        scd = sc.SCcut()
        scd.cut((self.kd.x,self.kd.y,self.ku.x,self.ku.y))
        scd.save()
    
    def saveToCut(self):
        scd = sc.SCcut()
        scd.cut((self.kd.x,self.kd.y,self.ku.x,self.ku.y))
        scd.saveToCut()

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
if __name__ == '__main__':
    w = CutWindow()
    w.win.mainloop()
