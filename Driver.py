import tkinter as tk
import os
import init_window

def main():
    master = tk.Tk()
    init_window.initwin(master)
    master.mainloop()

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    main()  