from tkinter import *
Newspaper = Tk()
Newspaper.geometry("744x133")
Newspaper.title("Newspaper")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text ='''DATE- 6-08-2023   ****KANPUR TIMES****      DAY- SUNADAY''', bg ="WHITE", fg="BLACK", padx=5, pady=10, font="calligrapher 30", borderwidth=8, relief=GROOVE)
title1_label = Label(text ='''***NATIONAL NEWS***''', bg ="YELLOW", fg="BLACK", padx=8, pady=10, font="calligrapher 30", borderwidth=8, relief=GROOVE) 
title0_label = Label(text ='''***EDUCATIONAL NEWS***''', bg ="YELLOW", fg="BLACK", padx=8, pady=10, font="calligrapher 30", borderwidth=8, relief=GROOVE) 
title2_label = Label(text ='''Jammu and Kashmir Lieutenant Governor Manoj Sinha said on August 6that the era of separatist and 
terror organisations disrupting normalife in the Valley on Pakistan's prodding has been relegated to pages of history, and development
 and peace are the buzzword here four years after the abrogation of Article 370.In interaction with a group of journalists,Mr. Sinha said 
 it is now entirely up to the Election Commission to take a callon holding Assembly elections in the Union Territory after the completion 
 of the delimitation exercise and revision of electoral rolls.“J-K administration will follow what the Election Commission of India decides,” 
 he said while noting thatover 32,000 elected representatives of various local bodies are very much part ofthe decision-making process in the 
 UT.nHome Minister Amit Shah had given assurancein Parliament that assembly elections will follow the delimitation exercise and that Jammu and Kashmir 
 will also get its statehood at an appropriate time, he noted.''', bg ="WHITE", fg="BLACK", padx=5, pady=5, font="calligrapher 15", borderwidth=8, relief=GROOVE) 
title3_label = Label(text ='''While IIM Lucknow is currently inviting applications for CAT 2023,
there are several other options where students can apply,in order toget admission in management schools.
Check details about some of these management entrance exams''', bg ="WHITE", fg="BLACK", padx=8, pady=10, font="calligrapher 30", borderwidth=8, relief=GROOVE) 
title4_label = Label(text ='''***SPORTS NEWS***''', bg ="YELLOW", fg="BLACK", padx=8, pady=10, font="calligrapher 30", borderwidth=8, relief=GROOVE)
title5_label = Label(text ='''Wrestlers federation election battle: Brij Bhushan’s aide vs witness against him in sexual harassment case vie
for presidencyCandidates chosen by the former WFI chief, who is facing sexual harassment charges, will contest for all 15 posts, including president
, general secretary and treasurer.''', bg ="WHITE", fg="BLACK", padx=8, pady=10, font="calligrapher 30", borderwidth=8, relief=GROOVE)  
title6_label = Label(text ='''EDITOR - NAYAN MISHRA''', bg ="GREEN", fg="BLACK", padx=8, pady=10, font="calligrapher 30", borderwidth=8, relief=GROOVE) 
# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

title_label.pack(side=TOP, fill=X)
title1_label.pack(side=TOP,fill=X)
title2_label.pack(side=TOP,fill=X)
title0_label.pack(side=TOP,fill=X)
title3_label.pack(side=TOP,fill=X)
title4_label.pack(side=TOP,fill=X)
title5_label.pack(side=TOP,fill=X)
title6_label.pack(side=BOTTOM,anchor=NE)
Newspaper.mainloop()


