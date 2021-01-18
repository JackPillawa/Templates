from tkinter import *

class GUI(Frame):
  def __init__(self, root):
    Frame.__init__(self)
    self.root = root
    
    frame = Frame(self.root, bg="red", width=200, height=200)
    frame.pack()

if __name__ == "__main__":
  window = Tk()
  gui = GUI(window)
  window.mainloop()
