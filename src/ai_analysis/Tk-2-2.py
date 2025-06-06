import tkinter
import tkinter.font

root = tkinter.Tk()
root.title("Text 표시")
root.geometry("400x200")
root.resizable(False,False)

font = tkinter.font.Font(size = 30)
label=tkinter.Label(root, text="hello", font=font)
label.pack()

root.mainloop()