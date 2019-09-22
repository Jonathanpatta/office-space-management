import tkinter as tk
import tkclass




class main_menu:
    def __init__(self,master):
        self.canvas = tk.Canvas(master, height = 700 ,width = 800)
        self.canvas.pack()

        # ***** bg image *****

        self.background_image = tk.PhotoImage(file='bluelines.png')
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(relx=0,rely=0,relwidth=1, relheight=1)
        #***** left frame*****
        self.frame1 = tk.Frame(master,bg = '#2ECC71',bd=5)
        self.frame1.place(relx=0.1,rely=0.5,relwidth =0.3,relheight = 0.5,anchor='w')

        self.button = tk.Button(self.frame1, text = "enter user record",bg = '#ECF0F1',fg = 'red',command=lambda:self.insert_user(master))
        self.button.place(rely=0,relwidth=1,relheight=0.25)

        self.button = tk.Button(self.frame1, text = "enter booking record",bg = '#ECF0F1',fg = 'red',command=lambda:self.insert_booking(master))
        self.button.place(rely=0.25,relwidth=1,relheight=0.25)

        self.button = tk.Button(self.frame1, text = "enter room record",bg = '#ECF0F1',fg = 'red',command=lambda:self.insert_room(master))
        self.button.place(rely=0.5,relwidth=1,relheight=0.25)

        self.button = tk.Button(self.frame1, text = "enter usertype record",bg = '#ECF0F1',fg = 'red',command=lambda:self.insert_usertype(master))
        self.button.place(rely=0.75,relwidth=1,relheight=0.25)
        
        #***** right frame*****
        self.frame2 = tk.Frame(master,bg = '#2ECC71',bd=5)
        self.frame2.place(relx=0.9,rely=0.5,relwidth =0.3,relheight = 0.5,anchor='e')

        self.button = tk.Button(self.frame2, text = "show users",bg = '#ECF0F1',fg = 'red',command=lambda:self.read_user(master))
        self.button.place(rely=0,relwidth=1,relheight=0.25)

        self.button = tk.Button(self.frame2, text = "show bookings",bg = '#ECF0F1',fg = 'red',command=lambda:self.read_booking(master))
        self.button.place(rely=0.25,relwidth=1,relheight=0.25)

        self.button = tk.Button(self.frame2, text = "show rooms",bg = '#ECF0F1',fg = 'red',command=lambda:self.read_room(master))
        self.button.place(rely=0.5,relwidth=1,relheight=0.25)

        self.button = tk.Button(self.frame2, text = "show usertypes",bg = '#ECF0F1',fg = 'red',command=lambda:self.read_usertype(master))
        self.button.place(rely=0.75,relwidth=1,relheight=0.25)

    def insert_user(self,master):
        window = tk.Toplevel(master)
        window.wm_title("user insert")
        b=tkclass.tkframe(window,"user_insert")

    def insert_booking(self,master):
        window = tk.Toplevel(master)
        window.wm_title("booking insert")
        b=tkclass.tkframe(window,"booking_insert")

    def insert_room(self,master):
        window = tk.Toplevel(master)
        window.wm_title("room insert")
        b=tkclass.tkframe(window,"room_insert")

    def insert_usertype(self,master):
        window = tk.Toplevel(master)
        window.wm_title("usertype_insert")
        b=tkclass.tkframe(window)

    def read_user(self,master):
        window = tk.Toplevel(master)
        window.wm_title("user read")
        b=tkclass.tkframe(window,"user_read")

    def read_booking(self,master):
        window = tk.Toplevel(master)
        window.wm_title("booking read")
        b=tkclass.tkframe(window,"booking_read")

    def read_room(self,master):
        window = tk.Toplevel(master)
        window.wm_title("room read")
        b=tkclass.tkframe(window,"room_read")

    def read_usertype(self,master):
        window = tk.Toplevel(master)
        window.wm_title("usertype read")
        b=tkclass.tkframe(window,"usertype_read")
        



root = tk.Tk()
#b = tkclass.tkframe(root)
b=main_menu(root)

root.mainloop()
