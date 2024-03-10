from tkinter import *
from PIL import Image,ImageTk
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector
#function part
def message():
    data()
    s1=station1.get()
    s2=station2.get()
    if s1==""and s2=="":
        messagebox.showerror("Error!","Please input a valid station, as mentioned in your left!")
    elif s1=="":
         messagebox.showerror("Error!","Please input a valid station, as mentioned in your left!")
    #elif(s1!="Gurudev Chauraha" or s1!="IIT Kanpur" or s1!="Kalyanpur" or s1!="LLR Hospital" or s1!="Moti Jheel" or s2!="Rawatpur" or s1=="SPM Hospital" or s1!="Vishwavidalya")and(s2!="Gurudev Chauraha" or s2!="IIT Kanpur" or s2!="Kalyanpur" or s2!="LLR Hospital" or s2!="Motijheel" or s2!="Rawatpur" or s2!="SPM Hospital" or s2!="Vishwavidalya"):
        #messagebox.showerror("Error!","Please enter stations as mentioned in your left")
    #Gurudev Chauraha--
    elif s1=="Gurudev Chauraha" and s2=="Gurudev Chauraha":
        messagebox.showerror("Error!","Staions can not be similar")
    elif s1=="Gurudev Chauraha" and s2=="IIT Kanpur":
        metro.destroy()
        import gc_iit
        #database linkup
    elif s1=="Gurudev Chauraha" and s2=="Kalyanpur":
        metro.destroy()
        import gc_kalyanpur
    elif s1=="Gurudev Chauraha" and s2=="LLR Hospital":
        metro.destroy()
        import gc_llr
    elif s1=="Gurudev Chauraha" and s2=="Moti Jheel":
        metro.destroy()
        import gc_motijheel
    elif s1=="Gurudev Chauraha" and s2=="Rawatpur":
        metro.destroy()
        import gc_rawatpur
    elif s1=="Gurudev Chauraha" and s2=="SPM Hospital":
        metro.destroy()
        import gc_spm
    elif s1=="Gurudev Chauraha" and s2=="Vishwavidalya":
        metro.destroy()
        import gc_vishwavidyalay
    #IIT Kanpur--
    elif s1=="IIT Kanpur" and s2=="IIT Kanpur":
        messagebox.showerror("Error!","Staions can not be similar")
    elif s1=="IIT Kanpur" and s2=="Gurudev Chauraha":
        metro.destroy()
        import iit_gc
    elif s1=="IIT Kanpur" and s2=="Kalyanpur":
        metro.destroy()
        import iit_kalyanpur
    elif s1=="IIT Kanpur" and s2=="LLR Hospital":
        metro.destroy()
        import iit_llr
    elif s1=="IIT Kanpur" and s2=="Moti Jheel":
        metro.destroy()
        import iit_motijheel
    elif s1=="IIT Kanpur" and s2=="Rawatpur":
        metro.destroy()
        import iit_rawatpur
    elif s1=="IIT Kanpur" and s2=="SPM Hospital":
        metro.destroy()
        import iit_spm
    elif s1=="IIT Kanpur" and s2=="Vishwavidalya":
        metro.destroy()
        import iit_vishwavidyalay
    #Kalyanpur--
    elif s1=="Kalyanpur" and s2=="Kalyanpur":
        messagebox.showerror("Error!","Staions can not be similar")
    elif s1=="Kalyanpur" and s2=="Gurudev Chauraha":
        metro.destroy()
        import kalyanpur_gc
    elif s1=="Kalyanpur" and s2=="IIT Kanpur":
        metro.destroy()    
        import kalyanpur_iit
    elif s1=="Kalyanpur" and s2=="LLR Hospital":
        metro.destroy()    
        import kalyanpur_llr
    elif s1=="Kalyanpur" and s2=="Moti Jheel":
        metro.destroy()
        import kalyanpur_motijheel
    elif s1=="Kalyanpur" and s2=="Rawatpur":
        metro.destroy()
        import kalyanpur_rawatpur
    elif s1=="Kalyanpur" and s2=="SPM Hospital":
        metro.destroy()     
        import kalyanpur_spm
    elif s1=="Kalyanpur" and s2=="Vishwavidalya":
        metro.destroy()
        import kalyanpur_vishwavidyalay
    #LLR HOSPITAL--
    elif s1=="LLR Hospital" and s2=="LLR Hospital":
        messagebox.showerror("Error!","Staions can not be similar")
    elif s1=="LLR Hospital" and s2=="Gurudev Chauraha":
        metro.destroy()
        import llr_gc
    elif s1=="LLR Hospital" and s2=="IIT Kanpur":
        metro.destroy()
        import llr_iit
    elif s1=="LLR Hospital" and s2=="Kalyanpur":
        metro.destroy()     
        import llr_kalyanpur
    elif s1=="LLR Hospital" and s2=="Moti Jheel":
        metro.destroy()     
        import llr_motijheel
    elif s1=="LLR Hospital" and s2=="Rawatpur":
        metro.destroy()    
        import llr_rawatpur
    elif s1=="LLR Hospital" and s2=="SPM Hospital":
        metro.destroy()
        import llr_spm
    elif s1=="LLR Hospital" and s2=="Vishwavidalya":
        metro.destroy()
        import llr_vishwavidyalay
    #MOTI JHEEL--
    elif s1=="Moti Jheel" and s2=="Moti Jheel":
        messagebox.showerror("Error!","Staions can not be similar")
    elif s1=="Moti Jheel" and s2=="Gurudev Chauraha":
        metro.destroy()   
        import motijheel_gc
    elif s1=="Moti Jheel" and s2=="IIT Kanpur":
        metro.destroy()    
        import motijheel_iit
    elif s1=="Moti Jheel" and s2=="Kalyanpur":
        metro.destroy()
        import motijheel_kalyanpur
    elif s1=="Moti Jheel" and s2=="LLR Hospital":
        metro.destroy()
        import motijheel_llr
    elif s1=="Moti Jheel" and s2=="Rawatpur":
        metro.destroy()
        import motijheel_rawatpur
    elif s1=="Moti Jheel" and s2=="SPM Hospital":
        metro.destroy()     
        import motijheel_spm
    elif s1=="Moti Jheel" and s2=="Vishwavidalya":
        metro.destroy()
        import motijheel_vishwavidyalay
    #RAWATPUR--
    elif s1=="Rawatpur" and s2=="Rawatpur":
        messagebox.showerror("Error!","Staions can not be similar")
    elif s1=="Rawatpur" and s2=="Gurudev Chauraha":
        metro.destroy()  
        import rawatpur_gc
    elif s1=="Rawatpur" and s2=="IIT Kanpur":
        metro.destroy()   
        import rawatpur_iit
    elif s1=="Rawatpur" and s2=="Kalyanpur":
        metro.destroy()
        import rawatpur_kalyanpur
    elif s1=="Rawatpur" and s2=="LLR Hospital":
        metro.destroy()
        import rawatpur_llr
    elif s1=="Rawatpur" and s2=="Moti Jheel":
        metro.destroy()
        import rawatpur_motijheel
    elif s1=="Rawatpur" and s2=="SPM Hospital":
        metro.destroy()    
        import rawatpur_spm
    elif s1=="Rawatpur" and s2=="Vishwavidalya":
        metro.destroy()
        import rawatpur_vishwavidyalay
    #SPM Hospital--
    elif s1=="SPM Hospital" and s2=="SPM Hospital":
        messagebox.showerror("Error!","Staions can not be similar")
    elif s1=="SPM Hospital" and s2=="Gurudev Chauraha":
        metro.destroy()
        import spm_gc
    elif s1=="SPM Hospital" and s2=="IIT Kanpur":
        metro.destroy()
        import spm_iit
    elif s1=="SPM Hospital" and s2=="Kalyanpur":
        metro.destroy()  
        import spm_kalyanpur
    elif s1=="SPM Hospital" and s2=="LLR Hospital":
        metro.destroy()
        import spm_llr
    elif s1=="SPM Hospital" and s2=="Moti Jheel":
        metro.destroy()   
        import spm_motijheel
    elif s1=="SPM Hospital" and s2=="Rawatpur":
        metro.destroy()   
        import spm_rawatpur
    elif s1=="SPM Hospital" and s2=="Vishwavidalya":
        metro.destroy()
        import spm_vishwavidyalay
    #Vishwavidalya--
    elif s1=="Vishwavidalya" and s2=="Vishwavidalya":
        messagebox.showerror("Error!","Staions can not be similar")
    elif s1=="Vishwavidalya" and s2=="Gurudev Chauraha":
        metro.destroy()
        import vishwavidyalay_gc
    elif s1=="Vishwavidalya" and s2=="IIT Kanpur":
        metro.destroy()
        import vishwavidyalay_iit
    elif s1=="Vishwavidalya" and s2=="Kalyanpur":
        metro.destroy()
        import vishwavidyalay_kalyanpur
    elif s1=="Vishwavidalya" and s2=="LLR Hospital":
        metro.destroy()
        import vishwavidyalay_llr
    elif s1=="Vishwavidalya" and s2=="Moti Jheel":
        metro.destroy()
        import vishwavidyalay_motijheel
    elif s1=="Vishwavidalya" and s2=="Rawatpur":
        metro.destroy()
        import vishwavidyalay_rawatpur
    elif s1=="Vishwavidalya" and s2=="SPM Hospital":
        metro.destroy()
        import vishwavidyalay_spm
    else:
        messagebox.showerror("Error!","Please input a valid station, as mentioned in your left!")

#def station_1(self):
 #   if station1.get()=="  Station 1":
        #station1.delete(0,END)
#def station_2(self):
#    if station2.get()=="  Station 2":
 #       station2.delete(0,END)
#GUI PART-
metro=Tk()
metro.title("Kanpur Metro Portal")
metro.geometry("1100x630")
metro.resizable(FALSE,FALSE)
metro.configure(bg="skyblue2")
myfont=Font(family="Times New Roman",size=30)
myfonnt1=Font(family="Times New Roman",size=26)
myfonnt2=Font(family="Times New Roman",size=25)
myfonnt3=Font(family="Monospaced Font,bold",size=17)
myfonnt4=Font(family="Times New Roman",size=20)
myfonnt5=Font(family="Times New Roman, bold",size=15)
myfonnt6=Font(family="Times New Roman, bold",size=20)
title0=Label(text="Available Stations",bg="darkseagreen3",fg="black",font=myfont,padx=4,pady=8,borderwidth=6,relief=SUNKEN)
title=Label(text="Uttar Pradesh Kanpur Metro Enquiry Portal",bg="papaya whip",fg="black",font=myfont,padx=5,pady=6,borderwidth=6,relief=SUNKEN)
title1=Label(text="Kanpur Metro Map",bg="darkseagreen3",fg="black",font=myfont,padx=105,pady=10,borderwidth=6,relief=SUNKEN)
title5=Label(text="1. Gurudev Chauraha",bg="darkseagreen3",fg="black",font=myfonnt1,padx=1,pady=8,borderwidth=6,relief=SUNKEN)
title6=Label(text="2. IIT Kanpur      ",bg="darkseagreen3",fg="black",font=myfonnt1,padx=22,pady=8,borderwidth=6,relief=SUNKEN)
title7=Label(text="3. Kalyanpur       ",bg="darkseagreen3",fg="black",font=myfonnt1,padx=22,pady=8,borderwidth=6,relief=SUNKEN)
title8=Label(text="4. LLR Hospital    ",bg="darkseagreen3",fg="black",font=myfonnt1,padx=16,pady=8,borderwidth=6,relief=SUNKEN)
title9=Label(text="5. Moti Jheel      ",bg="darkseagreen3",fg="black",font=myfonnt1,padx=26,pady=8,borderwidth=6,relief=SUNKEN)
title10=Label(text="6. Rawatpur       ",bg="darkseagreen3",fg="black",font=myfonnt1,padx=28,pady=8,borderwidth=6,relief=SUNKEN)
title11=Label(text="7. SPM Hospital   ",bg="darkseagreen3",fg="black",font=myfonnt1,padx=19,pady=8,borderwidth=6,relief=SUNKEN)
title12=Label(text="8. Vishwavidalya  ",bg="darkseagreen3",fg="black",font=myfonnt1,padx=19,pady=12,borderwidth=6,relief=SUNKEN)
title2=Label(text="Start Your Journey",bg="skyblue2",fg="brown4",font=myfont,padx=7,pady=6,bd=0,relief=SUNKEN)
title3=Label(text="From",bg="skyblue2",fg="brown4",font=myfonnt2,padx=5,pady=6,bd=0,relief=SUNKEN)
title4=Label(text="To    ",bg="skyblue2",fg="brown4",font=myfonnt2,padx=5,pady=6,bd=0,relief=SUNKEN)
station1=Entry(metro,bg="white",width=27,font=myfonnt3,fg="brown4",bd=2,relief=SUNKEN)
station1.place(x=780,y=250)
station2=Entry(metro,bg="white",width=27,font=myfonnt3,fg="brown4",bd=2,relief=SUNKEN)
station2.place(x=780,y=360)
title3.place(x=780,y=210)
title4.place(x=780,y=320)
title.pack(side=TOP,fill=X)
title1.pack(side=TOP,anchor=NW)
title2.place(x=800,y=135)
title0.place(x=480,y=62)
title5.place(x=483,y=129)
title6.place(x=483,y=192)
title7.place(x=483,y=254)
title8.place(x=483,y=314)
title9.place(x=483,y=375)
title10.place(x=483,y=437)
title11.place(x=483,y=499)
title12.place(x=483,y=559)
image=Image.open("metro_pic2.jpg")
photo=ImageTk.PhotoImage(image)
pic=Label(image=photo)
pic.place(x=0,y=130)
#station1.insert(0,"  Station 1")
#station1.bind("<FocusIn>",station_1)
#station2.insert(0,"  Station 2")
#station2.bind("<FocusIn>",station_2)
searchbutton=Button(metro,text="Search",width=8,bg="darkseagreen3",fg="brown4",font=myfonnt4,activebackground="yellow",padx=3,pady=6,borderwidth=0,relief=SUNKEN,cursor="hand2",command=message)
searchbutton.place(x=860,y=440)
#Needhelpbutton=Button(metro,text="need help?",bg="darkseagreen3",fg="black",font=myfonnt5,border=0,activebackground="darkseagreen3",cursor="hand2")
#Needhelpbutton.place(x=980,y=550)
title13=Label(text="********* need help? *********",bg="skyblue2",fg="brown4",font=myfonnt6,padx=5,pady=6,bd=0)
title13.place(x=790,y=510)
fb_logo=PhotoImage(file="facebook.png")
fblable=Label(metro,image=fb_logo,bg="skyblue2")
fblable.place(x=835,y=560)
google_logo=PhotoImage(file="google.png")
googlelable=Label(metro,image=google_logo,bg="skyblue2")
googlelable.place(x=905,y=560)
twitter_logo=PhotoImage(file="twitter.png")
twitterlable=Label(metro,image=twitter_logo,bg="skyblue2")
twitterlable.place(x=975,y=560)
metro_logo=PhotoImage(file="logo.png")
metrolable=Label(metro,image=metro_logo,bg="skyblue2")
metrolable.place(x=60,y=15)
g20_logo=PhotoImage(file="g20.png")
g20lable=Label(metro,image=g20_logo,bg="papaya whip")
g20lable.place(x=120,y=17)
yogi_logo=PhotoImage(file="yogi.png")
yogilable=Label(metro,image=yogi_logo,bg="papaya whip")
yogilable.place(x=950,y=17)
modi_logo=PhotoImage(file="modi1.png")
modilable=Label(metro,image=modi_logo,bg="papaya whip")
modilable.place(x=1010,y=12)
Frame(metro,width=290,height=2,bg="black").place(x=780,y=180)
Frame(metro,width=30,height=2,bg="black").place(x=10,y=20)
Frame(metro,width=30,height=2,bg="black").place(x=10,y=30)
Frame(metro,width=30,height=2,bg="black").place(x=10,y=40)
#database-
def data():
    nayan=mysql.connector.connect(host="localhost",user="root",password="nayanmishra",database="enquiryportal")
    cur=nayan.cursor()
    s="insert into data1(station_number1,station_number2) values(%s,%s)"
    v=(station1.get(),station2.get())
    cur.execute(s,v)
    nayan.commit()
metro.mainloop()
