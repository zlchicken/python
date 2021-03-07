"""
@version: python3.7
@Author  : ZL
@Explain :
@Time    : 2021/2/28 21:50
@File    : tkHello
@Software: PyCharm
"""
import tkinter
top = tkinter.Tk()
quit = tkinter.Button(top,text='hello world!',command=top.quit)
quit.pack()
tkinter.mainloop()