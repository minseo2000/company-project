import pyupbit
from tkinter import *
from tkinter import messagebox
#get category of coin

tickers = pyupbit.get_tickers(fiat = "KRW")
allPrice = pyupbit.get_current_price("KRW-BTG")
print(allPrice) # won.
past_price = pyupbit.get_ohlcv(ticker = "KRW-BTG") # 6months
print(past_price)


access = "G6YjEn5YUnSRaiJ5mcfUt8yhwKp2gJOuMSYSJYsB"
secret = "FVmi5v1xxsxsjlMwJOfvagCJJCpHMYZPxeVdQ2KR"

upbit = pyupbit.Upbit(access, secret)
print(upbit.get_balances())

root = Tk()
root.title("UPBIT PROGRAM")
root.geometry("500x300")
root.resizable(False, False)
root.configure(background ='white')
frame = Frame(root)
frame.configure(background='white')
frame.pack()

label_title = Label(frame, text="title")
label_title.pack(side = LEFT)
label_price = Label(frame, text="price")
label_price.pack(side = LEFT)

leftbutton = Button(frame, text = "buy")
leftbutton.pack(side = RIGHT)

rightbutton = Button(frame, text = "sell")
rightbutton.pack(side = RIGHT)


root.mainloop()