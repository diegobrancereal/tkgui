from tkinter import *
from tkinter.messagebox import *
from datetime import *
from PIL import ImageTk, Image, ImageOps
from tkcalendar import DateEntry
from random import *
#Mind that there are quite some things that I can't seem to able to repeat with functions. That's why everything here is quite a bit... long.
#



"""
This system I made is awful and all over the place.



Anyways it seems to work.

Everything is organized, but how the system works is absolutely ghoulish. 

The system is "technically" organized, but at the same time, it's flawed beyond all doubt.
Globals are being used everywhere and are all over the place
"""


#I added a lot of labelframes so that if I don't see that the menu looks good, I can easily adjust positions and change the menu

#One more note, I met all the criteria, but where I met it might not be obvious, some testing is going to have to be done.



def registerAGuestWindow():
    global mega_listbox_of_all_people

    #Basics
    newWin = Toplevel()
    main2 = Frame(newWin)
    newWin.title("Register a guest")
    newWin.geometry("750x550")
    newWin.maxsize(width=750, height=550)
    newWin.minsize(width=750, height=550)
        

    #FUNCTIONS
    
        
    def VerifyAllAndCreateList():
        
        #basic vars
        firstname = firstNameEntryVar.get()
        lastname = lastNameEntryVar.get()
        MaleOrFem = maleOrFemale.get()

        #Gotta calculate to see if age matches with birth date... "skull"
        birthday = dateOfBirth.get().split("/")#Seperated birthday into three indexes
        for i in range(0, len(birthday)):
            birthday[i] = int(birthday[i])

        #print(birthday)
        birthdayYear = birthday[2]
        birthdayMonth = birthday[1]
        #print(birthdayMonth)
        birthdayDay = birthday[0]



        #Current date. Used to caclulate if the person's inputted birthday is valid or not.
        currentmonth = datetime.now().date().month
        currentday = datetime.now().date().day
        currentYear = datetime.now().date().year
        supposedAge = currentYear - birthdayYear - 1
        realAge = ageVal.get()

        if birthdayMonth < currentmonth:
            supposedAge += 1 
            #print(realAge)
        elif birthdayMonth == currentmonth and birthdayDay <= currentday:
            supposedAge += 1


        #Additional vars
        medissues = detailsOfMedIssue.get()
        campName = campsiteName.get()
        cabin_num = cabinNumberVar.get()
        #print(cabin_num)

        #ID num generator 
        identifier = randint(10000, 100000)
        while identityUniqunessVerifier(identifier) != True:#In the rather unlikely event two same id's are generated, it will regenerate an ID until the function that checks for uniquess comes back as true
            identifier = randint(10000, 100000)



    
        if firstname == "":
            showerror("Error", "Please fill in your first name.", parent=newWin)
        elif lastname == "":
            showerror("Error", "Please fill in your last name.", parent=newWin)
        elif realAge <= 12:
            showerror("Error", "You must be 12 years or older in order to be registered! This is a big boy camp!", parent=newWin)
        elif medissues == "":
            showerror("Error", "You must type in medical issues, or write none if you don't have any!", parent=newWin)
        elif supposedAge < realAge or supposedAge > realAge:
            if supposedAge < 0:
                showerror("Error", "Bro you can't be born in the future.", parent=newWin)
            else:
                showerror("Error", f"Curious how you say that you're born on {dateOfBirth.get()} yet you say that you're {realAge}, despite calculations showing that you're supposed to be {supposedAge}", parent=newWin)
        else:
            #Making the full name
            fullName = firstname.strip() + " " + lastname.strip()

            #Adding them to a list. This seems to work fairly well. I like it.
            listOfAllValues = [] + [fullName] + [MaleOrFem] + [birthday] + [realAge] + [medissues] + [campName] + [cabin_num] + [identifier] + [0]
            #print(listOfAllValues)
            RegisteredGuestList.append(listOfAllValues)
            newWin.destroy()
            
    
        
            




        

    
    
    #WIDGETS
    first_frame = LabelFrame(main2, text="Guest's personal information", relief="sunken")######################### FRAME

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
    Soption_frame = LabelFrame(first_frame)######################### FRAME
    sex_option_label = Label(Soption_frame, text="Sex:")

    maleOrFemale = StringVar()
    maleOrFemale.set("Male")
    male_radio_button = Radiobutton(Soption_frame, variable=maleOrFemale, value="Male", text="Male")
    female_radio_button = Radiobutton(Soption_frame, variable=maleOrFemale, value="Female", text="Female")

    #DateofBirth
    doption_frame = LabelFrame(first_frame, relief="flat")######################### FRAME
    date_of_birth_label = Label(doption_frame, text="Date of birth:")
    dateOfBirth = StringVar()
    date_of_birth_num = DateEntry(doption_frame, textvariable=dateOfBirth, state="readonly", date_pattern="d/mm/yyyy")

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
    campsites = ["Genistein", "Daidzein", "Biochanin A"]
    campsiteName = StringVar()
    campsiteName.set("Genizadien")
    campsite_location = OptionMenu(campsite_frame, campsiteName, *campsites)
    campsite_location.config(width=10)

    #Cabin number
    cabin_label = Label(campsite_frame, text="Cabin")
    cabin_list_of_num = []
    for i in range(1, 11):
        cabin_list_of_num.append(i)
    cabinNumberVar = IntVar()
    cabinNumberVar.set(1)
    cabin_number_spinbox = Spinbox(campsite_frame, textvariable=cabinNumberVar, values=cabin_list_of_num, width=10, state="readonly")

   
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
    Soption_frame.grid(row=3, column=1, columnspan=2, sticky=W, pady=5, padx=5)######################### FRAME
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

def registerAGuestForAnActivityWindow():

    newWin = Toplevel()
    main2 = Frame(newWin)
    newWin.geometry("750x650")
    newWin.maxsize(width=750, height=650)
    newWin.minsize(width=750, height=650)

    #Update the dates available to schedule an activity for.
    def updateAvailableDates():
        global availDatesForASpecificActivity
        global numOfSpotsForActivity
        rad_val = radio_button_activity_value.get()
        #I chould have changed them into ints but that would make it harder to read :skull: so I didn't!
        
        if rad_val == "Mountain hiking":
            strVar = "Available only on fridays and saturdays"
            availDatesForASpecificActivity = [2, 3, 9, 10, 16, 17, 23, 24, 30]#Dates of june
            numOfSpotsForActivity = 4

        elif rad_val == "Camping":
            strVar = "Available only on mondays"
            availDatesForASpecificActivity = [5, 12, 19, 26]
            numOfSpotsForActivity = 3
        elif rad_val == "Kayaking":
            strVar = "Available only on weekends"
            availDatesForASpecificActivity = [3, 4, 10, 11, 17, 18, 24, 25]
            numOfSpotsForActivity = 6
        elif rad_val == "Fishing":
            strVar = "Available only on wednesdays"
            availDatesForASpecificActivity = [7, 14, 21, 28]
            numOfSpotsForActivity = 3
        elif rad_val == "Horseback riding":
            strVar = "Available only on weekdays"
            availDatesForASpecificActivity = [5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30]
            numOfSpotsForActivity = 8
        elif rad_val == "Dirt road biking":
            strVar ="Available only on tuesdays"
            availDatesForASpecificActivity = [6, 13, 20, 27]
            numOfSpotsForActivity = 2
        elif rad_val == "Archery":
            strVar = "Available only on thursdays and fridays"
            availDatesForASpecificActivity = [1, 2, 8, 9, 15, 16, 22, 23, 29, 30]
            numOfSpotsForActivity = 5
        elif rad_val == "Rockclimbing":
            strVar = "Available only on weekends"
            availDatesForASpecificActivity = [3, 4, 10, 11, 17, 18, 24, 25]
            numOfSpotsForActivity = 7
        elif rad_val == "Stargazing":
            strVar = "Available only on fridays"
            availDatesForASpecificActivity = [9, 16, 23, 30]
            numOfSpotsForActivity = 1
        elif rad_val == "Bird watching":
            strVar = "Available only on thursdays"
            availDatesForASpecificActivity = [8, 15, 22, 29]
            numOfSpotsForActivity = 2
        
        #print(availabilityVar)
        availabilityVar.set(strVar)

        subtractAvail = 0
        for i in range(0, len(storageOfAllPeopleDoingActivities)):
            if rad_val == storageOfAllPeopleDoingActivities[i][1]:
                subtractAvail += 1
            
        numOfSpotsLeftVar.set(numOfSpotsForActivity - subtractAvail)

        
    def checkifDateIsValid(dateOfActivity):
        #print(dateOfActivity)

        selectedDayValid = False

        for num in availDatesForASpecificActivity:
            if dateOfActivity == num:
                #print(dateOfActivity, num)
                selectedDayValid = True

        return selectedDayValid

    def sendGuestIntoRegisteredForActivitiesBank():

        #THE THREE CHECKS
        #Check if day is valid
        #Check if day is free for that specific activity
        #Check if that activity's schedule isn't full.
        global availDatesForASpecificActivity
        global storageOfAllPeopleDoingActivities
        #I don't even know how to explain whether if this is even ok anymore


        activity = radio_button_activity_value.get()
        
        #Date_list
        date_of_activity = dateEntryVar.get()
        date_list = date_of_activity.split("/")
        #OK IT CONVERTS THE GODDAMN THING INTO A NUMBER. YES I USED THE SAME THING TWICE. I AINT USING IT AGAIN.
        for i in range(0, len(date_list)):
            date_list[i] = int(date_list[i])
        


        #So I can use the number to do actual comparisons
         
        dayOfActivity = date_list[0]#
        

        needTut = needTutVar.get() 
        needAGuard = needsAGuardianVar.get()
        needAddTools = needsAdditionalToolsVar.get()
        #No need to check :skull: listofvalid dates will automatically know if it's valid or not. No need to type if activity is equals to this one thing
        dayValidOrNot = checkifDateIsValid(dayOfActivity)
        #print(dayValidOrNot)
        

        
        

        

        try:
            selectedGuestIndex = mega_listbox_of_all_people.curselection()[0]#Selected Guests name
            #print(RegisteredGuestList[selectedGuestIndex][0])
            selectedGuestsName = RegisteredGuestList[selectedGuestIndex][0]
            selectedGuestsId = RegisteredGuestList[selectedGuestIndex][7]
            selectedGuestsAge = RegisteredGuestList[selectedGuestIndex][3]
            #Oh hey the person apparently now has registered for ONE activity.

            #print(f"The person has been registered for {RegisteredGuestList[selectedGuestIndex][8]} activity")

            #Only one person can register for one activity in a day.
            alreadyRegisteredDay = False
            indexValofP = 0
            global numOfTimesActBeenScheduled
            numOfTimesActBeenScheduled = 0
            
            for index in range(0, len(storageOfAllPeopleDoingActivities)):
                    #Absolutely bizarre way to do this but I think it works.
                    if activity == storageOfAllPeopleDoingActivities[index][1]:
                        numOfTimesActBeenScheduled += 1
                        
                    if activity == storageOfAllPeopleDoingActivities[index][1] and date_list[0] == storageOfAllPeopleDoingActivities[index][2][0]:
                        alreadyRegisteredDay = True
                        
                        indexValofP = index
                        

            #print(numOfTimesActBeenScheduled)
            #print(numOfSpotsForActivity)

            
            if numOfTimesActBeenScheduled != numOfSpotsForActivity:#Is the day on a valid day that it can be scheduled for?

                if dayValidOrNot == True:#Has the times the activity been scheduled for, reached the limit?
                    if alreadyRegisteredDay == False:#Has the activity that you're trying to schedule the Guest for already be scheduled by someone else?
                        GuestActivityProfile = [] + [selectedGuestsName] + [activity] + [date_list] + [selectedGuestsAge] + [needTut] + [needAGuard]+ [needAddTools] + [selectedGuestsId]
                        #print(GuestActivityProfile)
                        storageOfAllPeopleDoingActivities.append(GuestActivityProfile)
                        RegisteredGuestList[selectedGuestIndex][8] += 1
                
                        #Updating the listbox incase you upload it on the same day the listbox is on

                        day = dayInt.get()
                        goThroughAndAppendToSchedule(day)

                        newWin.destroy()

                    else:
                        showerror("Error", f"Looks like {storageOfAllPeopleDoingActivities[indexValofP][0].lower()} is already doing {storageOfAllPeopleDoingActivities[indexValofP][1].lower()} on that day. Please select a different day.", parent=newWin)
                
                else:
                    showerror("Error", "Please enter an available date in in order to register the Guest into the activity.", parent=newWin)
            else:
                showerror("Error", f"{activity} is full, it can only be scheduled {numOfSpotsForActivity} times before the limit is reached", parent=newWin)  
                
        except:
            showerror("Error", "Please select a Guest", parent=newWin)




        


        


        


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

    #Number of spots left
    num_spots_left_label = Label(available_dates_labelframe, text="Number of spots left:")
    numOfSpotsLeftVar = IntVar()
    num_of_spots_left_numLabel = Label(available_dates_labelframe, textvariable=numOfSpotsLeftVar, width=3, bg="#ffffff", relief="sunken")

    updateAvailableDates()

    

    #Date of activity
    dOfAct_labelframe = LabelFrame(second_frame, relief="flat")

    date_of_activity_label = Label(dOfAct_labelframe, text="Date of activity:")
   
    dt1=date(2023,6,1)
    dt2=date(2023,6,30)
    dateEntryVar = StringVar()
    date_entry = DateEntry(dOfAct_labelframe, textvariable=dateEntryVar, mindate=dt1, maxdate=dt2, state="readonly", date_pattern="d/m/yyyy")

    
    #Supplementary activity needs 
    supl_labelframe = LabelFrame(second_frame, relief="flat")

    supplementary_act_needs_label = Label(supl_labelframe, text="Supplementary activity needs")

    needTutVar = BooleanVar()
    need_tutorial_check = Checkbutton(supl_labelframe, variable=needTutVar, text="Needs tutorial", onvalue=True, offvalue=False)

    needsAGuardianVar = BooleanVar()
    need_aguard_check = Checkbutton(supl_labelframe, variable=needsAGuardianVar, text="Needs a guardian", onvalue=True, offvalue=False)

    needsAdditionalToolsVar = BooleanVar()
    need_additionaltools_check = Checkbutton(supl_labelframe, variable=needsAdditionalToolsVar, text="Needs additional tools", onvalue=True, offvalue=False)


    tiny_button_frame = Frame(main2)
    register_button = Button(tiny_button_frame, text="Schedule activity \nfor Guest", width=20, height=3, command=sendGuestIntoRegisteredForActivitiesBank)
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
    available_dates_labelframe.grid(row=3, column=1, ipadx=40)######################### FRAME
    available_dates_label.grid(row=1, column=1)
    available_dates_display.grid(row=1, column=2)

    #Number of spots left
    num_spots_left_label.grid(row=1, column=4)
    num_of_spots_left_numLabel.grid(row=1, column=5)

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
    createAMegaListWithSearchBar(main2, 1, 1, 1, 5, 12, "Select a Guest")
    newWin.grab_set()

    newWin.mainloop()

    
    
def findAGuestWindow():
    newWin = Toplevel()
    main3 = Frame(newWin)
    newWin.title("List of registered guests")
    newWin.geometry("500x650")
    newWin.maxsize(width=500, height=650)
    newWin.minsize(width=500, height=650)

    def seeGuestDetails():
        #Seeing the details of the Guest, and all the activities that they're scheduled in.
        try:
            selectedIndex = mega_listbox_of_all_people.curselection()[0]

            selectedPerson = RegisteredGuestList[selectedIndex]

            #Locate the original information of this Guest


            stringForShow = f"{selectedPerson[0]} is a {selectedPerson[3]} year old {selectedPerson[1].lower()} who was born on {selectedPerson[2][0]}/{selectedPerson[2][1]}/{selectedPerson[2][2]}"
            stringForShow += f"\nThis guest lives in cabin {selectedPerson[6]} at campsite {selectedPerson[5].lower()}"
            stringForShow += f"\n\nMedical issues description: \n{selectedPerson[4]}"
            if selectedPerson[8] == 1:
                stringForShow += f"\n\nThis registered guest has {selectedPerson[8]} scheduled activity, which is:\n"
            elif selectedPerson[8] > 1:
                stringForShow += f"\n\nThis registered guest has {selectedPerson[8]} scheduled activities, which includes\n"
            else:
                stringForShow += f"\n\nThis registered guest has not been scheduled for any activites"
            for i in range(0, len(storageOfAllPeopleDoingActivities)):
            
                if selectedPerson[7] == storageOfAllPeopleDoingActivities[i][7]:

                   stringForShow += f"\n{storageOfAllPeopleDoingActivities[i][1]} at {storageOfAllPeopleDoingActivities[i][2][0]}/{storageOfAllPeopleDoingActivities[i][2][1]}/{storageOfAllPeopleDoingActivities[i][2][2]}"
        
        
            newWin.lower()
            showinfo("Info", stringForShow, parent=newWin)

        except:
            newWin.lower()
            showerror("Error", "Please select a guest first.", parent=newWin)
    

    createAMegaListWithSearchBar(main3, 1, 3, 1, 1, 30, "Bank of all registered guests")

    #See more button
    see_more_button = Button(main3, text="See more", width=20, height=3, command=seeGuestDetails)



    #GRID
    main3.grid(padx=30, pady=30)
    #See more
    see_more_button.grid(row=4, column=1, padx=30, pady=10)
    newWin.grab_set()



    newWin.mainloop()


def findGuestsRegisteredInActivity():
    
    global storageOfAllPeopleDoingActivities
    newWindow = Toplevel()
    firstFrame = Frame(newWindow)
    newWindow.title("All activities and all schedules")


    #List of all people scheduled to do the activity and when they're scheduled to do so.
    people_in_activity_label = Label(firstFrame, text="All people scheduled to do this activity: ")
    peopleInActVar = StringVar()
    peopleInActVar.set([])
    listbox_of_scheduled_people = Listbox(firstFrame, listvariable=peopleInActVar, selectmode=SINGLE, width=60, height=20)

    def findAllGuestsRegisteredForAct(activitySelected):
        desc = ""
        if activitySelected == "Mountain hiking":
            desc = "A lovely hike on the himalayan mountains."

        elif activitySelected == "Camping":
            desc = "Camping down in the fiery woods"

        elif activitySelected == "Kayaking":
            desc = "Kayaking in the longtail river"

        elif activitySelected == "Fishing":
            desc = "Fishing in the fenugreek creek"

        elif activitySelected == "Horseback riding":
            desc = "Horseriding down at the jenson farms"

        elif activitySelected == "Dirt road biking":
            desc = "Biking down the hill at muschraw with a dirt road bike"

        elif activitySelected == "Archery":
            desc = "Shooting arrows at a pile of hay"

        elif activitySelected == "Rockclimbing":
            desc = "Climbing huge mounts of rocks and hills"

        elif activitySelected == "Bird watching":
            desc = "Watching the birds sing and fly "

        descriptionVar.set(desc)
        peopleInActVar.set([])

        for person in storageOfAllPeopleDoingActivities:
            if activitySelected == person[1]:
                specialstr = ""
                specialstr += f"{person[0]} is scheduled to do this activity at {person[2][0]}/{person[2][1]}/{person[2][2]}"
                listbox_of_scheduled_people.insert(END, specialstr)
                


    #Select an activity to see all Guests scheduled to do it, and when.
    select_an_activity_to_see_all_sched_people_label = Label(firstFrame, text="Select an activity")
    listOfActs = ["Mountain hiking", "Camping", "Kayaking", "Fishing", "Horseback riding", "Dirt road biking", "Archery", "Rockclimbing", "Stargazing", "Bird watching"]
    listOfActsVar = StringVar()
    listOfActsVar.set("Mountain hiking")
    activity = OptionMenu(firstFrame, listOfActsVar, *listOfActs, command=findAllGuestsRegisteredForAct)
    activity.config(width=20, height=2)
    
    #Description of activity
    description_of_act_label = Label(firstFrame, text="Description")
    descriptionVar = StringVar()
    descriptionVar.set("")
    desc_label_that_changes = Label(firstFrame, textvariable=descriptionVar, bg="#ffffff", width=50)

    findAllGuestsRegisteredForAct("Mountain hiking")#Ran to make sure stuff starts when the application is opened.


    #GRID
    firstFrame.grid(padx=30, pady=30)
    #See more
    people_in_activity_label.grid(row=1, column=1)
    listbox_of_scheduled_people.grid(row=2, column=1)
    description_of_act_label.grid(row=3, column=1, sticky=N)
    desc_label_that_changes.grid(row=4, column=1, sticky=N)


    select_an_activity_to_see_all_sched_people_label.grid(row=1, column=2, padx=30, sticky=N)
    activity.grid(row=2, column=2, padx=30, sticky=N)
    
    newWindow.grab_set()

    newWindow.mainloop()

# SUPPORTER FUNCTIONS 


def exitWindow(windowToDestroy):
        windowToDestroy.destroy()
        
def createAMegaListWithSearchBar(main, rowNum, rowSpan, columnNum, columnSpan, sizeOfMegaList, textofTitle):

    #THIS MEGA LIST IS MEANT FOR ALL REGISTERED GuestS. 
    global RegisteredGuestList
    listOfAllGuestNames = []
    for person in RegisteredGuestList:
        listOfAllGuestNames.append(person[0])


    megaListFrame = Frame(main)
    

    search_bar_label = Label(megaListFrame, text=textofTitle)
    searchVar = StringVar()
    searchVar.set("")
    search_bar_entry = Entry(megaListFrame, textvariable=searchVar, width=70)


    def updateMegalist(event):
        
        global RegisteredGuestList#is this even necessary
        newList = []
        wordsTyped = searchVar.get()

        mega_listbox_of_all_people.delete(0, END)#gotta clear everyone to make sure the box doesn't go insane.. Doesn't seem to be working???

        if wordsTyped == "":
            megaList.set(listOfAllGuestNames)
        else:


            #DISABLED BECAUSE IT'S CONSIDERED A BACKUP
            """for i in range(0, len(GuestList)): 
                   if wordsTyped.lower() in GuestList[i].lower():
                   newList.append(GuestList[i])"""
            

            for i in range(0, len(listOfAllGuestNames)):
                points = 0
                for j in range(0, len(wordsTyped)):
                    
                    try: #Try is used because since you're going to use the loop length of the wordstyped into the entrybox, it would be extremely wise to ensure that you would not
                        letter = wordsTyped[j].lower()
                        nameLetter = listOfAllGuestNames[i][j].lower()
                        #print(listOfAllGuestNames[i][j].lower())
                        if letter == nameLetter:#Guest name, and then Guest's very first letter
                            #print(wordsTyped[j], listOfAllGuestNames[i][j])
                            points += 1
                            #print(f'POINTS: {points}')
                        Check = True
                    except:
                        #print(f"SKIPPED THE WORD {listOfAllGuestNames[i]}")
                        Check = False#Don't even bother lol
                
                if Check == True and points == len(wordsTyped):
                    newList.append(listOfAllGuestNames[i])#ADDED THE WORD 
                    #print(f"ADDED THE NAME: {listOfAllGuestNames[i]}")


            megaList.set(newList)
        
                    
                    
                        
        
        
                
    search_bar_entry.bind('<KeyRelease>', updateMegalist)


    global megaList
    global mega_listbox_of_all_people
    megaList = StringVar()
    megaList.set(listOfAllGuestNames)
    mega_listbox_of_all_people = Listbox(megaListFrame, listvariable=megaList, selectmode=SINGLE, width=70, height=sizeOfMegaList)
    vertListScroller = Scrollbar(megaListFrame,command = mega_listbox_of_all_people.yview)
    mega_listbox_of_all_people.config(yscrollcommand=vertListScroller.set)
    
    


    #GRIDDING
    megaListFrame.grid(row=rowNum, column=columnNum, rowspan=rowSpan, columnspan=columnSpan)


    search_bar_label.grid(row=0, column=1, sticky=W)
    search_bar_entry.grid(row=1, column=1)
    mega_listbox_of_all_people.grid(row=2, column=1, rowspan=5)
    vertListScroller.grid(row=2, column=2, sticky=NS, rowspan=5)

def identityUniqunessVerifier(id):
        findOutVal = 0
        for person in RegisteredGuestList:
            if id == person[7]:
                findOutVal += 1 
            else:
                findOutVal += 0 
        #print(f'uniqunessval = {findOutVal} ')
        if findOutVal == 0:
            return True
        else:
            return False

    






#MAIN FUNCTIONS

#Functions

def moveToNextDay():
    
    dayNum = dayInt.get()
    monthNum = monthInt.get()
    yearNum = yearInt.get()
    if dayNum == 30:
        showerror("Error", "Date range is limited only in the month of june")
    else:
        dayNum += 1
        dayInt.set(dayNum)
        goThroughAndAppendToSchedule(dayNum)
        
        

    
def movetoYesterday():

    dayNum = dayInt.get()

    if dayNum == 1:
        showerror("Error", "Date range is limited only in the month of june")
    else:
        dayNum -= 1
        dayInt.set(dayNum)
        goThroughAndAppendToSchedule(dayNum)
    
def goThroughAndAppendToSchedule(num):
        #DISABLED
        # allPeopleShownToday.clear()


        # for i in range(0, len(storageOfAllPeopleDoingActivities)):

        #     #checks the entire list
        #     registDay = storageOfAllPeopleDoingActivities[i][2][0]#Day of activity
        #     print(f"{storageOfAllPeopleDoingActivities[i][0]} is doing {storageOfAllPeopleDoingActivities[i][1].lower()} on {storageOfAllPeopleDoingActivities[i][2][0]}")


        #     #Formatting
        #     nameForDisplay = f"{storageOfAllPeopleDoingActivities[i][0]} is doing {storageOfAllPeopleDoingActivities[i][1].lower()} sometime today."

        #     if registDay == num:
        #         print("YAY")
        #         allPeopleShownToday.append(nameForDisplay)
        #         allPeopleShownTodayMirror.append(storageOfAllPeopleDoingActivities[i])
        #         print(allPeopleShownToday)
        #         print(allPeopleShownTodayMirror)

            
        

        # listOfAllPToday.set(allPeopleShownToday)

        schedule_list_box.delete(0, END)
        for i in range(0, len(storageOfAllPeopleDoingActivities)):

             registDay = storageOfAllPeopleDoingActivities[i][2][0]#Day of activity
             #print(f"{storageOfAllPeopleDoingActivities[i][0]} is doing {storageOfAllPeopleDoingActivities[i][1].lower()} on {storageOfAllPeopleDoingActivities[i][2][0]}")


             #Formatting
             nameForDisplay = f"{storageOfAllPeopleDoingActivities[i][0]} is doing {storageOfAllPeopleDoingActivities[i][1].lower()} sometime today."

             if registDay == num:
                 schedule_list_box.insert(END, nameForDisplay)
                 
            







def callback():
    
        #if askokcancel("Quit", "Do you really wish to quit the program?"):
    root.destroy()
    







#MAIN
#All global list variables



global dateForGuest
global RegisteredGuestList
#Name, Sex, Birthday(list), Age, "Health issues", "Camspite", "Cabin #", ID, # of activities the person was scheduled for.
RegisteredGuestList = [["Don eladio", "Male", [14, 11, 2006], 16, "None", "Genistein", 2, 19901, 0], ["Walter White", "Male", [11, 6, 1996], 26, "None", "Genistein", 2, 19301, 0], ["Walter Jr", "Male", [11, 6, 1996], 26, "None", "Genistein", 2, 17301, 0], ["Walter wits", "Male", [11, 6, 1996], 26, "None", "Genistein", 2, 27301, 0], ["Marie", "Female", [11, 6, 1996], 26, "None", "Genistein", 2, 47301, 0]]

global storageOfAllPeopleDoingActivities
storageOfAllPeopleDoingActivities = []#Storage of all people who were scheduled for an activity.

global listOfAllPeopleScheduledForToday
listOfAllPeopleScheduledForToday = []#Only for info.




global allPeopleShownToday
allPeopleShownToday = []#Actual storage box.

root = Tk()
mainframe = Frame(root)
root.geometry("750x600")
root.maxsize(width=750, height=600)
root.minsize(width=750, height=600)
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
register_a_Guest_button = Button(mainframe, text="Register a guest", width=20, height=3, command=registerAGuestWindow)

register_a_Guest_for_an_activity_button = Button(mainframe, text="Schedule an activity \nfor a registered guest", width=20, height=3, command=registerAGuestForAnActivityWindow)

find_a_Guest_button = Button(mainframe, text="Find a registered guest", width=20, height=3, command=findAGuestWindow)

see_list_of_activities_button = Button(mainframe, text="See all programs \n and schedules", width=20, height=3, command=findGuestsRegisteredInActivity)




# Calendar ---------------------------------------------

calendar_frame = LabelFrame(mainframe, width=40, relief="solid")


# Date button

#GIANT SANDWITCH 
left_arrow_button = Button(calendar_frame, text="Yesterday", image=left_arrow_image, command=movetoYesterday)
date_tinyframe = LabelFrame(calendar_frame, border=0)

#Time range is only within the month of june, starting from the first day of june.
dayInt = IntVar()
dayInt.set(1)
day_label = Label(date_tinyframe, textvariable=dayInt, width=2)

slash1_label = Label(date_tinyframe, text="/")#SEPARATOR 

monthInt = IntVar()
monthInt.set(6)
month_label = Label(date_tinyframe, textvariable=monthInt, width=2)

slash2_label = Label(date_tinyframe, text="/")

yearInt = IntVar()
yearInt.set(2023)
year_label = Label(date_tinyframe, textvariable=yearInt, width=4)


right_arrow_button = Button(calendar_frame, text="Next day", image=right_arrow_image, command=moveToNextDay)

#List of all registered Guests
label_for_list_box = Label(mainframe, text="All guests scheduled for an activity today:")
listOfAllPToday = StringVar()
listOfAllPToday.set(allPeopleShownToday)

schedule_list_box = Listbox(calendar_frame, listvariable=listOfAllPToday, selectmode=SINGLE, width=55, font="Arial 10", height=20)









#GRID the widgets
#root.maxsize(width=850, height=650)
#root.minsize(width=650, height=450)
mainframe.grid(padx=50, pady=50)

#MAIN GRID

#Buttons(IPADX AND IPADY COULD BE USED FOR SIZING)
register_a_Guest_button.grid(row=1, column=1, sticky=W)

register_a_Guest_for_an_activity_button.grid(row=2, column=1, sticky=W)
find_a_Guest_button.grid(row=4, column=1, sticky=W)

see_list_of_activities_button.grid(row=5, column=1, sticky=W)

#Calendarframe
calendar_frame.grid(row=1, column=2, rowspan=5, padx=90, sticky=W)

#Label
left_arrow_button.grid(row=1, column=1, sticky=W, ipadx=20, ipady=10)
date_tinyframe.grid(row=1, column=2, sticky=E, ipadx=15)
day_label.grid(row=1, column=1, sticky=EW)
slash1_label.grid(row=1, column=2, sticky=EW)
month_label.grid(row=1, column=3, sticky=EW)
slash2_label.grid(row=1, column=4, sticky=EW)
year_label.grid(row=1, column=5, sticky=EW)
right_arrow_button.grid(row=1, column=3, sticky=E, ipadx=20, ipady=10)

label_for_list_box.grid(row=0, column=2)
schedule_list_box.grid(row=2, column=1, columnspan=3)
root.mainloop()
