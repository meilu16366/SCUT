'''
Created on 2019年8月14日

截图选择按钮窗口

@author: ml
'''
import tkinter as tk
import time

class ChooseWin:
    '''初始化窗口，传入坐标'''
    def __init__(self,x,y,beforWin=None,saved=None):
        self.beforWin = beforWin
        self.saved = saved
        win = tk.Tk()
        win.geometry("135x30+%d+%d" % (x,y))
        win.attributes("-topmost",True)
        win.overrideredirect(True)
        self.win = win
        #添加按钮 ， 确认和取消
        tk.Button(self.win,text='保存',width=5,command=self.savePng).place(x=0,y=0)
        tk.Button(self.win,text='确认',width=5,command=self.enter).place(x=45,y=0)
        tk.Button(self.win,text='取消',width=5,command=self.ext).place(x=90,y=0)
    
    def ext(self,t=None):
        self.beforWin.win.destroy()
        self.beforWin.isDestroy = True
        self.win.destroy()
    def savePng(self,t=None):
        self.ext(1)
        time.sleep(1)
        self.beforWin.savePng()
    def enter(self):
        self.ext(1)
        time.sleep(2)
        self.beforWin.saveToCut()
        
if __name__ == '__main__':
    w = ChooseWin(20,20)

    w.win.mainloop()