import tkinter
import tkinter.font

root = tkinter.Tk()
root.title("타이머 출력")
root.geometry("400x200")
root.resizable(False,False)

font = tkinter.font.Font(size = 30)
label=tkinter.Label(root, text="", font=font)
label.pack()

cnt = 0
def get_coin_1sec():
    global cnt
    now_btc_price = str(cnt)
    cnt = cnt + 1
    label.config(text=now_btc_price)
    root.after(1000,get_coin_1sec)

get_coin_1sec()

root.mainloop()