'''
Created on 2019/8

截图接口

@author: ml
'''

from PIL import ImageGrab
import tkinter.filedialog as fl
import tkinter as tk
import win32clipboard as clip
import win32con
from io import BytesIO

class SCcut:
    
    def cut(self,args):
        
        img = ImageGrab.grab(bbox=args)
        self.img = img
        return img
    
    def save(self):
        win = tk.Tk()
        win.geometry("%dx%d+%d+%d" % (0,0,0,0) )
        win.overrideredirect(True)
        ftypes = [('*','png')]
        path = fl.asksaveasfilename(filetypes=ftypes,defaultextension='png',parent=win)
        
        
        if len(path) != 0:
            self.img.save(path)
        win.destroy()
        
    def saveToCut(self):
        output = BytesIO()  # BytesIO实现了在内存中读写bytes
        self.img.convert("RGB").save(output, "BMP") #以RGB模式保存图像
        data = output.getvalue()[14:]
        clip.OpenClipboard() #打开剪贴板
        clip.EmptyClipboard()  #先清空剪贴板
        clip.SetClipboardData(win32con.CF_DIB, data)  #将图片放入剪贴板
        clip.CloseClipboard()
        output.close()
        
    
if __name__ == '__main__':
    s = SCcut()
    s.cut((2,2,100,100))
    s.save()
