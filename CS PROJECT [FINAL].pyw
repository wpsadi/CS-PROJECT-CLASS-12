from tkinter import *
import mysql.connector
from datetime import date

m=Tk()
m.title('Vehicle Registration')
#---------------------------------connection with SQL
conn=mysql.connector.connect(
      host='localhost',
      user='root',
      password='tiger',
      database='system5')

    
#-------------background
m.configure(bg='White')
m.geometry('1200x600')
#----------------------------------------ALL 
ax=PhotoImage(file="logo parivahan sewa.png")
imghjk=PhotoImage(file="card.png")
bx=PhotoImage(file="header1.png")
dx=PhotoImage(file="line.png")
fx=PhotoImage(file="75independence.png")
hx=PhotoImage(file="pmmodi.png")
jx=PhotoImage(file="rc.png")
m_x=PhotoImage(file="reg1.png")

#==========date
newx=str(date.today()).split('-')
datex=newx[2]+'-'+newx[1]+'-'+newx[0]
Label(m,text='Date: '+datex,font=('Georgia',11,'bold')).place(x=1000,y=118)
#Label(m,text='Date: '+datex,bg="light gray",relief='raised',font=('Georgia',18,'bold')).place(x=870,y=110)
#------------------------------main window

Label(m,width=193,height=79,image=ax).place(x=20,y=20)
Label(m,width=722,height=83,image=bx).place(x=240,y=18)
Label(m,width=31,height=83,image=dx).place(x=220,y=20)
Label(m,width=80,height=80,image=fx).place(x=900,y=17)
Label(m,width=80,height=84,image=hx).place(x=1000,y=15)
#=====================FRAME 1
def frame():
    Frame(m,width=500,height=400,bg='#0078D7').place(x=60,y=150)
    fr=Frame(m,bg='#0078D7',width=500,height=400)
    fr.place(x=60,y=150)
    Label(fr,text="View Your Registration Details",bg="light green",fg="black",font=("arial",20)).place(x=60,y=60)
    Label(fr,width=250,height=147,image=jx).place(x=120,y=120)
    #just to remove error
    fr2=Frame(m,bg='#0078D7',width=500,height=400)
    #------------------------------
    b2=Button(fr,text="CLICK HERE",width=20,font=50,bg="#FFB658",command=lambda:[frame3()])#frame 3 missing
    b2.place(x=150,y=300)
    del_temp()


#===================================================FRAME 2
def frame2():
    Frame(m,width=500,height=400,bg='#0078D7').place(x=640,y=150)
    fr2=Frame(m,bg='#0078D7',width=500,height=400)
    fr2.place(x=640,y=150)
    Label(fr2,width=220,height=145,image=m_x).place(x=130,y=120)
    Label(fr2,text="Register New Vehicle" ,bg="light green",fg="black",font=("arial",20)).place(x=110,y=60)
    b3=Button(fr2,text="CLICK HERE",width=20,font=50,bg="#FFB658",command=lambda:[right_new_registration()])
    b3.place(x=150,y=300)
    del_temp()
#=============================FRAME 3
def frame3():
    Frame(m,width=500,height=400,bg='#0078D7').place(x=640,y=150)
    fr3=Frame(m,bg='#0078D7',width=500,height=400)
    fr3.place(x=640,y=150)
    '''Label(fr3,text="View Your Registration Details",bg="light green",fg="black",font=("arial",18)).place(x=30,y=45)
    b5=Button(fr3,text="SignUp",width=10,font=30,bg="#FFB658",command=lambda:[new_registration(fr3)])
    b5.place(x=100,y=80)'''
    
    Label(fr3,text="View Your Registration Details",bg="light green",fg="black",font=("arial",18)).place(x=85,y=15)
    b5=Button(fr3,text="SignUp",width=10,font=30,bg="#FFB658",command=lambda:[new_registration(fr3)])
    b5.place(x=100,y=60)

    b6=Button(fr3,text="  Login  ",width=10,font=30,bg="#FFB658",command=lambda:[login_frame(fr3)])
    b6.place(x=300,y=60)
    '''b6=Button(fr3,text="  Login  ",width=10,font=30,bg="#FFB658",command=lambda:[login_frame(fr3)])
    b6.place(x=300,y=80)'''
    
    Button(fr3,text="< Back",width=6,font=40,bg="#FFB658",command=lambda:[home()]).place(x=0,y=0)
    del_temp()
    
#----------------------------------------------------------delete data that is temporary
def del_temp():
    import mysql.connector
    import random
    
    global conn
    conn=mysql.connector.connect(host='localhost',user='root',password='tiger',database='system5')
    cur=conn.cursor()
    cur.execute('select v_id from vrsuser;')
    l1=[]#l1 ke andar vid hogi
    x=cur.fetchall()
    for i in x:
        
        if len(i)==1:
            l1.append(i[0])
    cur=conn.cursor()
    cur.execute('select v_id from logindata;')
    l2=[]#l1 ke andar vid hogi
    x=cur.fetchall()
    for i in x:
        
        if len(i)==1:
            l2.append(i[0])
    if len(l1)!=0:
        for i in range(len(l1)):
            if l1[i] not in l2:
                cur=conn.cursor()
                cur.execute('delete from vrsuser where v_id="{}";'.format(l1[i]))
                conn.commit()  
#++++++++++++++++++++++++++Registration through [FRAME 1]

def back_signup_fr3():
    home()
    frame3()
    del_temp()
def new_registration(fr3):
    Label(fr3,text='  ' ,width=15,bg='#0078D7').place(x=350,y=380)
    Label(fr3,text='  ' ,width=50,bg='#0078D7').place(x=180,y=380)
    Button(fr3,text="< Back",width=6,font=40,bg="#FFB658",command=lambda:[back_signup_fr3()]).place(x=0,y=0)
    Label(fr3,text='Enter Your Name :' ,bg='light green',width=20).place(x=40,y=100)
    Label(fr3,text='Enter Car Number :' ,bg='light green',width=20).place(x=40,y=130)
    Label(fr3,text='Enter Contact Number :' ,bg='light green',width=20).place(x=40,y=160)
    Label(fr3,text='Enter Email ID :' ,bg='light green',width=20).place(x=40,y=190)
    Label(fr3,text='Enter Address :' ,bg='light green',width=20).place(x=40,y=220)
    Label(fr3,text='Enter Pincode :' ,bg='light green',width=20).place(x=40,y=250)
    Label(fr3,text='Enter City :' ,bg='light green',width=20).place(x=40,y=280)
    Label(fr3,text='Enter State :' ,bg='light green',width=20).place(x=40,y=310)
    Label(fr3,text='Unique VID Generated :' ,bg='light green',width=20).place(x=40,y=340)

    
    
          
    name=Entry(fr3,width=30)
    name.place(x=240,y=100)
    
    car_num=Entry(fr3,width=30)
    car_num.place(x=240,y=130)
      
    contact=Entry(fr3,width=30)
    contact.place(x=240,y=160)
    #contact=str(contact.get()).lower().strip()
    email=Entry(fr3,width=30)
    email.place(x=240,y=190)
    
    address=Entry(fr3,width=30)
    address.place(x=240,y=220)
    pincode=Entry(fr3,width=30)
    pincode.place(x=240,y=250)
    #pincode=str(pincode.get()).strip()
    city=Entry(fr3,width=30)
    city.place(x=240,y=280)
    #city=city.get().lower().strip()
    state=Entry(fr3,width=30)
    state.place(x=240,y=310)
    #Label(fr3,text=vid,relief='raised',width=26).place(x=240,y=340)                 #use  of "lambda": to control the execution of a function that requires parameters
    sub_sign=Button(fr3,text='S\nU\nB\nM\nI\nT',height=6,width=2,command=lambda:[com_sub_sign(car_num,name,contact,email,address.get(),pincode,city,state,fr3)])#sub_sign
    sub_sign.place(x=450,y=220)
    del_temp()
def view_certificate(vid,fr3):
      import mysql.connector
      blank_fr=Frame(fr3,bg='#0078D7',width=500,height=400)
      blank_fr.place(x=0,y=0)
      conn=mysql.connector.connect(host='localhost',user='root',password='tiger',database='system5')
      cur=conn.cursor()
      cur.execute('select * from vrsuser where v_id="{}";'.format(vid))
      x=cur.fetchmany(1)
      for i in x:
            if len(i)!=0:
                  l=i
                  break
      #img=PhotoImage(file="card.png")
      n=Label(blank_fr,width=415,height=255,image=imghjk)
      Label(blank_fr,text=l[0].upper(),width=6,relief='raised').place(x=385,y=136)#VID
      Label(blank_fr,text=l[2].upper(),width=25,relief='raised').place(x=195,y=173)#name
#      Label(blank_fr,text=l[1].upper(),width=25,relief='raised').place(x=195,y=173)#NAME
      Label(blank_fr,text=l[1].upper(),width=15,relief='raised').place(x=230,y=136)#CAR NUMBER
      Label(blank_fr,text=l[5],width=30,relief='raised').place(x=205,y=208)#ADDRESS
      Label(blank_fr,text=l[7].upper(),width=20,relief='raised').place(x=180,y=240)#CITY
      Label(blank_fr,text=l[8].upper(),width=20,relief='raised').place(x=190,y=267)#STATE
      Label(blank_fr,text=l[6].upper(),width=10,relief='raised').place(x=200,y=295)#PINCODE
#      Label(blank_fr,text=l[4],width=21,relief='raised').place(x=133,y=242)#EMAIL
      Label(blank_fr,text='YOUR DETAILS ARE STORED TEMPORARILY AND WILL BE DELETED SHORTLY',bg="red",fg="white",font=('ARIAL',10),relief=RAISED,width=62).place(x=0,y=15)
#      Label(blank_fr,text=l[3].upper(),width=28,relief='raised').place(x=236,y=268)#CONTACT
      n.place(x=50,y=80)
      #cur.execute('delete from vrsuser where v_id="{}";'.format(l[0]))
      Button(blank_fr,text='CLOSE',bg="#FFB658",width=8,height=2,command=lambda:[home()]).place(x=220,y=360)
      Button(blank_fr,text='SAVE',bg="#FFB658",width=8,height=2,command=lambda:[save_reg(fr3,l)]).place(x=220,y=37)
def save_reg(fr3,l):
      blank_fr=Frame(fr3,bg='#0078D7',width=500,height=400)
      blank_fr.place(x=0,y=0)
      right_com_sub_sign(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],fr3)      
def com_sub_sign(car_num,name,contact,email,address,pincode,city,state,fr3):

    import mysql.connector
    import random
    
    global conn
    conn=mysql.connector.connect(host='localhost',user='root',password='tiger',database='system5')
    cur=conn.cursor()
    cur.execute('select v_id from vrsuser;')
    l1=[]#l1 ke andar vid hogi
    x=cur.fetchall()
    for i in x:
        
        if len(i)==1:
            l1.append(i[0])
    #vid=eval(input('Enter your UNIQUE'))      #ye randomly generate hoga

    s='0123456789'
    vid_u=False
    while vid_u==False:
        c=0
        vid=name.get()[0:2].upper()
        while c<4:
            x=random.randint(0,9)
            vid+=s[x]
            c+=1
        if vid not in l1:
            vid_u=True
    cur=conn.cursor()
    #Label(fr3,width=3,height=7,bg='#0078D7').place(x=450,y=220)
    Label(fr3,text=vid,relief='raised',bg='sienna3',fg='black',width=20,font=('bold')).place(x=240,y=340)
    name=name.get().strip().lower()
    car_num=car_num.get().upper().strip() 
    contact=str(contact.get()).lower().strip()
    email=str(email.get()).lower().strip()
    pincode=str(pincode.get()).strip()
    city=city.get().lower().strip()
    state=state.get().lower().strip()
      
    query='insert into vrsuser values("{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(vid,car_num,name,contact,email,address,pincode,city,state)                                       
    cur.execute(query)
    Label(fr3,text='REGISTRATION SUCCESSFULL',relief='raised').place(x=120,y=370)
    conn.commit()
    certificate_button=Button(fr3,text='VIEW CERTIFICATE',height=1,width=17,command=lambda:[view_certificate(vid,fr3)])
    certificate_button.place(x=330,y=370)
    
def view_certificate_login(vid,fr5):
      import mysql.connector
      blank_fr=Frame(fr5,bg='#0078D7',width=500,height=400)
      blank_fr.place(x=0,y=0)
      conn=mysql.connector.connect(host='localhost',user='root',password='tiger',database='system5')
      cur=conn.cursor()
      cur.execute('select * from vrsuser where v_id="{}";'.format(vid))
      x=cur.fetchmany(1)
      for i in x:
            if len(i)!=0:
                  l=i
                  break
      #img=PhotoImage(file="card.png")
      n=Label(blank_fr,width=415,height=255,image=imghjk)
      Label(blank_fr,text=l[0].upper(),width=6,relief='raised').place(x=385,y=136)#VID
      Label(blank_fr,text=l[2].upper(),width=25,relief='raised').place(x=195,y=173)#name
#      Label(blank_fr,text=l[1].upper(),width=25,relief='raised').place(x=195,y=173)#NAME
      Label(blank_fr,text=l[1].upper(),width=15,relief='raised').place(x=230,y=136)#CAR NUMBER
      Label(blank_fr,text=l[5],width=30,relief='raised').place(x=205,y=208)#ADDRESS
      Label(blank_fr,text=l[7].upper(),width=20,relief='raised').place(x=180,y=240)#CITY
      Label(blank_fr,text=l[8].upper(),width=20,relief='raised').place(x=190,y=267)#STATE
      Label(blank_fr,text=l[6].upper(),width=10,relief='raised').place(x=200,y=295)#PINCODE
#      Label(blank_fr,text=l[4],width=21,relief='raised').place(x=133,y=242)#EMAIL
     
#      Label(blank_fr,text=l[3].upper(),width=28,relief='raised').place(x=236,y=268)#CONTACT
      n.place(x=50,y=80)
      Button(blank_fr,text='CLOSE',width=8,height=2,bg="#FFB658",command=lambda:[home()]).place(x=220,y=360)
      del_temp()
def login(name,vid,password,fr5,fr3):
      cur=conn.cursor()
      Label(fr5,text='  ',width=100,height=4,bg='#0078D7').place(x=130,y=30)
      cur.execute('select * from logindata where name="{}" and password="{}" and v_id="{}";'.format(name,password,vid))
      x=cur.fetchmany(1)
      if len(x)==0:
            Label(fr5,width=500,height=400,bg='#0078D7').place(x=0,y=0)
            Label(fr5,text="Invalid Credentials !!",bg="red",fg="white",font=('ARIAL',20),relief=RAISED,width=20).place(x=90,y=160)
            login_but=Button(fr5,text='Click To Retry !',bg="black",fg="white",height=3,width=25,command=lambda:[login_frame(fr3)])
            login_but.place(x=150,y=230)
            Button(fr5,text="< Back",width=6,font=40,bg="#FFB658",command=lambda:[login_frame(fr3)]).place(x=0,y=0)
      else:
            Button(fr5,text="< Back",width=6,font=40,bg="#FFB658",command=lambda:[login_frame(fr3)]).place(x=0,y=0)
            Label(fr5,width=18,height=4,bg='#0078D7').place(x=180,y=230)
            #l=[x[0],x[1],x[2]]
            #Label(fr5,text='LOGIN SUCCESSFULL',bg='gold3').place(x=250,y=200)
            #card_button=Button(fr5,text='VIEW CA',width=8,command=lambda:[view_certificate_login(vid,fr5)])
            #card_button.place(x=350,y=380)
            Label(fr5,text="Login Successful !!",bg="gold3",font=("arial",25)).place(x=100,y=230)
            certificate_button=Button(fr5,text='VIEW CERTIFICATE',height=3,width=17,bg="black",fg="white",command=lambda:[view_certificate_login(vid,fr5)])
            certificate_button.place(x=170,y=280)

      del_temp()
def back_fr5() :
    home()
    frame3()
    del_temp()
def login_frame(fr3):
      
      fr5=Frame(fr3,width=500,height=400,bg='#0078D7')
      
      Label(fr5,width=500,height=400,bg='#0078D7').place(x=0,y=0)
      Button(fr5,text="< Back",width=6,font=40,bg="#FFB658",command=lambda:[back_fr5()]).place(x=0,y=0)
      c=Label(fr5,text='Enter Your NAME :' ,bg='light green',width=20,font=("arial",11))
      c.place(x=40,y=120)
      g=Label(fr5,text='Enter PASSWORD :' ,bg='light green',width=25)
      g.place(x=40,y=150)
      Label(fr5,text='Enter V_ID :' ,bg='light green',width=25).place(x=40,y=180)
      name=Entry(fr5,width=30)
      name.place(x=250,y=120)
      password=Entry(fr5,width=30,show='*')
      password.place(x=250,y=150)
      vid=Entry(fr5,width=30)
      vid.place(x=250,y=180)
      login_but=Button(fr5,text='ENTER',bg="black",fg="white",height=3,width=15,command=lambda:[login(name.get().strip().lower(),vid.get().strip().lower(),password.get().strip(),fr5,fr3)])
      login_but.place(x=180,y=230)
      fr5.place(x=0,y=0)
      del_temp()
def right_submit_blank_fr4(name,vid,password,blank_fr4,fr4):
      cur=conn.cursor()
      Label(fr4,text='',width=20,height=6,bg='#0078D7').place(x=160,y=200)
      cur.execute('insert into logindata values("{}","{}","{}");'.format(name.get().strip(),vid,password.get().strip()))
      Label(blank_fr4,text='YOUR VEHICLE REGISTRATION IS LINKED TO YOUR ACCOUNT',relief='raised',bg='gold3',font=("arial",11)).place(x=30,y=300)
      conn.commit()
      Button(fr4,text="CLOSE",width=6,height=1,font=30,bg="#FFB658",command=lambda:[home()]).place(x=215,y=333)
def right_com_sub_sign(vid,car_num,name,contact,email,address,pincode,city,state,fr4):

      conn=mysql.connector.connect(host='localhost',user='root',password='tiger',database='system5')
      cur=conn.cursor()
      try:
          name=name.get().strip().lower()
          car_num=car_num.get().upper().strip() 
          contact=str(contact.get()).lower().strip()
          email=str(email.get()).lower().strip()
          pincode=str(pincode.get()).strip()
          city=city.get().lower().strip()
          state=state.get().lower().strip()
          query='insert into vrsuser values("{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(vid,car_num,name,contact,email,address,pincode,city,state)                                       
          #print(query)
          cur.execute(query)
          conn.commit()
      except:
          None

      blank_fr4=Frame(fr4,bg='#0078D7',width=500,height=400)
      blank_fr4.place(x=0,y=0)
      Label(blank_fr4,text='REGISTRATION SUCCESSFULL',relief='raised',font=("arial",14)).place(x=100,y=30)
      Label(blank_fr4,text="CREATE NEW ACCOUNT",bg="light green",fg="black",font=("arial",20)).place(x=80,y=80)
      c=Label(blank_fr4,text='Enter Your NAME :' ,bg='light green',width=20,font=("arial",11))
      c.place(x=40,y=140)
      g=Label(blank_fr4,text='Enter PASSWORD :' ,bg='light green',width=26)
      g.place(x=40,y=180)
      name=Entry(blank_fr4,width=30)
      name.place(x=250,y=140)
      password=Entry(blank_fr4,width=30)
      password.place(x=250,y=180)
      sub_sign=Button(fr4,text='CREATE ACCOUNT',bg="Black",fg="white",height=3,width=15,command=lambda:[right_submit_blank_fr4(name,vid,password,blank_fr4,fr4)])
      sub_sign.place(x=190,y=230)
def r_vid_print_back():
    home()
    right_new_registration()
    del_temp()
def r_vid_print(name,car_num,contact,email,address,pincode,city,state,fr4):

    import mysql.connector
    import random
    
    global conn
    conn=mysql.connector.connect(host='localhost',user='root',password='tiger',database='system5')
    cur=conn.cursor()
    cur.execute('select v_id from vrsuser;')
    l1=[]#l1 ke andar vid hogi
    x=cur.fetchall()
    for i in x:
        
        if len(i)==1:
            l1.append(i[0])


    #vid=eval(input('Enter your UNIQUE'))      #ye randomly generate hoga

    
    s='0123456789'
    vid_u=False
    while vid_u==False:
        c=0
        vid=name.get()[0:2].upper()
        while c<4:
            x=random.randint(0,9)
            vid+=s[x]
            c+=1
        if vid not in l1:
            vid_u=True
    Button(fr4,text="< Back",width=6,font=40,bg="#FFB658",command=lambda:[r_vid_print_back()]).place(x=0,y=0)
    Label(fr4,text=vid,relief='raised',width=20,bg='sienna3',fg='black',font=('bold')).place(x=240,y=320)
    Label(fr4,text=' ',width=50,height=2,bg='#0078D7').place(x=190,y=360)
    sub_sign=Button(fr4,text='NEXT ->',width=10,command=lambda:[right_com_sub_sign(vid,car_num,name,contact,email,address,pincode,city,state,fr4)])#sub_sign
    sub_sign.place(x=290,y=360)
    del_temp()
def right_new_registration():
      Frame(m,width=500,height=400,bg='#0078D7').place(x=60,y=150)
      fr4=Frame(m,bg='#0078D7',width=500,height=400)
      fr4.place(x=60,y=150)
      Button(fr4,text="< Back",width=6,font=40,bg="#FFB658",command=lambda:[home()]).place(x=0,y=0)
      Label(fr4,text="Register New Vehicle" ,bg="light green",fg="black",font=("arial",20)).place(x=110,y=30)
      
      Label(fr4,text='  ' ,width=15,bg='#0078D7').place(x=350,y=380)
      Label(fr4,text='  ' ,width=50,bg='#0078D7').place(x=180,y=380)
      c=Label(fr4,text='Enter Your Name :' ,bg='light green',width=20)
      c.place(x=40,y=80)
      z=Label(fr4,text='Enter Car Number :' ,bg='light green',width=20)
      z.place(x=40,y=110)
      d=Label(fr4,text='Enter Contact Number :' ,bg='light green',width=20)
      d.place(x=40,y=140)
      e=Label(fr4,text='Enter Email ID :' ,bg='light green',width=20)
      e.place(x=40,y=170)
      f=Label(fr4,text='Enter Address :' ,bg='light green',width=20)
      f.place(x=40,y=200)
      g=Label(fr4,text='Enter Pincode :' ,bg='light green',width=20)
      g.place(x=40,y=230)
      h=Label(fr4,text='Enter City :' ,bg='light green',width=20)
      h.place(x=40,y=260)
      i=Label(fr4,text='Enter State :' ,bg='light green',width=20)
      i.place(x=40,y=290)
      j=Label(fr4,text='Unique VID Generated :' ,bg='light green',width=20)
      j.place(x=40,y=320)
#==============ENTRY
      name=Entry(fr4,width=30)
      name.place(x=240,y=80)
      car_num=Entry(fr4,width=30)
      car_num.place(x=240,y=110)
      contact=Entry(fr4,width=30)
      contact.place(x=240,y=140)
      email=Entry(fr4,width=30)
      email.place(x=240,y=170)
      address=Entry(fr4,width=30)
      address.place(x=240,y=200)
      pincode=Entry(fr4,width=30)
      pincode.place(x=240,y=230)
      city=Entry(fr4,width=30)
      city.place(x=240,y=260)
      state=Entry(fr4,width=30)
      state.place(x=240,y=290)
      sub_sign=Button(fr4,text='Submit ->',width=10,command=lambda:[r_vid_print(name,car_num,contact,email,address.get(),pincode,city,state,fr4)])#sub_sign
      sub_sign.place(x=190,y=360)
      del_temp()

#=========================================================================================================================

      
def home():
    
    
    del_temp()
    frame()
    frame2()

home_but=Button(m,text="HOME",width=10,font=30,bg="#FFB658",command=home)
home_but.place(x=548,y=115)
home()
m.mainloop()
