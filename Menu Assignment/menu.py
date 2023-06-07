from tkinter import *
from tkinter.messagebox import *
from datetime import *
from PIL import ImageTk, Image, ImageOps
from tkcalendar import DateEntry
#bruh this code is getting out of hand I legitimately can't think of a good way to somehow tinysize these things.
#Attempted to think about how I could downsize everything here only to realize that there would be a LOT of trouble customizing each widget if I had done so.


def registerACamperWindow():
    #Basics
    newWin = Toplevel()
    main2 = Frame(newWin)
    newWin.geometry("750x800")
    newWin.maxsize(width=750, height=800)
    newWin.minsize(width=750, height=800)
        
    #I added a lot of labelframes so that if I don't see that the menu looks good, I can easily adjust positions and change the menu
    
    #WIDGETS
    first_frame = LabelFrame(main2, text="Camper's personal information", relief="sunken")######################### FRAME

    #First name label 
    first_name_label_frame = LabelFrame(first_frame, relief="flat")######################### FRAME
    first_name = Label(first_name_label_frame, text="First name: ")
    firstNameEntryVar = StringVar()
    first_name_entry = Entry(first_name_label_frame, width=30)

    #Second name label
    last_name_label_frame = LabelFrame(first_frame, relief="flat")######################### FRAME
    last_name = Label(last_name_label_frame, text="Last name: ")
    lastNameEntryVar = StringVar()
    last_name_entry = Entry(last_name_label_frame, width=30)


    #Sex select
    Soption_frame = LabelFrame(first_frame, relief="sunken")######################### FRAME
    sex_option_label = Label(Soption_frame, text="Sex:")

    maleOrFemaleOrOther = StringVar()
    maleOrFemaleOrOther.set("Male")
    male_radio_button = Radiobutton(Soption_frame, variable=maleOrFemaleOrOther, value="Male", text="Male")
    female_radio_button = Radiobutton(Soption_frame, variable=maleOrFemaleOrOther, value="Female", text="Female")
    other_radio_button = Radiobutton(Soption_frame, variable=maleOrFemaleOrOther, value="Other", text="Other")

    #DateofBirth
    doption_frame = LabelFrame(first_frame, relief="flat")######################### FRAME
    date_of_birth_label = Label(doption_frame, text="Date of birth:")
    tiny_y_label = Label(doption_frame, text="Y:")
    tiny_y_entry = Entry(doption_frame, width=5)
    tiny_m_label = Label(doption_frame, text="M:")
    tiny_m_entry = Entry(doption_frame, width=5)
    tiny_d_label = Label(doption_frame, text="D:")
    tiny_d_entry = Entry(doption_frame, width=5)

    #Age 
    age_frame = LabelFrame(first_frame, relief="flat")######################### FRAME
    age_label = Label(age_frame, text="Age:")
    ageVal = IntVar()
    ageVal.set(0)
    ageScaler = Scale(age_frame, from_= 0, to=100, orient=HORIZONTAL, variable=ageVal, width=20, length=200, showvalue=False)
    age_display = Label(age_frame, textvariable=ageVal, width=6, bg="#ffffff", relief="sunken") 

    
    


    #Medical info 
    medicalinfo_labelframe = LabelFrame(first_frame, relief="flat", text="Medical information")######################### FRAME
    detailsOfMedIssue = StringVar()
    detailsOfMedIssue.set("")
    details_entry = Entry(medicalinfo_labelframe, textvariable=detailsOfMedIssue, width=50)

    #Register and Cancel widget
    register_button = Button(main2, text="Register")
    cancel_button = Button(main2, text="Cancel")


    #Campsite
    campsite_frame = LabelFrame(first_frame, relief="flat")
    campsite_title = Label(campsite_frame, text="Campsite and location")
    campsite_label = Label(campsite_frame, text="Campsite")
    campsites = ["Genizadien", "Raziadien", "Phasmacosa"]
    campsiteList = StringVar()
    campsiteList.set("Genizadien")
    campsite_location = OptionMenu(campsite_frame, campsiteList, *campsites)

    #Cabin number
    cabin_label = Label(campsite_frame, text="Cabin")
    cabin_list_of_num = []
    for i in range(1, 11):
        cabin_list_of_num.append(i)
    cabin_number = IntVar()
    cabin_number.set(1)
    cabin_number_spinbox = Spinbox(campsite_frame, textvariable=cabin_number, values=cabin_list_of_num)

    #Unit number
    unit_label = Label(campsite_frame, text="Unit")
    unit_list_of_num = []
    for i in range(1, 31):
        unit_list_of_num.append(i)

    unit_number = IntVar()
    unit_number.set(1)
    unit_number_spinbox = Spinbox(campsite_frame, textvariable=unit_number, values=unit_list_of_num)






    #GRIDDING FOR FRIST FRAME
    main2.grid(padx=50, pady=50)
    #First frame
    first_frame.grid(row=1, column=1, padx=30, pady=30, ipadx=20, ipady=30)######################### FRAME

    ###First name label frame
    first_name_label_frame.grid(row=1, column=1, pady=10)#FRAME FOR BOTH WIDS
    first_name.grid(row=1, column=1)
    first_name_entry.grid(row=1, column=2, pady=10)

    ###Last name label frame
    last_name_label_frame.grid(row=1, column=2)#FRAME FOR BOTH WIDS
    last_name.grid(row=1, column=1)
    last_name_entry.grid(row=1, column=2)

    ###Male or female label frame
    Soption_frame.grid(row=3, column=1, columnspan=2, sticky=W, pady=5, padx=20)######################### FRAME
    sex_option_label.grid(row=1, column=1)
    male_radio_button.grid(row=1, column=2)
    female_radio_button.grid(row=1, column=3)
    other_radio_button.grid(row=1, column=4)

    ###Date
    doption_frame.grid(row=4, column=1, pady=10, sticky=W)######################### FRAME
    date_of_birth_label.grid(row=1, column=1)
    tiny_y_label.grid(row=1, column=2)
    tiny_y_entry.grid(row=1, column=3)
    tiny_m_label.grid(row=1, column=4)
    tiny_m_entry.grid(row=1, column=5)
    tiny_d_label.grid(row=1, column=6)
    tiny_d_entry.grid(row=1, column=7)

    #Age
    age_frame.grid(row=4, column=2)
    age_label.grid(row=1, column=8)
    age_display.grid(row=1, column=9)
    ageScaler.grid(row=1, column=10)

    #Campsite location
    campsite_frame.grid(row=6, column=1, columnspan=4, sticky=EW)######################### FRAME
    #Title
    campsite_title.grid(row=1, column=2, sticky=EW)
    #Campsite
    campsite_label.grid(row=2, column=1)
    campsite_location.grid(row=3, column=1)
    #Cabin
    cabin_label.grid(row=2, column=2)
    cabin_number_spinbox.grid(row=3, column=2)
    #Unit
    unit_label.grid(row=2, column=3)
    unit_number_spinbox.grid(row=3, column=3)


    #Medical info
    medicalinfo_labelframe.grid(row=5, column=1, columnspan=2, sticky=W)
    details_entry.grid(row=1, column=1, rowspan=1)#Ask the teacher on how you can make a gigantic entry here, without the use of ipady because you need a lot of writing space.
    










    #SECOND FRAME
    second_frame = LabelFrame(main2, relief="sunken", text="Details of activity")

    


    #Activity #reminder to attach the activity to a description.
    activity_frame = LabelFrame(second_frame, relief="raised")

    activity_label = Label(activity_frame, text="Activity")

    radio_button_activity_value = StringVar()

    radio_button_activity_value.set("Mountain hiking")
    mountain_hiking_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Mountain hiking", text="Mountain hiking")

    camping_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Camping", text="Camping")

    kayaking_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Kayaking", text="Kayaking")

    fishing_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Fishing", text="Fishing")

    horseback_riding_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Horseback riding", text="Horseback riding")

    dirt_road_biking_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Dirt road biking", text="Dirt road biking")

    archery_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Archery", text="Archery")

    rockclimbing_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Rockclimbing", text="Rockclimbing")

    stargazing_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Stargazing", text="Stargazing")

    bird_watching = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Bird watching", text="Bird watching")



    #Date of activity
    dOfAct_labelframe = LabelFrame(second_frame, relief="raised")

    date_of_activity_label = Label(dOfAct_labelframe, text="Date of activity:")
    dateEntryVar = StringVar()
    date_entry = DateEntry(dOfAct_labelframe, textvariable=dateEntryVar)



    #Length of activity
    lengthOfAct_labelframe = LabelFrame(second_frame, relief="raised")
    hourListBox = []
    for i in range(1, 25):
        hourListBox.append(i)
    hourIntVar = IntVar()
    hourIntVar.set(1)
    hour_of_activity = OptionMenu(lengthOfAct_labelframe, hourIntVar, *hourListBox)
    colon_for_time_label = Label(lengthOfAct_labelframe, text=" : ")






    #GRIDDING FOR SECOND FRAME
    second_frame.grid(row=2, column=1, padx=30, pady=30, ipadx=30, ipady=30)



    




    #Activities
    activity_frame.grid(row=2, column=1, sticky=W)######################### FRAME

    activity_label.grid(row=1, column=1, columnspan=2, sticky=EW)

    #First section of activities
    mountain_hiking_activity.grid(row=2, column=1, sticky=W)
    camping_activity.grid(row=2, column=2, sticky=W)
    kayaking_activity.grid(row=2, column=3, stick=W)
    fishing_activity.grid(row=2, column=4, sticky=W)
    horseback_riding_activity.grid(row=2, column=5, sticky=W)

    #Second section of activities
    dirt_road_biking_activity.grid(row=3, column=1, sticky=W)
    archery_activity.grid(row=3, column=2, sticky=W)
    rockclimbing_activity.grid(row=3, column=3, sticky=W)
    stargazing_activity.grid(row=3, column=4, sticky=W)
    bird_watching.grid(row=3, column=5, sticky=W)





    #Date of activity
    dOfAct_labelframe.grid(row=3, column=1, sticky=W)######################### FRAME
    date_of_activity_label.grid(row=1, column=1)
    date_entry.grid(row=1, column=3)

    #Scheduled time for activity
    lengthOfAct_labelframe.grid(row=3, column=2, sticky=W)
    hour_of_activity.grid(row=1, column=1)


    #BUTTONS THAT ARE COMPLETELY OUT OF THE FRAME
    register_button.grid(row=3, column=1, sticky=E)
    cancel_button.grid(row=3, column=2, sticky=E)
    newWin.grab_set()

    newWin.mainloop()
    
    
    
def findACamperWindow():
    newWin = Toplevel()
    main3 = Frame(newWin)
    newWin.title("List of campers")
    newWin.geometry("750x600")
    
    search_bar_label = Label(main3, text="Search bar")
    searchVar = StringVar()
    searchVar.set("")
    search_bar_entry = Entry(main3, textvariable=searchVar, width=70)
    
    def updateMegalist(event):
        
        global CamperList#is this even necessary
        newList = []
        wordsTyped = searchVar.get()

        mega_listbox_of_all_people.delete(0, END)#gotta clear everyone to make sure the box doesn't go insane.. Doesn't seem to be working???

        if wordsTyped == "":
            megaList.set(CamperList)
        else:


            #DISABLED BECAUSE IT'S CONSIDERED A BACKUP
            """for i in range(0, len(CamperList)): 
                   if wordsTyped.lower() in CamperList[i].lower():
                   newList.append(CamperList[i])"""
            

            for i in range(0, len(CamperList)):
                points = 0
                for j in range(0, len(wordsTyped)):
                    
                    try: #Try is used because since you're going to use the loop length of the wordstyped into the entrybox, it would be extremely wise to ensure that you would not
                        letter = wordsTyped[j].lower()
                        nameLetter = CamperList[i][j].lower()
                        if letter == nameLetter:#Camper name, and then camper's very first letter
                            print(wordsTyped[j], CamperList[i][j])
                            points += 1
                            print(f'POINTS: {points}')
                        Check = True
                    except:
                        print(f"SKIPPED THE WORD {CamperList[i]}")
                        Check = False#Don't even bother lol
                
                if Check == True and points == len(wordsTyped):
                    newList.append(CamperList[i])#ADDED THE WORD 
                    print(f"ADDED THE NAME: {CamperList[i]}")


            megaList.set(newList)
        
                    
                    
                        
        
        
                
    search_bar_entry.bind('<KeyRelease>', updateMegalist)
    #Megalist
    megaList = StringVar()
    megaList.set(CamperList)
    mega_listbox_of_all_people = Listbox(main3, listvariable=megaList, selectmode=SINGLE, width=70, height=30)

    #See more button
    see_more_button = Button(main3, text="See more", width=20, height=3)

    #GRID
    main3.grid(padx=30, pady=30)
    #Search bar widgets
    search_bar_label.grid(row=0, column=1, sticky=W)
    search_bar_entry.grid(row=1, column=1)

    #Mega listbox
    mega_listbox_of_all_people.grid(row=2, column=1, rowspan=5)

    #See more
    see_more_button.grid(row=2, column=2, padx=30)
    newWin.grab_set()



    newWin.mainloop()

def callback():
    
        #if askokcancel("Quit", "Do you really wish to quit the program?"):
    root.destroy()
    

#MAIN
#All global list variables



global dateForCamper
global CamperList
CamperList = ["Ga", "Gab", "Gabc", "Gabcd", "Gabcde", "Henry", "Gabbie", "Hesun"]

root = Tk()
mainframe = Frame(root)
root.geometry("750x600")
root.title("Jegg's & Bill's camping registry")
root.protocol("WM_DELETE_WINDOW", callback)


#Images

#Left arrow Image
left_raw = Image.open('left-arrow.png')#Could have opened it another way but this works well too I guess
resized_left = left_raw.resize((32, 30))#Resizes theimage
left_arrow_image = ImageTk.PhotoImage(resized_left) #Display's the image

#Right arrow Image
flipped_left = ImageOps.mirror(resized_left) # Flips the image
right_arrow_image = ImageTk.PhotoImage(flipped_left)



#Buttons 
register_a_camper_button = Button(mainframe, text="Register a camper", width=20, height=3, command=registerACamperWindow)

find_a_camper_button = Button(mainframe, text="Find a camper", width=20, height=3, command=findACamperWindow)

see_list_of_activities_button = Button(mainframe, text="See list of activites", width=20, height=3)

see_more_button = Button(mainframe, text="see more", width=20, height=3)




# Calendar ---------------------------------------------

calendar_frame = LabelFrame(mainframe, width=40, relief="solid")


# Date button

left_arrow_button = Button(calendar_frame, text="Yesterday", image=left_arrow_image)
date_label = Label(calendar_frame, text="DATE HERE")
right_arrow_button = Button(calendar_frame, text="Next day", image=right_arrow_image)

#List of all registered campers
listOfAllPToday = StringVar()
listOfAllPToday.set(CamperList)

schedule_list_box = Listbox(calendar_frame, listvariable=listOfAllPToday, selectmode=SINGLE, width=55, font="Arial 10", height=20)









#GRID the widgets
#root.maxsize(width=850, height=650)
#root.minsize(width=650, height=450)
mainframe.grid(padx=50, pady=50)

#MAIN GRID

#Buttons(IPADX AND IPADY COULD BE USED FOR SIZING)
register_a_camper_button.grid(row=1, column=1, sticky=W)

find_a_camper_button.grid(row=4, column=1, sticky=W)

see_list_of_activities_button.grid(row=5, column=1, sticky=W)

see_more_button.grid(row=6, column=2)
#Calendarframe
calendar_frame.grid(row=1, column=2, rowspan=5, padx=90, sticky=W)

#Label
left_arrow_button.grid(row=1, column=1, sticky=W, ipadx=20, ipady=10)
date_label.grid(row=1, column=2, ipadx=60, ipady=10)
right_arrow_button.grid(row=1, column=3, sticky=E, ipadx=20, ipady=10)

schedule_list_box.grid(row=2, column=1, columnspan=3)
root.mainloop()
