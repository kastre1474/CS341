import tkinter as tk
import os
import Home

def main():
    master = tk.Tk()
    Home.init(master)
    master.mainloop()

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    main()  