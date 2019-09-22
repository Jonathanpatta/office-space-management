import tkinter as tk
import mysql.connector as sql
import datetime

#import functions


class tkframe:
    def __init__(self,master,text):
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
        self.entry.place(relwidth=0.75,relheight=1)

        

        self.button = tk.Button(self.frame, text = "submit",bg = '#ECF0F1',fg = 'red',command=lambda: self.func_call(text,self.entry.get()))
        self.button.place(relx=0.80,relwidth=0.2,relheight=1)

        
        

        # ****** lower textbox ******

        self.lower_frame = tk.Frame(master, bg='#2ECC71', bd=10)
        self.lower_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.75, anchor='n')



        self.label = tk.Label(self.lower_frame,fg='red', bg = '#ECF0F1')
        self.label.place(relwidth=1, relheight=1)

    def get_entry(self):
        return self.entry.get()

    def show_label(self,entry):
        self.label['text']=entry

    # ************************************** DBMS call functions *************************************************

    def func_call(self,text,entry):
        if(text=="user_insert"):
            self.insert_users(entry)
        if(text=="booking_insert"):
            self.insert_bookings(entry)
        if(text=="room_insert"):
            self.insert_rooms(entry)
        if(text=="usertype_insert"):
            self.insert_usertype(entry)

        if(text=="user_read"):
            self.read_users()
        if(text=="booking_read"):
            self.read_bookings()
        if(text=="room_read"):
            self.read_rooms()
        if(text=="usertype_read"):
            self.read_usertype()

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
#************************************users table****************************************************
    def insert_users(self,entry):
        fname,lname,phno,company,usertype,loginid,password=entry.split(',')

        
        tup=(fname,lname,phno,company,usertype,loginid,password)
        client="INSERT INTO users (fname,lname,phoneno,company,usertype,loginid,password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.execute(client, tup)
        self.show_label(entry)
        self.read_users()
        #self.mydb.commit()


    def read_users(self):
        self.mycursor.execute("SELECT * FROM `users`")
        fetch = self.mycursor.fetchall()
        print(fetch[0][0])
        p=""
        for data in fetch:
            for data1 in data:
                p+=str(data1)+","
            p+="\n"
        self.show_label(p)

#************************************bookings table****************************************************
    def insert_bookings(self,entry):
        username,password,start_year,start_month,start_day,end_year,end_month,end_day,room_name=entry.split(',')
        
        query = ("SELECT password,loginid,userid FROM users WHERE password = %s AND loginid = %s")
        self.mycursor.execute(query,(password,username))
        fetch=self.mycursor.fetchall()
        if len(fetch)!=1:
            self.show_label("access denied!!")

        else:
            query1 = ("SELECT roomid FROM rooms WHERE roomname = %s")
            self.mycursor.execute(query1,(room_name,))
            fetch1=self.mycursor.fetchall()
            if len(fetch1)!=1:
                self.show_label("room not found.selecting default room")
                roomid=2
            else:
                roomid=fetch1[0][0]
            description="nice!"
            startdt=datetime.datetime(int(start_year),int(start_month),int(start_day),9,0,0,0)
            enddt=datetime.datetime(int(end_year),int(end_month),int(end_day),21,0,0,0)
            createdt=datetime.datetime.now()
            modifydt=datetime.datetime.now()
            userid=fetch[0][2]
            tup=(startdt,enddt,description,userid,roomid,createdt,modifydt)
            client="INSERT INTO bookings (startdate,enddate,description,userid,roomid,createddate,modifieddate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.mycursor.execute(client, tup)
            self.show_label(entry)
            #self.mydb.commit()
        


    def read_bookings(self):
        self.mycursor.execute("SELECT * FROM `bookings`")
        fetch = self.mycursor.fetchall()
        p=""
        for data in fetch:
            p=p+data+"\n"
        self.show_label(p)

#************************************rooms table****************************************************
    def insert_rooms(self,entry):
        username,password,room_name,seats,room_area,price_seat,price_sqft=entry.split(',')
        
        query = ("SELECT password,loginid,userid,fname FROM users WHERE password = %s AND loginid = %s")
        self.mycursor.execute(query,(password,username))
        fetch=self.mycursor.fetchall()
        if len(fetch)!=1:
            self.show_label("access denied!!")

        else:
            description="nice!"
            createdt=datetime.datetime.now()
            modifydt=datetime.datetime.now()
            userid=fetch[0][2]
            createdby=fetch[0][3]
            tup=(room_name,seats,room_area,price_seat,price_sqft,description,createdt,modifydt,createdby)
            client="INSERT INTO rooms (roomname,seats,roomarea,priceseat,pricesqft,description,createddate,modifieddate,createdby) VALUES (%s, %s, %s, %s, %s, %s, %s, %s. %s)"
            self.mycursor.execute(client, tup)
            self.show_label(entry)
            #self.mydb.commit()
        


    def read_rooms(self):
        self.mycursor.execute("SELECT * FROM `rooms`")
        fetch = self.mycursor.fetchall()
        p=""
        for data in fetch:
            p=p+data+"\n"
        self.show_label(p)

#************************************usertype table****************************************************
    def insert_usertype(self,entry):
        fname,lname,phno,company,usertype,loginid,password=entry.split(',')

        
        tup=(fname,lname,phno,company,usertype,loginid,password)
        client="INSERT INTO users (fname,lname,phoneno,company,usertype,loginid,password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.execute(client, tup)
        self.show_label(entry)
        self.read_users()
        #self.mydb.commit()


    def read_usertype(self):
        self.mycursor.execute("SELECT * FROM `usertype`")
        fetch = self.mycursor.fetchall()
        p=""
        for data in fetch:
            p=p+data+"\n"
        self.show_label(p)
