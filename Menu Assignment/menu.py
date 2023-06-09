from tkinter import *
from tkinter.messagebox import *
from datetime import *
from PIL import ImageTk, Image, ImageOps
from tkcalendar import DateEntry
#bruh this code is getting out of hand I legitimately can't think of a good way to somehow tinysize these things.
#Attempted to think about how I could downsize everything here only to realize that there would be a LOT of trouble customizing each widget if I had done so.
#BRO I LEGIT USED LABELFRAME THINKING THAT WAS THE ONLY FRAME THIGN THERE WAS, APPARENTLY FRAME WORKS TOO. BRUHHHHHH
def registerACamperWindow():
    global mega_listbox_of_all_people
    #Basics
    newWin = Toplevel()
    main2 = Frame(newWin)
    newWin.geometry("750x550")
    newWin.maxsize(width=750, height=550)
    newWin.minsize(width=750, height=550)
        

    #FUNCTIONS

    def VerifyAllAndCreateList():
        
        firstname = firstNameEntryVar.get()
        lastname = lastNameEntryVar.get()
        
        MaleOrFem = maleOrFemale.get()

        #Gotta calculate to see if age matches with birth date... "skull"
        birthday = dateOfBirth.get().split("/")#Seperated birthday into three indexes

        

        birthdayYear = int(birthday[2])
        birthdayMonth = int(birthday[1])
        print(birthdayMonth)
        birthdayDay = int(birthday[0])


        currentmonth = datetime.now().date().month
        currentday = datetime.now().date().day
        currentYear = datetime.now().date().year
        supposedAge = currentYear - birthdayYear - 1
        realAge = ageVal.get()

        if birthdayMonth < currentmonth:
            supposedAge += 1 
            print(realAge)
        elif birthdayMonth == currentmonth and birthdayDay <= currentday:
            supposedAge += 1


        medissues = detailsOfMedIssue.get()
        campName = campsiteName.get()
        cabin_num = cabin_number.get()
        
        
        if firstname == "":
            showerror("Error", "Please fill in your first name.")
        elif lastname == "":
            showerror("Error", "Please fill in your last name.")
        elif realAge <= 12:
            showerror("Error", "You must be 12 years or older in order to be registered! This is a big boy camp!")
        elif medissues == "":
            showerror("Error", "You must type in medical issues, or write none if you don't have any!")
        elif supposedAge < realAge or supposedAge > realAge:
            if supposedAge > 0:
                showerror("Error", "Bro you can't be born in the future.")
            showerror("Error", f"Curious how you say that you're born on {dateOfBirth.get()} yet you say that you're {realAge}, despite calculations showing that you're supposed to be {supposedAge}")
        else:
            #Making the full name
            fullName = firstname + " " + lastname

            #Adding them to a list. This seems to work fairly well. I like it.
            listOfAllValues = [] + [fullName] + [MaleOrFem] + [birthday] + [medissues] + [campName] + [cabin_num]
            print(listOfAllValues)
            RegisteredCamperList.append(listOfAllValues)
            newWin.destroy()
            
    
        
            




        

    #I added a lot of labelframes so that if I don't see that the menu looks good, I can easily adjust positions and change the menu
    
    #WIDGETS
    first_frame = LabelFrame(main2, text="Camper's personal information", relief="sunken")######################### FRAME

    #First name label 
    first_name_label_frame = LabelFrame(first_frame, relief="flat")######################### FRAME
    first_name = Label(first_name_label_frame, text="First name: ")
    firstNameEntryVar = StringVar()
    first_name_entry = Entry(first_name_label_frame, width=30, textvariable=firstNameEntryVar)

    #Second name label
    last_name_label_frame = LabelFrame(first_frame, relief="flat")######################### FRAME
    last_name = Label(last_name_label_frame, text="Last name: ")
    lastNameEntryVar = StringVar()
    last_name_entry = Entry(last_name_label_frame, width=30, textvariable=lastNameEntryVar)


    #Sex select
    Soption_frame = LabelFrame(first_frame, relief="sunken")######################### FRAME
    sex_option_label = Label(Soption_frame, text="Sex:")

    maleOrFemale = StringVar()
    maleOrFemale.set("Male")
    male_radio_button = Radiobutton(Soption_frame, variable=maleOrFemale, value="Male", text="Male")
    female_radio_button = Radiobutton(Soption_frame, variable=maleOrFemale, value="Female", text="Female")

    #DateofBirth
    doption_frame = LabelFrame(first_frame, relief="flat")######################### FRAME
    date_of_birth_label = Label(doption_frame, text="Date of birth:")
    dateOfBirth = StringVar()
    date_of_birth_num = DateEntry(doption_frame, textvariable=dateOfBirth, state="readonly", date_pattern="dd/mm/yyyy")

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

    


    #Campsite
    campsite_frame = LabelFrame(first_frame, relief="flat")
    campsite_title = Label(campsite_frame, text="Campsite and location")
    campsite_label = Label(campsite_frame, text="Campsite")
    campsites = ["Genizadien", "Raziadien", "Phasmacosa"]
    campsiteName = StringVar()
    campsiteName.set("Genizadien")
    campsite_location = OptionMenu(campsite_frame, campsiteName, *campsites)
    campsite_location.config(width=10)

    #Cabin number
    cabin_label = Label(campsite_frame, text="Cabin")
    cabin_list_of_num = []
    for i in range(1, 11):
        cabin_list_of_num.append(i)
    cabin_number = IntVar()
    cabin_number.set(1)
    cabin_number_spinbox = Spinbox(campsite_frame, textvariable=cabin_number, values=cabin_list_of_num, width=10, state="readonly")

    #Register and Cancel widget
    tiny_button_frame = Frame(main2)
    register_button = Button(tiny_button_frame, text="Register", width=20, height=3, command=VerifyAllAndCreateList)
    cancel_button = Button(tiny_button_frame, text="Cancel", width=20, height=3, command= lambda: exitWindow(newWin))

    

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

    ###Date
    doption_frame.grid(row=4, column=1, pady=10, sticky=W)######################### FRAME
    date_of_birth_label.grid(row=1, column=1)
    date_of_birth_num.grid(row=1, column=2)

    #Age
    age_frame.grid(row=4, column=2)
    age_label.grid(row=1, column=8)
    age_display.grid(row=1, column=9)
    ageScaler.grid(row=1, column=10)

    #Campsite location
    campsite_frame.grid(row=6, column=1, columnspan=2, sticky=W, padx=60)######################### FRAME
    #Title
    campsite_title.grid(row=1, column=1, columnspan=2, sticky=EW)
    #Campsite
    campsite_label.grid(row=2, column=1, sticky=EW)
    campsite_location.grid(row=3, column=1, sticky=EW)
    #Cabin
    cabin_label.grid(row=2, column=2, sticky=EW)
    cabin_number_spinbox.grid(row=3, column=2, sticky=E)

    #Medical info
    medicalinfo_labelframe.grid(row=5, column=1, columnspan=2, sticky=W)
    details_entry.grid(row=1, column=1, rowspan=1)#Ask the teacher on how you can make a gigantic entry here, without the use of ipady because you need a lot of writing space.
    








    #BUTTONS THAT ARE COMPLETELY OUT OF THE FRAME
    tiny_button_frame.grid(row=3, column=1)
    register_button.grid(row=1, column=1, sticky=E)
    cancel_button.grid(row=1, column=2, sticky=E)
    newWin.grab_set()

    newWin.mainloop()

def registerACamperForAnActivity():

    newWin = Toplevel()
    main2 = Frame(newWin)
    newWin.geometry("750x800")
    newWin.maxsize(width=750, height=800)
    newWin.minsize(width=750, height=800)


    def updateAvailableDates():
        global availDatesForASpecificActivity

        rad_val = radio_button_activity_value.get()
        #I chould have changed them into ints but that would make it harder to read :skull: so I didn't!
        
        if rad_val == "Mountain hiking":
            strVar = "Available only on fridays and saturdays"
            availDatesForASpecificActivity = [2, 3, 9, 10, 16, 17, 23, 24]#Dates of june

        elif rad_val == updateAvailableDates():
            strVar = "Available only on mondays"
            availDatesForASpecificActivity = [5, 12, 19, 26]

        elif rad_val == "Kayaking":
            strVar = "Available only on weekends"
            availDatesForASpecificActivity = [3, 4, 10, 11, 17, 18, 24, 25]
        
        elif rad_val == "Fishing":
            strVar = "Available only on wednesdays"
            availDatesForASpecificActivity = [7, 14, 21, 28]

        elif rad_val == "Horseback riding":
            strVar = "Available only on weekdays"
            availDatesForASpecificActivity = [5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30]

        elif rad_val== "Dirt road biking":
            strVar ="Available only on tuesdays"
            availDatesForASpecificActivity = [5, 12, 19, 26]

        elif rad_val == "Archery":
            strVar = "Available only on thursdays and fridays"
            availDatesForASpecificActivity = [8, 9, 15, 16, 22, 23, 29, 30]

        elif rad_val == "Rockclimbing":
            strVar = "Available only on weekends"
            availDatesForASpecificActivity = [3, 4, 10, 11, 17, 18, 24, 25]

        elif rad_val == "Stargazing":
            strVar = "Available only on fridays"
            availDatesForASpecificActivity = [9, 16, 23, 30]
        elif rad_val == "Bird watching":
            strVar = "Available only on thursdays"
            availDatesForASpecificActivity = [8, 15, 22, 29]
        
        print(availabilityVar)
        availabilityVar.set(strVar)
        
    def checkifDateIsValid(dateOfActivity):
        selectedDayValid = False

        for num in availDatesForASpecificActivity:
            if dateOfActivity == num:
                print(dateOfActivity, num)
                selectedDayValid = True

        return selectedDayValid

    def register_camper_for_activity():
        global availDatesForASpecificActivity
        #I don't even know how to explain whether if this is even ok anymore
        createActivityDayProfileForCamper = []
        activity = radio_button_activity_value.get()
        date_of_activity = dateEntryVar.get()
        date_list = date_of_activity.split("/")
        try: 
            dayOfActivity = int(date_list[0])
        except: 
            dayOfActivity = int(date_list[0].replace("0", ""))
        print(dayOfActivity)
        #No need to check :skull: listofvalid dates will automatically know if it's valid or not. No need to type if activity is equals to this one thing
        dayValidOrNot = checkifDateIsValid(dayOfActivity)
        print(dayValidOrNot)
        

            

        # needTut = needTutVar.get()
        # try:
        #     selectedCamper = mega_listbox_of_all_people.curselection()[0]
        #     camperActivityInfo = []
            

        # except:
        #     showerror("Error", "Please select a camper to register an activity for")


        


        


    #SECOND FRAME
    second_frame = LabelFrame(main2, relief="sunken", text="Details of activity")

    


    #Activity #reminder to attach the activity to a description.
    activity_frame = LabelFrame(second_frame, relief="flat")

    activity_label = Label(activity_frame, text="Activity")

    radio_button_activity_value = StringVar()

    radio_button_activity_value.set("Mountain hiking")
    mountain_hiking_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Mountain hiking", text="Mountain hiking", command=updateAvailableDates)# Fri AND Sat

    camping_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Camping", text="Camping", command=updateAvailableDates)# 

    kayaking_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Kayaking", text="Kayaking", command=updateAvailableDates)

    fishing_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Fishing", text="Fishing", command=updateAvailableDates)

    horseback_riding_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Horseback riding", text="Horseback riding", command=updateAvailableDates)

    dirt_road_biking_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Dirt road biking", text="Dirt road biking", command=updateAvailableDates)

    archery_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Archery", text="Archery", command=updateAvailableDates)

    rockclimbing_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Rockclimbing", text="Rockclimbing", command=updateAvailableDates)

    stargazing_activity = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Stargazing", text="Stargazing", command=updateAvailableDates)

    bird_watching = Radiobutton(activity_frame, variable=radio_button_activity_value, value="Bird watching", text="Bird watching", command=updateAvailableDates)
    

    #Available dates
    available_dates_labelframe = LabelFrame(second_frame, relief="flat")
    available_dates_label = Label(available_dates_labelframe, text="Available dates:")
    availabilityVar = StringVar()
    availabilityVar.set("Available on mondays")
    available_dates_display = Label(available_dates_labelframe, textvariable=availabilityVar, width=40, bg="#ffffff")
    updateAvailableDates()
    #Date of activity
    dOfAct_labelframe = LabelFrame(second_frame, relief="flat")

    date_of_activity_label = Label(dOfAct_labelframe, text="Date of activity:")
   
    dt1=date(2023,6,1)
    dt2=date(2023,6,30)
    dateEntryVar = StringVar()
    date_entry = DateEntry(dOfAct_labelframe, textvariable=dateEntryVar, mindate=dt1, maxdate=dt2, state="readonly", date_pattern="dd/mm/yyyy")


    #Supplementary activity needs 
    supl_labelframe = LabelFrame(second_frame, relief="flat")

    supplementary_act_needs_label = Label(supl_labelframe, text="Supplementary activity needs")

    needTutVar = StringVar()
    need_tutorial_check = Checkbutton(supl_labelframe, variable=needTutVar, text="Needs tutorial", onvalue="Yes", offvalue="No")

    needsAGuardianVar = StringVar()
    need_aguard_check = Checkbutton(supl_labelframe, variable=needsAGuardianVar, text="Needs a guardian", onvalue="Yes", offvalue="No")

    needsAdditionalToolsVar = StringVar()
    need_additionaltools_check = Checkbutton(supl_labelframe, variable=needsAdditionalToolsVar, text="Needs additional tools", onvalue="Yes", offvalue="No")


    tiny_button_frame = Frame(main2)
    register_button = Button(tiny_button_frame, text="Register for activity", width=20, height=3, command=register_camper_for_activity)
    cancel_button = Button(tiny_button_frame, text="Cancel", width=20, height=3, command= lambda: exitWindow(newWin))

    #GRIDDING
    main2.grid(padx=10, pady=10)





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


    #Available dates
    available_dates_labelframe.grid(row=3, column=1, ipadx=40)
    available_dates_label.grid(row=1, column=1)
    available_dates_display.grid(row=1, column=2)
    #Date of activity
    dOfAct_labelframe.grid(row=4, column=1, sticky=EW)######################### FRAME
    date_of_activity_label.grid(row=1, column=1)
    date_entry.grid(row=1, column=3)

    #Supplementary activity needs
    supl_labelframe.grid(row=5, column=1)
    supplementary_act_needs_label.grid(row=1, column=1, columnspan=3, sticky=EW)
    need_tutorial_check.grid(row=2, column=1)
    need_aguard_check.grid(row=2, column=2)
    need_additionaltools_check.grid(row=2, column=3)
    #Gay
    tiny_button_frame.grid(row=6, column=1)
    register_button.grid(row=1, column=1)
    cancel_button.grid(row=1, column=2)
    createAMegaListWithSearchBar(main2, 1, 1, 1, 5, 20, "Select a camper")
    newWin.grab_set()

    newWin.mainloop()

    
    
def findACamperWindow():
    newWin = Toplevel()
    main3 = Frame(newWin)
    newWin.title("List of campers")
    newWin.geometry("750x600")
    
    createAMegaListWithSearchBar(main3, 1, 3, 1, 1, 30, "Find a camper")
    #See more button
    see_more_button = Button(main3, text="See more", width=20, height=3)

    #GRID
    main3.grid(padx=30, pady=30)
    #See more
    see_more_button.grid(row=2, column=2, padx=30)
    newWin.grab_set()



    newWin.mainloop()

def callback():
    
        #if askokcancel("Quit", "Do you really wish to quit the program?"):
    root.destroy()
    



# SUPPORTER FUNCTIONS 


def exitWindow(windowToDestroy):
        windowToDestroy.destroy()
        
def createAMegaListWithSearchBar(main, rowNum, rowSpan, columnNum, columnSpan, sizeOfMegaList, textofTitle):
    global RegisteredcamperList
    listOfAllCamperNames = []
    for person in RegisteredCamperList:
        listOfAllCamperNames.append(person[0])


    megaListFrame = Frame(main)
    

    search_bar_label = Label(megaListFrame, text=textofTitle)
    searchVar = StringVar()
    searchVar.set("")
    search_bar_entry = Entry(megaListFrame, textvariable=searchVar, width=70)


    def updateMegalist(event):
        
        global RegisteredCamperList#is this even necessary
        newList = []
        wordsTyped = searchVar.get()

        mega_listbox_of_all_people.delete(0, END)#gotta clear everyone to make sure the box doesn't go insane.. Doesn't seem to be working???

        if wordsTyped == "":
            megaList.set(listOfAllCamperNames)
        else:


            #DISABLED BECAUSE IT'S CONSIDERED A BACKUP
            """for i in range(0, len(CamperList)): 
                   if wordsTyped.lower() in CamperList[i].lower():
                   newList.append(CamperList[i])"""
            

            for i in range(0, len(listOfAllCamperNames)):
                points = 0
                for j in range(0, len(wordsTyped)):
                    
                    try: #Try is used because since you're going to use the loop length of the wordstyped into the entrybox, it would be extremely wise to ensure that you would not
                        letter = wordsTyped[j].lower()
                        nameLetter = listOfAllCamperNames[i][j].lower()
                        print(listOfAllCamperNames[i][j].lower())
                        if letter == nameLetter:#Camper name, and then camper's very first letter
                            print(wordsTyped[j], listOfAllCamperNames[i][j])
                            points += 1
                            print(f'POINTS: {points}')
                        Check = True
                    except:
                        print(f"SKIPPED THE WORD {listOfAllCamperNames[i]}")
                        Check = False#Don't even bother lol
                
                if Check == True and points == len(wordsTyped):
                    newList.append(listOfAllCamperNames[i])#ADDED THE WORD 
                    print(f"ADDED THE NAME: {listOfAllCamperNames[i]}")


            megaList.set(newList)
        
                    
                    
                        
        
        
                
    search_bar_entry.bind('<KeyRelease>', updateMegalist)


    global megaList
    global mega_listbox_of_all_people
    megaList = StringVar()
    megaList.set(listOfAllCamperNames)
    mega_listbox_of_all_people = Listbox(megaListFrame, listvariable=megaList, selectmode=SINGLE, width=70, height=sizeOfMegaList)
    vertListScroller = Scrollbar(megaListFrame,command = mega_listbox_of_all_people.yview)
    mega_listbox_of_all_people.config(yscrollcommand=vertListScroller.set)
    
    


    #GRIDDING
    megaListFrame.grid(row=rowNum, column=columnNum, rowspan=rowSpan, columnspan=columnSpan)


    search_bar_label.grid(row=0, column=1, sticky=W)
    search_bar_entry.grid(row=1, column=1)
    mega_listbox_of_all_people.grid(row=2, column=1, rowspan=5)
    vertListScroller.grid(row=2, column=2, sticky=NS, rowspan=5)

#MAIN
#All global list variables



global dateForCamper
global RegisteredCamperList
RegisteredCamperList = [["Don eladio"], ["Gustavo fring"], ["Heisenberg"], ["Jesse pinkman"]]

global storageOfAllPeopleDoingActivities
storageOfAllPeopleDoingActivities = []
global allPeopleShownToday
allPeopleShownToday = []
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

register_a_camper_for_an_activity_button = Button(mainframe, text="Register a camper \nfor an activity", width=20, height=3, command=registerACamperForAnActivity)

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
listOfAllPToday.set(allPeopleShownToday)

schedule_list_box = Listbox(calendar_frame, listvariable=allPeopleShownToday, selectmode=SINGLE, width=55, font="Arial 10", height=20)









#GRID the widgets
#root.maxsize(width=850, height=650)
#root.minsize(width=650, height=450)
mainframe.grid(padx=50, pady=50)

#MAIN GRID

#Buttons(IPADX AND IPADY COULD BE USED FOR SIZING)
register_a_camper_button.grid(row=1, column=1, sticky=W)

register_a_camper_for_an_activity_button.grid(row=2, column=1, sticky=W)
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
