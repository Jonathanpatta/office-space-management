import tkinter as tk
import mysql.connector as sql

#import functions


class tkframe:
    def __init__(self,master):
        # ***** db call *****
        self.mydb = sql.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "Jonu@123",
                        database = "dbms_project"
                )
        self.mycursor = self.mydb.cursor()
        print(self.mydb)
        print ("connected to database")
       

        
         # ***** canvas ******
        self.canvas = tk.Canvas(master, height = 700 ,width = 800)
        self.canvas.pack()

        # ***** bg image *****

        self.background_image = tk.PhotoImage(file='bluelines.png')
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(relx=0,rely=0,relwidth=1, relheight=1)

        # ***** top part ******
        self.frame = tk.Frame(master,bg = '#2ECC71',bd=5)
        self.frame.place(relx=0.5,rely=0.1,relwidth =0.8,relheight = 0.07,anchor='n')

        self.entry = tk.Entry(self.frame,bg = '#ECF0F1')
        self.entry.place(relx=0.2,relwidth=0.5,relheight=1)

        

        self.button = tk.Button(self.frame, text = "click to enter client record",bg = '#ECF0F1',fg = 'red',command=lambda: self.show_db())#self.insert_clients(self.entry.get()))
        self.button.place(relx=0.75,relwidth=0.25,relheight=1)

        self.lab = tk.Label(self.frame,text ="text label",bg = '#ECF0F1',fg='red')
        self.lab.place(relwidth=0.15,relheight=1)
        

        # ****** lower textbox ******

        self.lower_frame = tk.Frame(master, bg='#2ECC71', bd=10)
        self.lower_frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.25, anchor='n')



        self.label = tk.Label(self.lower_frame,fg='red', bg = '#ECF0F1')
        self.label.place(relwidth=1, relheight=1)

    def get_entry(self):
        return self.entry.get()

    def show_label(self,entry):
        self.label['text']=entry

    # ************************************** DBMS call functions *************************************************


    def connect_db(self):
            self.mydb = sql.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "Jonu@123",
                    database = "dbms_project"
            )
            self.mycursor = self.mydb.cursor()
            print(self.mydb)
            print ("connected to database")

    def show_db(self):
        self.mycursor.execute("SHOW DATABASES")
        entry=""
        for db in self.mycursor:
            entry=entry+"\n"+db[0]
        self.show_label(entry)

    def insert_clients(self,entry):
        tup = tuple(entry)
        print(entry)
        client="INSERT INTO client (clientid,fname,lname,phoneno,company) VALUES (%s, %s, %s, %s, %s)"

        clid=self.entry.get()
        print(tup)
        #self.mycursor.execute(client,tup)
        self.get_text(entry)
        #self.mydb.commit()

    def get_text(self,entry):
        self.show_label( entry + '\nhas been added to the table' )
        

