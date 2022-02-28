
import os
import Home
import Conn
import User

def main():


    init_window.createPage()


    master = tk.Tk()
    conn = Conn.conn()
    user = User.user(None, None, None, None, None, None, None)
    Home.init(master, user, conn)
    master.mainloop()
    

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    main()  