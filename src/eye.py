import tkinter as tk
from typing import List, Dict
import random, time, os, sys

msg_list: List = [
    "close your eyes...",
    "rotate your eyes...",
    "blink your eyes 5 times...",
    "Drink water..."
    ]

# time in sec
msg_popup_time:int = 10
sleep_time: int = 10

def on_closing():
    sys.exit(0)

def main():
    """

    """
    # print(os.system("xrandr  | grep \* | cut -d' ' -f4"))
    
    while(True):
        
        win_obj = tk.Tk()
        win_obj.geometry("800x200")
        # win_obj.attributes('-fullscreen', True)
        win_obj.protocol("WM_DELETE_WINDOW", on_closing)
        #Make the window borderless
        # win_obj.overrideredirect(True)
        win_obj.title('Netram notification')

        random.shuffle(msg_list)
        txt = tk.Label(win_obj, font=("Arial", 30), text=msg_list[0])
        txt.pack()

        btn_skip = tk.Button(win_obj, text='Skip >>>', width=20, command=win_obj.destroy)
        btn_skip.pack()

        btn_close = tk.Button(win_obj, text='Close :(', width=20, command=sys.exit)
        btn_close.pack()

        win_obj.mainloop()
        # wait for some time then close the window
        time.sleep(msg_popup_time)

if __name__ == "__main__":
    main()