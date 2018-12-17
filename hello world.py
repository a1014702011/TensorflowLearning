from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLable = Label(self,text='Hello World!')
        self.helloLable.pack()
        #self.quitButton = Button(self,text='Quit',command=self.quit)
        #self.quitButton.pack()
        self.OutputButton = Button(self,text='你猜会怎样',command=self.hello)
        self.OutputButton.pack()
        self.InfoInput = Entry(self)
        self.InfoInput.pack()
        #列表控件
        self.List = Listbox(self,width=15)
        self.List.pack()
        for item in ['地址','值']:
            self.List.insert(END,item)


    def hello(self):
        info = self.InfoInput.get() or 'World'
        messagebox.showinfo('Message','你好，%s'% info)


app = Application()
app.master.title('Hello World!')
app.mainloop()
#print("hello world")

# import ctypes
# #dll = ctypes.cdll.LoadLibrary("D:DllDisplay2010-1.dll")
# dll = ctypes.cdll.LoadLibrary("D:DllDisplay.dll")
# dll.Display()