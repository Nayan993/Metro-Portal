from tkinter import*
from tkinter.font import Font
metro1=Tk()
#function part
def back():
    metro1.destroy()
    import kanpur_metro
    
#gui part
metro1.title("GURUDEV CHAURAHA TO RAWATPUR")
metro1.geometry("650x590")
metro1.resizable(0,0)
metro1.configure(bg="thistle1")
myfont=Font (family="Times New Roman",size=25)
myfont1=Font (family="Times New Roman",size=20)
myfont2=Font (family="Times New Roman",size=18)
title=Label(text="--GURUDEV CHAURAHA TO RAWATPUR--",bg="thistle3",fg="firebrick4",font=myfont,padx=5,pady=6,borderwidth=5,relief=RIDGE)
title.pack(side=TOP,fill=X)
title0=Label(text="Thanks For Travelling With Us",bg="thistle1",fg="firebrick4",font=myfont,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title0.pack(side=TOP,fill=X)
#first metro1
title1=Label(text="First Metro",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title1.place(x=127,y=110)
#last metro1
title2=Label(text="Last Metro",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title2.place(x=127,y=150)
#distance
title3=Label(text="Distance",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title3.place(x=127,y=190)
#time
title4=Label(text="Journey Period",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title4.place(x=127,y=230)
#stations
title5=Label(text="Total Inbetween Stations",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title5.place(x=127,y=270)
#fare
title6=Label(text="Net fare",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title6.place(x=127,y=310)
#metro1 parking
title7=Label(text="Metro Parking",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title7.place(x=127,y=350)
#layout
title8=Label(text="Layout",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title8.place(x=127,y=390)
#platform type
title9=Label(text="Platform Type",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title9.place(x=127,y=430)
#naerby locations
title10=Label(text="Nearby Locations",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title10.place(x=127,y=470)
#first metro1 ans
title1=Label(text="06:08 AM",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title1.place(x=330,y=110)
#last metro1 ans
title2=Label(text="10:08 PM",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title2.place(x=330,y=150)
#distance ans
title3=Label(text="2 KM",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title3.place(x=330,y=190)
#time ans
title4=Label(text="00:03:38",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title4.place(x=330,y=230)
#stations ans
title5=Label(text="2",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title5.place(x=350,y=270)
#fare ans
title6=Label(text="--",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title6.place(x=330,y=310)
#metro1 parking ans
title7=Label(text="Yes",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title7.place(x=330,y=350)
#layout ans
title8=Label(text="Elevated",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title8.place(x=330,y=390)
#platform type ans
title9=Label(text="Side",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title9.place(x=330,y=430)
#naerby locations ans
title10=Label(text="Rave@moti mall, Fashion factory etc.",bg="thistle1",fg="firebrick4",font=myfont1,padx=5,pady=6,borderwidth=0,relief=SUNKEN)
title10.place(x=330,y=470)
Frame(metro1,width=400,height=2,bg="firebrick4").place(x=127,y=90)
Frame(metro1,width=100,height=2,bg="firebrick4").place(x=127,y=150)
Frame(metro1,width=100,height=2,bg="firebrick4").place(x=127,y=190)
Frame(metro1,width=80,height=2,bg="firebrick4").place(x=127,y=230)
Frame(metro1,width=130,height=2,bg="firebrick4").place(x=127,y=270)
Frame(metro1,width=205,height=2,bg="firebrick4").place(x=127,y=310)
Frame(metro1,width=80,height=2,bg="firebrick4").place(x=127,y=350)
Frame(metro1,width=120,height=2,bg="firebrick4").place(x=127,y=390)
Frame(metro1,width=70,height=2,bg="firebrick4").place(x=127,y=430)
Frame(metro1,width=125,height=2,bg="firebrick4").place(x=127,y=470)
Frame(metro1,width=150,height=2,bg="firebrick4").place(x=127,y=510)
#newframes
Frame(metro1,width=100,height=2,bg="firebrick4").place(x=327,y=150)
Frame(metro1,width=100,height=2,bg="firebrick4").place(x=327,y=190)
Frame(metro1,width=80,height=2,bg="firebrick4").place(x=327,y=230)
Frame(metro1,width=90,height=2,bg="firebrick4").place(x=327,y=270)
Frame(metro1,width=40,height=2,bg="firebrick4").place(x=347,y=310)
Frame(metro1,width=70,height=2,bg="firebrick4").place(x=327,y=350)
Frame(metro1,width=70,height=2,bg="firebrick4").place(x=327,y=390)
Frame(metro1,width=85,height=2,bg="firebrick4").place(x=327,y=430)
Frame(metro1,width=55,height=2,bg="firebrick4").place(x=327,y=470)
Frame(metro1,width=310,height=2,bg="firebrick4").place(x=327,y=510)
metro1_logo=PhotoImage(file="metro3.png")
metro1lable=Label(metro1,image=metro1_logo,bg="thistle3")
metro1lable.place(x=30,y=5)
g20_logo=PhotoImage(file="g20.png")
g20lable=Label(metro1,image=g20_logo,bg="thistle3")
g20lable.place(x=570,y=12)
#back button
backbutton=Button(metro1,text="Back",width=8,bg="darkseagreen3",fg="firebrick4",font=myfont2,activebackground="yellow",padx=3,pady=6,borderwidth=0,relief=SUNKEN,cursor="hand2",command=back)
backbutton.place(x=250,y=535)
metro1.mainloop()